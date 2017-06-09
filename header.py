#!/usr/bin/python3
# -*- coding: utf-8 -*-


#########################################################################################################################
#																														#
#		INIT ENVIRONMENT MODULE AND CREATE IT																			#
#																														#
#########################################################################################################################


#from room import *
#from objects import *
#from verbs import *
from environment.room import *
from environment.objects import *
from environment.verbs import *
from environment.exits import *


OBJD = {	
	"lamp"		:	Objet(	["lamp"],
							"It is a oil lamp.",
							actions_list = ["take", "drop", "break"]
						),
	"cell key"		:	Objet(	["cell key"],
							"It is the key from your cell. You are free!",
							actions_list = ["take", "drop"]
						),
							
	"knife"		:	Objet(	["knife"],
							"It is a basic knife.",
							actions_list = ["take", "drop", "cut"]
						),
							
	"mirror"	:	Objet(	["mirror"],
							"You see yourself in the mirror. You don't look so good...",
							actions_list = ["break", "take", "drop"],
							state = -1
						),
	"bed"		:	Objet(	["bed"],
							"You see a large bed, seems very confortable"
						),
	"broom"		:	Objet(	["broom"],
							"An old broom with a long wooden pole and a few straw still attached to it.",
							actions_list = ["take", "drop"]
						),
	
	"treasure"	:	Objet(	["treasure"],
							"A big pile of gold, gems, perls and everything you could imagine to be in a treasue pile.",
							actions_list = ["take", "drop"]
							
						)
						
}

########################################################################################################################
########################################################################################################################


ROOMD = {
	"roof"		:	Room(	["roof"],
							0,
							exits = [	Exits(["drop"], "a risky fall", "east", "balcon 1"),
							
										Exits(["drop"], "a risky fall", "west", "balcon 2"),
										Exits(["tower"],"a risky climb back to your cell", "up", "cell")],
							inventory = [],
							description = "You are on the roof. Be careful not to fall!",
							first_auto_view = "What a beautiful view. You see th gardens and the forest all the way to the town."
						),
	
#*******************************************************************************************************#						
	"cell"		:	Room(	["cell"],
							0,
							exits = [	Exits( ["door"],"the only door of the room", "north", "stairs", state = "closed", keys=[OBJD["cell key"]]), 
										Exits( ["window", "small window"], "a small window", "east", "roof")],
							inventory = ["mirror", "bed"],
							description = "You see a cell.",
							first_auto_view = "It is your well known cell"
						),
							
	"stairs"	:	Room(	["stairs"],
							1,
							exits = [	Exits( ["door"],"upper door", "up", "cell", state = "closed", keys=[OBJD["cell key"]]), 
										Exits(["corridor"], "corridor", "down", "corridor")],
							inventory = [],
							description = "Normal stairs",
							first_auto_view = "You step unpon a normal stair."
						),
	"grenier"	:	Room(	["grenier"],
							1,
							exits = [	Exits(["trap"], "a trap in the floor", "down", "corridor")],
							inventory = [],
							description = "Normal stairs",
							first_auto_view = "You step unpon a normal stair."
						),
						
						
#*******************************************************************************************************#
	"corridor"	:	Room(	["corridor"],
							2,
							exits = [	Exits(["shiny door"], "a nice painted door that let some light pass under it", "east", "bedroom 1"), 
										Exits(["painted door"], "a nice painted door with a big lock screwed to it", "west", "bedroom 2"), 
										Exits(["stairway"], "a stairway going straight to a big room", "north", "hall"),
										Exits(["cell stairs", "normal stairs"], "a stairway going straight back to your cell", "south", "stairs"),
										Exits(["trap"], "a trap in the ceiling", "up", "grenier")],
							inventory = ["broom"],
							description = "A small corridor opens in front of you. There is nothiing special about this place.",
							first_auto_view = "A small corridor opens up before you."
						),
	"bedroom 1"	:	Room(	["bedroom 1"],
							3,
							exits = [	Exits(["painted door"], "a nice painted door", "west", "corridor")],
							inventory = ["bed"],
							description = "You see a big bedroom",
							first_auto_view = "You enter a big bedroom, well furnished and letting the sun enter by its broken window."
						),
	
	"balcon 1"	:	Room(	["balcon 1"],
							4,
							exits = [	Exits(["door", "glass door"], "a big glass door", "west", "bedroom 1")],
							inventory = [],
							description = "It is a large balcony giving on the front court. You see a well and the front door.",
							first_auto_view = "What a pleasant space to have breakfast watching the rising sun."
						),

	
	"bedroom 2"	:	Room(	["bedroom 2"],
							4,
							exits = [	Exits(["painted door", "door"], "a nice painted door", "east", "corridor"),
										Exits(["glass door", "door"], "a big glass door", "west", "balcon 2")],
							inventory = ["bed"],
							description = "You see a big bedroom",
							first_auto_view = "You enter a big bedroom, well furnished."
						),
						
	"balcon 2"	:	Room(	["balcon 2"],
							4,
							exits = [	Exits(["wooden door", "door"], "an old wooden door", "south", "corridor")],
							inventory = [],
							description = "It is a large balcony giving on the back court. You see a garden and what seems to be a tool shed.",
							first_auto_view = "What a pleasant space to spend the long summer evenings."
						),
	
	"bedroom 3"	:	Room(	["bedroom 3"],
							4,
							exits = [	Exits(["glass door", "door"], "a big glass door","east", "bedroom 2")],
							inventory = [],
							description = "You are in a small bedroom that could have been for a servant.",
							first_auto_view = "What a small bedroom. You could not live here comfortably."
						),
#*******************************************************************************************************#	
	"hall"	:	Room(	["hall"],
							5,
							exits = [	Exits(["straight stair", "stair"], "a straight stair going up to the first floor", "up", "corridor"), 
										Exits(["big door", "strong door", "door"], "a very big door, reinforced with iron nails a pikes", "east", "court"),
										Exits(["broken door", "door"], "a broken door", "south", "living room"),
										Exits(["door"], "a door", "west", "eating room")],
							inventory = ["treasor"],
							description = "You see what seem to be the hallway of the castle. But it is filled with gold and gems.",
							first_auto_view = "A yellow light hits you in the eyes and you are blind for a couple of second. When you recover your sight, it is to discover a huge treasure of gold and gems, illuminated by a the sun coming in via a ig broken door."
						),
	
	"eating room"	:	Room(	["eating room"],
							5,
							exits = [	Exits(["opening", "hole"], "an opening in the wall", "south", "kitchen"), 
										Exits(["door"], "a door", "east", "hall")],
							inventory = [""],
							description = "You see a long table in the center of the room, certainly to receive big banquet.",
							first_auto_view = "What a nice table!"
						),
	
	
	"kitchen"	:	Room(	["kitchen"],
							7,
							exits = [	Exits(["opening", "hole"], "an opening in the wall", "north", "eating room"),
										Exits(["small door", "door"], "a small door", "east", "living room"),
										Exits(["big door"], "a big door to let the food come in", "west", "back court"),
										Exits(["trap"], "a trap in the floor", "down", "basements")],
							inventory = ["knife"],
							description = "There is a whole bunch of cooking equipment",
							first_auto_view = "You enter in a fully equiped kitchen."
						),

	"living room"	:	Room(	["living room"],
							7,
							exits = [	Exits(["broken door", "door"], "a broken door", "north", "hall"),
										Exits(["small door"], "a small door", "west", "kitchen")],
							inventory = ["knife"],
							description = "You see some comfortable sofa and chairs, a chess table, big windiw to enjoy the summer.",
							first_auto_view = "You enter what appears to be the living room."
						),
	
	
	"front court"	:	Room(	["front court"],
							6,
							exits = [	Exits(["big door"], "a very big door, reinforced with iron nails a pikes", "west", "hall"),
										Exits(["opening"], "an opening in the plants", "east", "garden")],
							inventory = [],
							description = "You are in the central place of the castle. You see the tower of your cell behind you and an old castle.",
							first_auto_view = "You're outside!"
						),
	
	"back court"	:	Room(	["back court"],
							6,
							exits = [	Exits(["big door"], "a big door", "east", "kitchen"),
										Exits(["opening"], "an opening in the plants", "west", "garden")],
							inventory = [],
							description = "You are in the central place of the castle. You see the tower of your cell behind you and an old castle.",
							first_auto_view = "You're outside!"
						),
#*******************************************************************************************************#						
							
	"basements"	:	Room(	["basements"],
							6,
							exits = [	Exits(["trap"], "a trap in the ceiling", "up", "kitchen")],
							inventory = [],
							description = "You are in the basements of the castle",
							first_auto_view = "What a dark place"
						)
							
#*******************************************************************************************************#						
							
							
							
											
	#"name"	:	Room(	"name",
							#number,
							#exits = {"DIRECTION":("name of direction", "description")},
							#inventory = ["name of object"],
							#description = Description printed when looking at the room,
							#first_auto_view = First message to show when entering a room for the first time
						#)
					
					
}

	


########################################################################################################################
########################################################################################################################




DIRECTIONS_LIST = 	[
						["up", "u"],
						["down", "d"],
						["north", "n"],
						["south", "s"],
						["east", "e"],
						["west", "w"],
						["northeast", "ne"],
						["northwest", "nw"],
						["southeast", "se"],
						["southwest", "sw"]
					]

########################################################################################################################
########################################################################################################################



VERBS = [
					Verb(["look", "l"], 			[0,1]),
					Verb(["go", "g"], 				[1]),
					Verb(["take", "t"], 			[1]),
					Verb(["drop", "throw"], 	[1]),
					Verb(["break"], 				[1]),
					Verb(["inventory", "i"], 		[0]),
					Verb(["help", "h"], 			[0])
		]
		
		
		
#########################################################################################################################
#																														#
#		INIT PERSO MODULE AND CREATE PERSO																				#
#																														#
#########################################################################################################################

from perso import *	
PERSO = Perso(ROOMD["cell"], inventory=[OBJD["lamp"], OBJD["cell key"]])




#########################################################################################################################
#																														#
#		INIT RESPONSE MODULE																							#
#																														#
#########################################################################################################################


from response import *
