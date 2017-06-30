#!/usr/bin/python3
# -*- coding: utf-8 -*-

from header import *

class Objet:
	def __init__(self, names, description, actions_list = [], obj_use_with=[], obj_to_combine=[], state = 0, connectors = [], description_connectors = "", inventory = []):
		
		self.names=names
		self.name=names[0]
		self.description = description
		self.description_connectors = description_connectors
		self.aide = "No help available right now..."
		self.actions_list = actions_list
		self.use_with = obj_use_with
		self.combine_with = obj_to_combine
		self.state = state
		self.connectors = connectors
		self.inventory = inventory
	
	def Describe(self, connectors = []):
		if connectors == []:
			d_str = self.description + "\n"
			if len(self.inventory) != 0:
				for i, obj in enumerate(self.inventory):
					d_str_inv = ""
					if obj.state != "hidden":
						d_str_inv += "\ta " + obj.name + "\n"
				if d_str_inv != "":
					d_str += "You can also see :\n" + d_str_inv
		
		else:
			for c in connectors:
				if c in self.connectors:
					d_str = self.description_connectors + "\n"
					if len(self.inventory) != 0:
						d_str += "You can also see :\n"
						for i, obj in enumerate(self.inventory):
							self.inventory[i].state = 0
							d_str += "\ta " + obj.name + "\n"
					
		return d_str
	
	
	def Drop(self, obj_name):
		for i, o in enumerate(self.inventory):
			if(obj_name == o):
				del self.inventory[i]
				return True
		return False

	
	
	
	def __repr__(self):
		return "Object \"objet\": " + self.name

	
	def AllowAction(self, action):
		return (action in self.actions_list)
	
	def __eq__(self, string):
		#print("obj==")
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
