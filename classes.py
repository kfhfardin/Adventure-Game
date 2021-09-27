# Dr. McCartin-Lim's Adventure Game Engine 0.75
#Updated by Fardin for his game

import textwrap
from helperfunctions import *

# Global list of every "Thing" in the game
everyThingInGame = []

# Base class Thing (all objects in the game inherit this)
class Thing:
            
    def __init__(self, name, article="a"):
        global everyThingInGame
        self.name = name
        self.article = article
        self.aliases = []
        self.description = ""
        self.interactable = True #if this were set to False, then the player can't interact with it
        self.explicitMention = True #if this were set to False, then it won't be explicitly mentioned
        everyThingInGame.append(self)
    
    def __str__(self):
        if self.article != "":
            return self.article + " " + self.name
        else:
            # Proper noun
            return self.name
    
    def examine(self):
        if self.description != "":
            print(self.description)
        else:
            if self.article != "":
                print("There is nothing notable about the "+self.name+".")
            else:
                # Proper nouns don't have an article
                print("There is nothing notable about "+self.name+".")

    
# Class for a Thing that can contain other Things        
class Container(Thing):
    
    def __init__(self, name, article="a"):
        super().__init__(name,article)
        self.contents = []
    
    # Returns a list of objects in contents that match both stringToMatch and typeToMatch and are interactible
    # When stringToMatch is the empty string, we return all objects that match the typeToMatch
    def checkFor(self,stringToMatch,typeToMatch):
        
        #Strip out article from stringToMatch if it begins with an article
        if stringToMatch.startswith("the "):
            stringToMatch = stringToMatch.split("the ")[1]
        elif stringToMatch.startswith("a "):
            stringToMatch = stringToMatch.split("a ")[1]
        elif stringToMatch.startswith("an "):
            stringToMatch = stringToMatch.split("an ")[1]
            
        #Now, search contents for matches and add to listToReturn
        listToReturn = []
        for obj in self.contents:
            if isinstance(obj, typeToMatch) and obj.interactable:
                if stringToMatch == obj.name.lower() or stringToMatch in obj.aliases or stringToMatch=="":
                    listToReturn.append(obj)
                    
        #Return the list (if nothing found, empty list is returned)
        return listToReturn



# Class for Locations in the game        
class Location(Container):
    # These instance variables define locations you can move to from this location
    north = None
    south = None
    east = None
    west = None

    # We change this instance variable to True after the location has been visited at least once
    visitedOnce = False

    # Display description of room
    def displayDescription(self,verbose=False):
        print(self.name.upper())

        # If this is the first time visiting this location or verbose is True, print the full description
        if self.visitedOnce == False or verbose==True:
            print(self.description)

        # Print the list of everything in this location that should be explicitly mentioned
        explicitList = []
        for item in self.contents:
            if item.explicitMention:
                explicitList.append(item)
        if len(explicitList) > 0:
            print("")
            print("You see " + stringFromList(explicitList) + " here.")

        # Print the directions you can travel from here
        print("")
        dirList = []
        if self.north!=None: dirList.append("North")
        if self.south!=None: dirList.append("South")
        if self.east!=None: dirList.append("East")
        if self.west!=None: dirList.append("West")
        if (len(dirList) > 0):
            print("DIRECTIONS AVAILABLE: ",stringFromList(dirList))
        else:
            print("DIRECTIONS AVAILABLE: ","None")

    # Return True if we successfully enter the location
    def enter(self):
        self.displayDescription()
        self.visitedOnce = True
        return True

    def setNorth(self,location):
        self.north = location
        location.south = self

    def setSouth(self,location):
        self.south = location
        location.north = self

    def setEast(self,location):
        self.east = location
        location.west = self

    def setWest(self,location):
        self.west = location
        location.east = self
        
    def movePlayerTo(self,newlocation):
        global player
        if(newlocation != None):
            #We only update the player's current location if we
            #successfully entered newlocation. If not the enter()
            #method will give the player some kind of error message.
            if(newlocation.enter()):
                player.currentLocation = newlocation
        else:
            print("Sorry, you can't go that way.")        
        

class Portable(Thing):
    # Return True if successful
    def get(self):
        global player
        if self in player.currentLocation.contents:
            player.currentLocation.contents.remove(self)
            player.contents.append(self)
            print("You pick up "+str(self)+".")
            #Once a Portable is picked up it becomes explicitly mentioned, if it wasn't earlier
            self.explicitMention = True
            return True
        else:
            # This else condition should never happen
            # since the parser looks for the object
            # before its get method is called
            print("But it is not here.")
            return False
        
    # Return True if successful
    def drop(self):
        global player
        if self in player.contents:
            player.contents.remove(self)
            player.currentLocation.contents.append(self)
            print("You drop "+str(self)+".")
            return True
        else:
            # This else condition should never happen
            # since the parser looks for the object
            # before its drop method is called            
            print("But you do not have it.")
            return False

# This class represents things that can be read
class Readable(Thing):
    def read(self):
        self.examine()

# This class represents things that can be used
class Usable(Thing):
    # Default message when attempting to use it. Override this in the game
    def use(self):
        print("But there does not seem to be any particularly good reason to use the "+self.name+" at the moment.")
        return False

# This class inherits from both Portable and Usable
class UsablePortable(Portable,Usable):
    pass

# This class represents Non-Player Characters
class NPC(Thing):
    # We can try to give items to the NPC, but by default they are rejected
    def give(self,item):
        print(str(self) + " does not want the " + item.name+".")
    def praise(self):
        print("You have praise")
    def debate(self):
        print("Please Debate")
    def manipulate(self):
        print("You are devious")
    def fight(self):
        print("You are devious")

# Class to represent the player
class Player(Container):
    
    def __init__(self):
        self.name = "player"
        self.article = "the"
        self.aliases = ["me","myself","self"]
        self.description = "You are but one of many brave players to try to beat this game."
        self.explicitMention = False
        self.score = 0
        self.currentLocation = None
    
    def __str__(self):
        return "yourself"

    def increaseScore(self, amount):
        print("")
        print("YOUR SCORE HAS GONE UP BY "+str(amount)+" POINTS!")
        self.score += amount    

#Global player object
player = Player()