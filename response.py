#!/usr/bin/python3
# -*- coding: utf-8 -*-

from header import *

class Action:
	
	def __init__(self, chaine):
		self.copy = chaine
		self.chaine = chaine.lower().strip().split()
		self.difficulty = len(self.chaine)
		self.meaning = ""
		self.COD = ""
		self.useless_list=["a", "the", "to", "at"]
		self.connectors_list=["in", "on", "with", "under"]
		
		self.verb = ""
		self.connectors = []
		self.CODs = []
		
	
	def IdWords(self):
		"""identify the verb, objects and connectors in the request"""
		#print("DEBUG:", self.chaine)
		self.verb = self.chaine[0]
		i=1
		tmp = []
		while i < len(self.chaine):
			if self.chaine[i] not in self.connectors_list:
				tmp.append(self.chaine[i])
			else:
				self.CODs.append(tmp)
				self.connectors.append(self.chaine[i])
				tmp = []
			i+=1
		if tmp != []:
			self.CODs.append(tmp)
		for i, cod in enumerate(self.CODs):
			tmp = ""
			for j, w in enumerate(cod):
				tmp += w + " " 
			self.CODs[i] = tmp.strip()
		
		
	
	def Verify(self):

##VERIFY IF VERB EXIST. IF YES, TAKE THE DEFAULT WRITING (e.g: l -> look)
		verified = False
		error=""
		i=0
		while i < len(VERBS) and verified is False:
			if self.verb in VERBS[i].names:
				verified = True
				self.verb = VERBS[i]
			i+=1
		for d in DIRECTIONS_LIST: #if verb is a direction -> verb = go, cod=direction
			if self.verb in d:
				verified = True
				self.CODs.append(d[0])
				self.verb = Verb(["go", "g"], 1)
				
		if verified is False:
			error="verb doesn't exist"
			return (verified, error)	
		
		if self.verb == "inventory" and len(self.CODs) == 0 and len(self.connectors) == 0:
			return True, ""
		
## VERIFY IF DIRECTION EXIST, IF YES TAKE THE DEFAULT WRITING (e.g: n -> north)
		if self.verb == "go":
			if len(self.CODs) == 0:
				return False, "No direction"
			verified = False
			if len(self.CODs) == 1:
				for i, d in enumerate(DIRECTIONS_LIST):
					if self.CODs[0] in d and d[0] in PERSO.room.exits_position :
						verified = True
						self.CODs[0] = d[0]
						
				if verified is False:
					error="direction doesn't exist"
					return verified, error
				ex = PERSO.room.GetExitFromDirection(self.CODs[0])
				if(ex.state == "closed"):
					verified = False
					for k in ex.keys:
						if(k in PERSO.inventory):
							verified = True
							PERSO.room.GetExitFromDirection(self.CODs[0]).SetState("open")
							print("You unlock this exit ({0}) with a key ({1})!".format(ex.name, k.name))
							break
				if verified is False:
					return verified, "Exit is closed and you don't have a key..."
				
				return True, ""
				
##VERIFY THERE IS THE GOOD NUMBER OF CODs FOR THE VERB
		if len(self.CODs) not in self.verb.nb_obj:
			return False, "Wrong number of CODs for this verb, expected: " + str(self.verb.nb_obj) + ", received: " + str(len(self.CODs))
				
				
## VERIFY IF LOOK IS USED WITHOUT COD
		if self.verb.name == "look" and len(self.CODs) == 0:
			self.CODs.append(PERSO.room)

		
		if len(self.CODs) > 0:
			
## VERIFY IF ALL OBJECTS ARE REACHABLE
			for i, cod in enumerate(self.CODs):
				if(cod != ""):
					place = self.FindReachableObject(cod)
					#print("PLACE:", place)
					if place is not False:
						if type(place) == type(str()) and place == PERSO.room.name:
							self.CODs[i] = ROOMD[PERSO.room.name]
						else:
							#print(place.inventory)
							for j, obj in enumerate(place.inventory):
								if cod == obj:
									self.CODs[i] = place.inventory[j]
									#print("CODs[i]", self.CODs[i])
					else:
						return False, "Object not reachable"
					
					if self.CODs[i].state == "hidden":
						return False, "Object reachable but hidden. You little cheater!"
			
			#print("CODs:", self.CODs)
			
## VERIFY IF ALL OBJECTS (CODs) EXIST AS OBJECTS OR ROOMS, IF YES: TAKE THE DEFAULT WRITING (e.g: l -> look)
			#verified = False
			#for i, cod in enumerate(self.CODs):
				#for k in OBJD.keys():
					#if cod in OBJD[k].names:
						#verified = True
						#self.CODs[i] = OBJD[k]
						#break
				#if cod == "room":
					#verified = True
					#self.CODs[i] = PERSO.room
				#else:
					#for k in ROOMD.keys():
						#if cod in ROOMD[k].names:
							#verified = True
							#self.CODs[i] = ROOMD[k]
							#break
			#if verified is False:
				#return False, "COD neither room nor object"



##################################################################################################################################
###			FROM NOW ON, self.CODs[i] IS THE OF Object TYPE, NOT STRING, EXCEPT IF THERE IS A HOLE BEFORE A CONNECTOR
##################################################################################################################################


## VERIFY IF COD IS IN THE RIGHT PLACE TO BE USED (e.g. : "IN_ROOM" FOR "TAKE", OR "IN_INVENTORY" FOR "DROP")
			if self.verb.pos_obj_condition == "not_in_inventory" and self.CODs[0].name in PERSO.inventory:
				return False, "Object is already in your inventory"
			elif self.verb.pos_obj_condition == "in_inventory" and self.CODs[0].name not in PERSO.inventory:
				return False, "Object is not in your inventory (maybe in the room)"
			

## NO CONNECTORS: VERIFY IF THE ACTION ON THE COD IS ALLOWED
			if len(self.connectors) == 0:   #i.e 1 verb and 0 or 1 COD
				#print(self.verb)
				if len(self.CODs) not in self.verb.nb_obj:
					return False, "Invalid number of COD"
				if self.verb != "look" and len(self.CODs) == 1 and self.CODs[0].AllowAction(self.verb.name) is False:
					verified = False
					error = "Verb not allowed on object"
					return (verified, error)

			
			if len(self.connectors) > 0:
## VERIFY IF CONNECTORS EXIST
				for i, con in enumerate(self.connectors):
					if con not in self.connectors_list:
						return (False, "Connector " + con + " do not exist in my language")

## VERIFY IF THERE IS SOMETING TO CONNECT
				if len(self.connectors) > 0 and len(self.CODs) == 0:
					return False, "connectors miss cod"

## MAX NUMBER OF CONNECTORS == 1:
				if len(self.connectors) > 1:
					return False, "Too complicated for me (nb connectors > 1)"

## VERIFY THAT THERE IS EXACTLY TWO COD TO CONNECT
				if len(self.CODs) != 2:
					return False, "I want EXACTLY two 2 cod for the moment"

## VERIFY THAT THE 2 OBJECTS ARE DIFFERENT
				if self.CODs[0] == self.CODs[1]:
					return False, "Cannot connect an object with itself"

## VERIFY IF THE INDIRECT OBJ (the 2nd one) ACCEPT THE CONNECTOR:
				if self.connectors[0] not in self.CODs[1].connectors:
					return False, "Indirect object does not accept this connector"



		return (verified, error)

	def Repondre(self):
		
		self.Simplify()
		if len(self.chaine) == 0:
			return "This is not a complete statement!"
		self.IdWords()
		reponse = ""
		verified, error = self.Verify()
		reponse = error
		#print("Verified?", verified, "Error:", error)
		#print("Verb:", self.verb, "\nCODs:", self.CODs, "\nConnectors:", self.connectors)
		if verified:
			
			if self.verb.name == "look":
				#if self.CODs[0].name in OBJD.keys():
					#reponse = OBJD[self.CODs[0].name].Describe()
				#else:
					#reponse = PERSO.room.Describe()
				if len(self.CODs) < 2:
					reponse = self.CODs[0].Describe(self.connectors)
				else:
					reponse = self.CODs[1].Describe(self.connectors)
				
				
			elif self.verb == "inventory":
				reponse = PERSO.PrintInventory()
							
			elif self.verb.name == "go":
				#print("DEBUG GO ", self.CODs)
				used_exit = PERSO.room.GetExitFromDirection(self.CODs[0])
				PERSO.Move(used_exit)
			
			#elif self.verb.name == "use":
				#reponse = "You use "+ self.CODs[0].name
			
			elif self.verb.name == "take":
				print(self.FindReachableObject(self.CODs[0]))
				self.FindReachableObject(self.CODs[0]).Drop(self.CODs[0].name)
				PERSO.inventory.append(self.CODs[0])
				reponse = "You take " + self.CODs[0].name
			
			elif self.verb.name == "drop":
				PERSO.Drop(self.CODs[0].name)
				ROOMD[PERSO.room.name].inventory.append(self.CODs[0])
				reponse = "You drop " + self.CODs[0].name
			
			elif self.verb.name == "help":
				reponse = "I know it is not always easy to know what your next move should be, especially when you are in the dark.\nBut one good thing you can always do is LOOK around you. That way you'll have some idea about what could be of USE, or where to GO."
				
			elif self.verb.name == "break":
				print("BREAK ;)")
                            
			elif self.verb.name == "put":
				self.FindReachableObject(self.CODs[0]).Drop(self.CODs[0])
				self.CODs[1].inventory.append(self.CODs[0])
			
			
			else:
				reponse = "I understood everything but I suck."
		
		return reponse	
	
	
	def FindReachableObject(self, obj):
		if obj == PERSO.room or obj == "room":
			return PERSO.room.name

		elif obj in PERSO.room.inventory:
			return ROOMD[PERSO.room.name]
		
		elif obj in PERSO.inventory:
			return PERSO
		
		else:
			for i, o in enumerate(PERSO.inventory):
				if obj in o.inventory:
					return PERSO.inventory[i]
			for i, o in enumerate(ROOMD[PERSO.room.name].inventory):
				if obj in o.inventory:
					return ROOMD[PERSO.room.name].inventory[i]
		
		return False
	
	
	def Simplify(self):
		to_del = []
		for i, m in enumerate(self.chaine):
			if m in self.useless_list:
				to_del.append(i)
		for i, d in enumerate(to_del):
			del self.chaine[d-i]
	
	def Chercher(self, *mots):
		existe = -1
		for m in mots:
			for i, a in enumerate(self.chaine):
				if m == a:
					existe = i
					break
			if existe != -1:
				break
		return existe

		
	def get_COD(self):
		"""From a list of word already simplified, get the object of interest e.g: ['look' 'rusted' 'knife'] -> "rusted knife"""
		COD = ""
		for i, m in enumerate(self.chaine[1:]):
			COD += m
			if i+2 != len(self.chaine):
				COD += " "
		return COD
