#!/usr/bin/python3
# -*- coding: utf-8 -*-

from header import *
		
class Verb:
	
	def __init__(self, names, nb_obj, pos_obj_condition = "reachable"):
		self.names = names
		self.name = self.names[0]
		self.nb_obj = nb_obj
		self.pos_obj_condition = pos_obj_condition
		#self.function = fct
	
	#def Do(self, *args):
		#self.function(args)
	
	def __repr__(self):
		return "Object \"verb\": " + self.name

	def __eq__(self, string):
		#print("verb==")
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
