#!/usr/bin/python3
# -*- coding: utf-8 -*-

from header import *

class Room:
	def __init__(self, names, number, description, first_auto_view, exits={}, inventory=[]):
		
		self.names= names
		self.name = names[0]
		self.ID = number
		self.known = False
		self.inventory = inventory
		self.exits = exits
		self.exits_position = []
		for ex in self.exits:
			self.exits_position.append(ex.direction)
		self.aide = "No help available right now..."

		self.description = description
		self.first_view = first_auto_view
		
		self.connectors = ["in"]
		self.state = 0

	def Enter(self):
		if self.known:
			print("You enter the ", self.name)
		else:
			print(self.first_view)
			self.known=True

	def Exit(self, used_exit):
		print("You exit the " + self.name + " via " + used_exit.name + "." + " (" + used_exit.direction + ")")
		
	def Describe(self, connectors = []):
		d_str = self.description + "\n"
		d_str += "You see the following exit(s):\n"
		for ex in self.exits:
			d_str += "\t" + ex.description + " (" + ex.direction + ")\n"
		
		if len(self.inventory) != 0	:
			d_str += "You can also see different objects laying around:\n"
			for i, obj in enumerate(self.inventory):
				if obj.state != "hidden":
					d_str += "\ta " + obj.name + "\n"
		return d_str

	def GetExitFromDirection(self, direction_str):
		"""Return the exit corresponding to "direction_str" in the self.exits list. Return -1 if the exit doesn't exists"""
		e = -1
		for i, ex in enumerate(self.exits):
			if(ex.direction == direction_str):
				e = self.exits[i]
				break
		return e


	def Drop(self, obj_name):
		for i, o in enumerate(self.inventory):
			if(obj_name == o):
				del self.inventory[i]
				return True
		return False



	def __repr__(self):
		return "Object \"room\": " + self.name
	
	def __eq__(self, string):
		if type(string) is type(str()):
			return string in self.names
		elif type(string) is type(self):
			return string.name == self.name
		else:
			return False
	def __ne__(self, string):
		if type(string) is type(str()):
			return string not in self.names
		elif type(string) is type(self):
			return string.name != self.name
		else:
			return True

