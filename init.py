##!/usr/bin/python3
## -*- coding: utf-8 -*-

#from header import *
#from room import *

#def InitRooms():
	#roomd = {




	#"roof"		:	Room(	"roof",
							#0,
							#exits = {	"EAST":("balcon 1", "a risky fall"), 
										#"WEST":("balcon 2", "a risky fall"),
										#"UP":("cell", "a risky climb back to your cell")},
							#inventory = [],
							#description = "You are on the roof. Be careful not to fall!",
							#first_auto_view = "What a beautiful view. You see th gardens and the forest all the way to the town."
						#),
	
##*******************************************************************************************************#						
	#"cell"		:	Room(	"cell",
							#0,
							#exits = {	"NORTH":("stairs", "the only door of the room"), 
										#"EAST":("roof", "a small window")},
							#inventory = ["mirror", "bed"],
							#description = "You see a cell.",
							#first_auto_view = "It is your well known cell"
						#),
							
	#"stairs"	:	Room(	"stairs",
							#1,
							#exits = {	"UP":("cell", "upper door"), 
										#"DOWN":("corridor", "corridor")},
							#inventory = [],
							#description = "Normal stairs",
							#first_auto_view = "You step unpon a normal stair."
						#),
	#"grenier"	:	Room(	"grenier",
							#1,
							#exits = {	"DOWN":("corridor", "a trap in the floor")},
							#inventory = [],
							#description = "Normal stairs",
							#first_auto_view = "You step unpon a normal stair."
						#),
						
						
##*******************************************************************************************************#
	#"corridor"	:	Room(	"corridor",
							#2,
							#exits = {	"EAST":("bedroom 1", "a nice painted door that let some light pass under it"), 
										#"WEST":("bedroom 2", "a nice painted door with a big lock screwed to it"), 
										#"NORTH":("hall", "a stairway going straight to a big room"),
										#"UP":("grenier", "a trap in the ceiling")},
							#inventory = ["broom"],
							#description = "A small corridor opens in front of you. There is nothiing special about this place.",
							#first_auto_view = "A small corridor opens up before you."
						#),
	#"bedroom 1"	:	Room(	"bedroom 1",
							#3,
							#exits = {	"WEST":("corridor", "a nice painted door")},
							#inventory = ["bed"],
							#description = "You see a big bedroom",
							#first_auto_view = "You enter a big bedroom, well furnished and letting the sun enter by its broken window."
						#),
	
	#"balcon 1"	:	Room(	"balcon 1",
							#4,
							#exits = {	"WEST":("bedroom 1", "a big glass door")},
							#inventory = [],
							#description = "It is a large balcony giving on the front court. You see a well and the front door.",
							#first_auto_view = "What a pleasant space to have breakfast watching the rising sun."
						#),

	
	#"bedroom 2"	:	Room(	"bedroom 2",
							#4,
							#exits = {	"EAST":("corridor", "a nice painted door"),
										#"WEST":("balcon 2", "a big glass door")},
							#inventory = ["bed"],
							#description = "You see a big bedroom",
							#first_auto_view = "You enter a big bedroom, well furnished."
						#),
						
	#"balcon 2"	:	Room(	"balcon 2",
							#4,
							#exits = {	"SOUTH":("corridor", "an old wooden door")},
							#inventory = [],
							#description = "It is a large balcony giving on the back court. You see a garden and what seems to be a tool shed.",
							#first_auto_view = "What a pleasant space to spend the long summer evenings."
						#),
	
	#"bedroom 3"	:	Room(	"bedroom 3",
							#4,
							#exits = {	"EAST":("bedroom 2", "a big glass door")},
							#inventory = [],
							#description = "You are in a small bedroom that could have been for a servant.",
							#first_auto_view = "What a small bedroom. You could not live here comfortably."
						#),
##*******************************************************************************************************#	
	#"hall"	:	Room(	"hall",
							#5,
							#exits = {	"UP":("corridor", "a straight stair going up to the first floor"), 
										#"EAST":("court", "a very big door, reinforced with iron nails a pikes"),
										#"SOUTH":("living room", "a broken door"),
										#"WEST":("eating room", "a door")},
							#inventory = ["treasor"],
							#description = "You see what seem to be the hallway of the castle. But it is filled with gold and gems.",
							#first_auto_view = "A yellow light hits you in the eyes and you are blind for a couple of second. When you recover your sight, it is to discover a huge treasure of gold and gems, illuminated by a the sun coming in via a ig broken door."
						#),
	
	#"eating room"	:	Room(	"eating room",
							#5,
							#exits = {	"SOUTH":("kitchen", "an opening in the wall"), 
										#"EAST":("hall", "a door")},
							#inventory = [""],
							#description = "You see a long table in the center of the room, certainly to receive big banquet.",
							#first_auto_view = "What a nice table!"
						#),
	
	
	#"kitchen"	:	Room(	"kitchen",
							#7,
							#exits = {	"NORTH":("eating room", "an opening int the wall"),
										#"EAST":("living room", "a small door"),
										#"WEST":("back court", "a big door to let the food come in"),
										#"DOWN":("basements", "a trap in the floor")},
							#inventory = ["knife"],
							#description = "There is a whole bunch of cooking equipment",
							#first_auto_view = "You enter in a fully equiped kitchen."
						#),

	#"living room"	:	Room(	"living room",
							#7,
							#exits = {	"NORTH":("hall", "a broken door"),
										#"WEST":("kitchen", "a small door")},
							#inventory = ["knife"],
							#description = "You see some comfortable sofa and chairs, a chess table, big windiw to enjoy the summer.",
							#first_auto_view = "You enter what appears to be the living room."
						#),
	
	
	#"front court"	:	Room(	"front court",
							#6,
							#exits = {	"WEST":("hall", "a very big door, reinforced with iron nails a pikes"),
										#"EAST":("garden", "an opening in the plants")},
							#inventory = [],
							#description = "You are in the central place of the castle. You see the tower of your cell behind you and an old castle.",
							#first_auto_view = "You're outside!"
						#),
	
	#"back court"	:	Room(	"back court",
							#6,
							#exits = {	"EAST":("kitchen", "a big door"),
										#"WEST":("garden", "an opening in the plants")},
							#inventory = [],
							#description = "You are in the central place of the castle. You see the tower of your cell behind you and an old castle.",
							#first_auto_view = "You're outside!"
						#),
##*******************************************************************************************************#						
							
	#"basements"	:	Room(	"basements",
							#6,
							#exits = {	"UP":("kitchen", "a trap in the ceiling")},
							#inventory = [],
							#description = "You are in the basements of the castle",
							#first_auto_view = "What a dark place"
						#)
							
##*******************************************************************************************************#						
							
							
							
											
	##"name"	:	Room(	"name",
							##number,
							##exits = {"DIRECTION":("name of direction", "description")},
							##inventory = ["name of object"],
							##description = Description printed when looking at the room,
							##first_auto_view = First message to show when entering a room for the first time
						##)
					
					
#}

	
	#return roomd


#########################################################################################################################
##----------------------------------------------------------------------------------------------------------------------#
#########################################################################################################################



#def InitObjects():
	#objd = {	
	#"knife"		:	Objet(	"knife",
							#"It is a basic knife.",
							#["take", "cut"]
						#),
							
	#"mirror"	:	Objet(	"mirror",
							#"You see yourself in the mirror. You don't look so good...",
							#["break"]
						#),
	#"broom"	:		Objet(	"broom",
							#"An old broom with a long wooden pole and a few straw still attached to it.",
							#["take"]
						#),
	
	#"treasure"	:	Objet(	"treasure",
							#"A big pile of gold, gems, perls and everything you could imagine to be in a treasue pile.",
							#["take"]
							
						#)
						
#}
	#return objd

#########################################################################################################################
##----------------------------------------------------------------------------------------------------------------------#
#########################################################################################################################

#def InitDirections():
	#directions_list = [
					#["up", "u"],
					#["down", "d"],
					#["north", "n"],
					#["south", "s"],
					#["east", "e"],
					#["west", "w"],
					#["northeast", "ne"],
					#["northwest", "nw"],
					#["southeast", "se"],
					#["southwest", "sw"]
					#]
	#return directions_list

#########################################################################################################################
##----------------------------------------------------------------------------------------------------------------------#
#########################################################################################################################



#def InitVerbs():
	#verbs_list = [
					#Verb(["look", "l"],
							#(0,1)),
					#Verb(["up", "u"],
							#0),
					#Verb(["down", "d"],
							#0),
					#Verb(["north", "n"],
							#0),
					#Verb(["south", "s"],
							#0),
					#Verb(["east", "e"],
							#0),
					#Verb(["west", "w"],
							#0),
					#Verb(["go", "g"],
							#1),
					#Verb(["take", "t"],
							#1)
					
	
	
	
					#]
	
	#return verbs_list
	

