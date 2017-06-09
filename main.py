#!/usr/bin/python3
# -*- coding: utf-8 -*-

from header import *

continuer=1

history = []

print("\n\t You don't know where you are...\n\t Seems like your are layed down in a some kind of very confortable bed... But what a headache!\n\t What did you do yesterday? You wish you could get some HELP...\n")

while continuer:
	
	action = Action(input())
	#history.append(action)
	if action.difficulty != 0:
		print(action.Repondre(), "\n")

	if action == "stop":
		continuer = 0




