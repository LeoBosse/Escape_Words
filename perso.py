#!/usr/bin/python3
# -*- coding: utf-8 -*-

from header import *

class Perso:
	
	def __init__(self, room, inventory=[]):
		self.room = room
		self.old_room = room
		self.inventory = inventory

	def Move(self, used_exit):
		self.old_room = self.room
		new_room = ROOMD[used_exit.destination] 
		self.old_room.Exit(used_exit)
		new_room.Enter()	
		self.room = new_room	
	
	def PrintInventory(self):
		
		rep = "Your inventory is made of:\n"
		for i in self.inventory:
			rep += "\t"+i.name+"\n"
		return rep

		
	def Drop(self, obj_name):
		for i, o in enumerate(self.inventory):
			if(obj_name == o.name):
				del self.inventory[i]
				return True
		return False


	def __repr__(self):
		return "Object \"Perso\""
