#!/usr/bin/python3
# -*- coding: utf-8 -*-

from header import *

class Objet:
	def __init__(self, names, description, actions_list = [], obj_use_with=[], obj_to_combine=[], state = 0):
		
		self.names=names
		self.name=names[0]
		self.description = description
		self.aide = "No help available right now..."
		self.actions_list = actions_list
		self.use_with = obj_use_with
		self.combine_with = obj_to_combine
		self.state = 0
		
	def __repr__(self):
		return "Object \"objet\" " + self.name

	
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
