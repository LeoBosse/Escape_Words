#!/usr/bin/python3
# -*-coding:utf-8 -*


from header import *

class Exits:
	def __init__(self, names, description, direction, destination, state = "open", keys = []):
		self.names = names
		self.name = self.names[0]
		self.description = description
		self.direction = direction
		self.destination = destination
		self.state = state #"open", "closed".  ###Not implemented "0to1" ("1to0"): open only in direction self.rooms[0 (1)] to direction self.rooms[1 (0)]
		self.keys = keys
	
	def SetState(self, new_state):
		if(new_state in ["open", "closed"]):
			self.state = new_state
	
	def TestKey(self, key):
		"""Test if a key (type Objet()) can open the exit. If yes, adapt the exit state. Return:-1=already opened, False:wrong key, still closed, True:Good key! opened"""
		if(self.state == "open"):
			return -1
		elif(key in self.keys):
			self.SetState("open")
			return True
		else:
			return False
