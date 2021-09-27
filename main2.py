# Dr. McCartin-Lim's Adventure Game Engine 0.75
#Updated by Fardin for his game


from classes import *
from helperfunctions  import *
from commandparser import *

# Here's the data for our game
from gamedata import *

#Play game
player.contents= [clue1,ivorydress]
player.currentLocation = musuem_entrance
musuem_entrance.enter()
while(True):
    for thing in everyThingInGame:
        if hasattr(thing,"updateEveryTurn"):
            thing.updateEveryTurn()
    command = input("> ")
    print("")
    parseCommand(command)
