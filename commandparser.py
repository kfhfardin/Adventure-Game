# Fardin's Adventure Game Engine 0.75(with help from Dr. Mc-Cartin Lim

from classes import *
from helperfunctions import *

# Here's the data for our game
from gamedata import *

def parseCommand(command):
    global player
    # Convert command to lowercase
    command = command.lower()
    
    # Check each verb
    if command == "look":
        # Print a verbose description of the player's current location
        player.currentLocation.displayDescription(True)

    elif command == "quit":
        #Exit the game
        exit()

    elif command == "score":
        #Print the player's current score
        print("Your current score is now "+str(player.score)+ " points.")
    
    elif command == "inventory" or command == "inv" or command == "i":
        if len(player.contents) == 0:
            print("You are not carrying anything!")
        else:
            print("You have "+stringFromList(player.contents)+".")
        
    elif command == "north" or command == "n":
        player.currentLocation.movePlayerTo(player.currentLocation.north)
            
    elif command == "south" or command == "s":
        player.currentLocation.movePlayerTo(player.currentLocation.south)
            
    elif command == "east" or command == "e":
        player.currentLocation.movePlayerTo(player.currentLocation.east)
            
    elif command == "west" or command == "w":
        player.currentLocation.movePlayerTo(player.currentLocation.west) 
        
    elif command.startswith("examine "):
        objToLookat = command.split("examine ")[1]
        # Search both the current location and the player's inventory
        matches = player.currentLocation.checkFor(objToLookat,Thing) + player.checkFor(objToLookat,Thing)
        # We found an exact match
        if len(matches) == 1:
            matches[0].examine()
        # There are multiple matches, so it's ambiguous what the player is referencing
        elif len(matches) > 1:
            print("Are you talking about " + stringFromList(matches,"or") + "?")
        # We found no matches
        else:
            print("I do not know what you are referring to.")    

    elif command.startswith("read "):
        objToLookat = command.split("read ")[1]
        # Search both the current location and the player's inventory
        matches = player.currentLocation.checkFor(objToLookat,Readable) + player.checkFor(objToLookat,Readable)
        badmatches = player.currentLocation.checkFor(objToLookat,Thing) + player.checkFor(objToLookat,Thing)
        # We found an exact match
        if len(matches) == 1:
            matches[0].read()
        # There are multiple matches, so it's ambiguous what the player is referencing
        elif len(matches) > 1:
            print("Are you talking about " + stringFromList(matches,"or") + "?")
        # Player may be referring to a Thing that is not Readable
        elif len(badmatches) >= 1:
            print("There doesn't seem to be anything interesting to read on the " + badmatches[0].name + ".")
        # We found no matches
        else:
            print("I do not know what you are referring to.")

    elif command.startswith("use "):
        objToUse = command.split("use ")[1]
        # Search both the current location and the player's inventory
        matches = player.currentLocation.checkFor(objToUse,Usable) + player.checkFor(objToUse,Usable)
        badmatches = player.currentLocation.checkFor(objToUse,Thing) + player.checkFor(objToUse,Thing)
        # We found an exact match
        if len(matches) == 1:
            matches[0].use()
        # There are multiple matches, so it's ambiguous what the player is referencing
        elif len(matches) > 1:
            print("Are you talking about " + stringFromList(matches,"or") + "?")
        elif len(badmatches) >= 1:
            print("How would you use "+str(badmatches[0])+"?")
        # We found no matches
        else:
            print("I do not know what you are referring to.")
    #help verb
    elif command.startswith("help"):
        print(("Verbs:\n\n"
       " examine:to read clues\n"
       " drop:drop objects to a location\n"
       " get: get objects from a location\n"
       " inventory: to check for contents the player has \n"
       " Verbs to interact with NPC(Non-playable Chracters): \n"
       " praise: to praise NPC \n"
       " fight:player fight NPC \n"
       " manipulate:player try to manipulate NPC\n"
       " debate: player try to debate NPC\n"
       " Each verb must be followed by a noun(except for inventory)\n"
       "Only single space must exist between verb and noun. all letter must be lower case\n\n"))



    elif command.startswith("get "):
        objToGet = command.split("get ")[1]
        matches = player.currentLocation.checkFor(objToGet,Portable)
        badmatches1 = player.checkFor(objToGet,Portable)
        badmatches2 = player.currentLocation.checkFor(objToGet,Thing)
        # We found an exact match
        if len(matches) == 1:
            matches[0].get()
        # There are multiple matches, so it's ambiguous what the player is referencing
        elif len(matches) > 1:
            print("Are you talking about " + stringFromList(matches,"or") + "?")
        # The player may be referring to an item they already have
        elif len(badmatches1) >= 1:
            print("You already have " + str(badmatches1[0]) + ".")
        # The player may be referring to something that is not obtainable
        elif len(badmatches2) >= 1:
            unobtainable = badmatches2[0].name
            # If it's not a proper noun, we will use the article "the"
            if badmatches2[0].article != "":
                unobtainable = "the " + unobtainable
            print("You are cannot remove "+unobtainable+".")
        # We found no matches
        else:
            print("I do not know what you are referring to.")
            
    #Praise verb
            
    elif command.startswith("praise "):
        newvariable1=command.split("praise ")[1]
        matches = player.currentLocation.checkFor(newvariable1,NPC)
        badmatches = player.currentLocation.checkFor(newvariable1,Thing)
        if len(matches)==1 :
            matches[0].praise()
        elif len(matches)>1:
            print("Error. I did not program this, how did you get it?")
        elif len(badmatches)>0:
            print("Who are you trying to screw with? I invented the game.")
        elif len(matches)==0:
            print("You are either in the wrong room or praising the wrong person. Learn some history.")
       
    #Debate Verb
    elif command.startswith("debate "):
        newvariable1=command.split("debate ")[1]
        matches = player.currentLocation.checkFor(newvariable1,NPC)
        badmatches = player.currentLocation.checkFor(newvariable1,Thing)
        if len(matches)==1 :
            matches[0].debate()
        elif len(matches)>1:
            print("Error. I did not program this, how did you get it?")
        elif len(badmatches)>0:
            print("Who are you trying to screw with? I invented the game.")
        elif len(matches)==0:
            print("You are either in the wrong room or debating the wrong person. Stop debating random stuff man.Talking does not make you smart.")
        
    # Manipulate Verb
    elif command.startswith("manipulate "):
        newvariable1=command.split("manipulate ")[1]
        matches= player.currentLocation.checkFor(newvariable1,NPC)
        badmatches = player.currentLocation.checkFor(newvariable1,Thing)
        if len(matches)==1 :
            matches[0].manipulate()
        elif len(matches)>1:
            print("Error. I did not program this, how did you get it?")
        elif len(badmatches)>0:
            print("Who are you trying to screw with? I invented the game.")
        elif len(matches)==0:
            print("You are trying to manipulate the wrong thing.")
    #Fight Verb
    elif command.startswith("fight "):
        newvariable1=command.split("fight ")[1]
        matches= player.currentLocation.checkFor(newvariable1,NPC)
        badmatches = player.currentLocation.checkFor(newvariable1,Thing)
        if len(matches)==1 :
            matches[0].fight()
        elif len(matches)>1:
            print("Error. I did not program this, how did you get it?")
        elif len(badmatches)>0:
            print("Who are you trying to screw with? I invented the game.")
        elif len(matches)==0:
            print("Why are you trying to pick a fight with random things? You have to be more smarter to finish the game.")
    
    #implement drop function
    elif command.startswith("drop "):
        objToGet = command.split("drop ")[1]
        matches = player.checkFor(objToGet,Portable)
        badmatches = player.currentLocation.checkFor(objToGet,Thing)
        # We found an exact match
        if len(matches) == 1:
            matches[0].drop()
        # There are multiple matches, so it's ambiguous what the player is referencing
        elif len(matches) > 1:
            print("Are you talking about " + stringFromList(matches,"or") + "?")
        # The player may be referring to something else in their current location
        elif len(badmatches) >= 1:
            unobtainable = badmatches[0].name
            # If it's not a proper noun, we will use the article "the"
            if badmatches[0].article != "":
                unobtainable = "the " + unobtainable
            print("But you are not carrying "+unobtainable+".")
        # We found no matches
        else:
            print("I do not know what you are referring to.")

    # Implements GIVE X TO Y
    elif command.startswith("give "):
        giveString = command.split("give ")[1]
        givePart = giveString.rpartition(" to ")
        thingToGive = givePart[0]
        npcToGiveTo = givePart[2]
        if(thingToGive == ""):
            print("I do not know what you mean.")
        else:
            thingMatches = player.checkFor(thingToGive,Thing)
            npcMatches = player.currentLocation.checkFor(npcToGiveTo,NPC)
            # We found an exact match for both NPC and the item
            if len(npcMatches) == 1 and len(thingMatches) == 1:
                npcMatches[0].give(thingMatches[0])
            # Possible error messages
            elif len(npcMatches) > 1:
                print("Are you talking about " + stringFromList(npcMatches,"or") + "?")
            elif len(thingMatches) > 1:
                print("Are you talking about " + stringFromList(thingMatches,"or") + "?")
            elif len(npcMatches) == 0:
                print("No idea who you are referring to.")
            elif len(thingMatches) == 0:
                print("You cannot give what you do not have.")

    # "look at" is a synonym for "examine"
    elif command.startswith("look at "):
        objToLookat = command.split("look at ")[1]
        parseCommand("examine "+objToLookat)

    # "take" is a synonym for "get"
    elif command.startswith("take "):
        objToGet = command.split("take ")[1]
        parseCommand("get "+objToGet)

    # permit "go" prefix in game, for instance "go north" should be synonym for "north"
    elif command.startswith("go "):
        gosuffix = command.split("go ")[1]        
        parseCommand(gosuffix)
            
       
    else:
        print("I do not understand what you want to do.")
