# Dr. McCartin-Lim's Adventure Game Engine 0.5
#updated by Fardin for the Easter Egg Game

from classes import *
from helperfunctions  import *

#General Cao Character Interaction
class Cao(NPC):
    alive=False
    dienextturn=False
    def updateEveryTurn(self):
        global ancient_china
        if scepter in ancient_china.contents and self.alive==False: 
            print("General Cao's statue has suddenly comes to life")
            print("He looks at you with intrigue.You have the option to praise,manipulate,fight and debate.Your life depends on it")
            self.alive=True
            self.dienextturn=True
        elif ancestralheirloom in ancient_china.contents and self.alive==False: 
            print("General Cao's statue has suddenly come to life")
            print("He looks at you with intrigue.You have the option to praise,manipulate,fight and debate.Your life depends on it")
            self.alive=True
            self.dienextturn=True
        elif pyramid in ancient_china.contents and self.alive==False: 
            print("General Cao's staute has suddenly come to life ")
            print("He looks at you with intrigue.You have the option to praise,manipulate,fight and debate.Your life depends on it")
            self.alive=True
            self.dienextturn=True
        elif self.dienextturn==True:
            print("General Cao Cao has lost his patience with your unsatisfying response. He has driven a sword right through your heart.")
            exit()        
    def praise(self):
        if self.alive==True:
            print("General Cao is not pleased. He is not swayed by flattery") 
            print("You are dead")   
            exit()
        else:
            super().praise()
    def debate(self):
        if self.alive==True and self.dienextturn:
            print("General Cao is intrigued by your knowledge. However, he is a master manipulator and see you as a threat to his vast knowledge")
            print("He poisons you")
            exit()
        else:
            super().debate()
    def manipulate(self):
        if self.alive==True:
            print("General Cao sees himself in your reflection. He will let you live another day")
            self.dienextturn=False
        else:
            super().manipulate()
    def fight(self):
        if self.alive==True:
            print("Cao is disgusted by you resorting to force.Much like Yuan Shao you fall due to his superior intellect.")
            print("You are dead")
            exit()
        else:
            super().fight()


#Genghis Khan Chracter Interaction
class Genghis(NPC):
    alive=False
    dienextturn=False
    def updateEveryTurn(self):
        global steppedhordes
        if scepter in steppedhordes.contents and self.alive==False: 
            print("The Great Khan has come to life")
            print("He looks at you with intrigue.You have the option to praise,manipulate,fight and debate.Your life depends on it")
            self.alive=True
            self.dienextturn=True
        elif bow in steppedhordes.contents and self.alive==False: 
            print("The Great Khan has come to life")
            print("He looks at you with intrigue.You have the option to praise,manipulate,fight and debate.Your life depends on it")
            self.alive=True
            self.dienextturn=True
        elif jadeseal in steppedhordes.contents and self.alive==False: 
            print("The Great Khan has come to life")
            print("He looks at you with intrigue.You have the option to praise,manipulate,fight and debate.Your life depends on it")
            self.alive=True
            self.dienextturn=True
        elif self.dienextturn==True:
            print("Genghis has lost his patience with your unsatisfying response. He has put arrow right through your heart.")
            exit()        
    def praise(self):
        if self.alive==True:
            print("Khan is not pleased. He is not swayed by flattery") 
            print("You are dead")   
            exit()
        else:
            super().praise()
    def debate(self):
        if self.alive==True and self.dienextturn:
            print("Khan does not take to idle talk")
            print("You are dead")
            exit()
        else:
            super().debate()
    def manipulate(self):
        if self.alive==True:
            print("Khan is not bemused by your cheap trickery.")
            print("You are dead")
            exit()
        else:
            super().manipulate()
    def fight(self):
        if self.alive==True:
            print("Khan respects your bravery. A man who is brave enough to defend himself has earned the respect of the Khan.")
            self.dienextturn=False
        else:
            super().fight()
        

#Athena NPC chracter interaction
class Athena(NPC):
    alive=False
    dienextturn=False
    def updateEveryTurn(self):
        global ancient_greece
        if purpletogre in ancient_greece.contents and self.alive==False: 
            print("Athena has come to life")
            print("She looks at you with disgust.You have the option to praise,manipulate,fight and debate.Your life depends on it")
            self.alive=True
            self.dienextturn=True
        elif scepter in ancient_greece.contents and self.alive==False: 
            print("Athena has come to life")
            print("She looks at you with disgust.You have the option to praise,manipulate,fight and debate.Your life depends on it")
            self.alive=True
            self.dienextturn=True
        elif oldestliterature in ancient_greece.contents and self.alive==False: 
            print("Athena has come to life")
            print("She looks at you with disgust.You have the option to praise,manipulate,fight and debate.Your life depends on it")
            self.alive=True
            self.dienextturn=True
        elif self.dienextturn==True:
            print("Athena has lost her patience with your unsatisfying response. She has sent you to Hades")
            exit()        
    def praise(self):
        if self.alive==True:
            print("Athena is not pleased. She is the goddess of wisdom, she does not take to flattery.") 
            print("You are dead")   
            exit()
        else:
            super().praise()
    def debate(self):
        if self.alive==True and self.dienextturn:
            print("Athena finds your knowledge acceptable.You will not meet Hades Today")
            self.dienextturn=False
        else:
            super().debate()
    def manipulate(self):
        if self.alive==True:
            print("Athena is not pleased. She is the goddess of wisdom, she does not take to trickery.")
            print("You are dead")
            exit()
        else:
            super().manipulate()
    def fight(self):
        if self.alive==True:
            print("Athena respects your bravery. You will not be taken to the underworld today")
            self.dienextturn=False
        else:
            super().fight()

#Rival
class Rival(NPC):
    alive=False
    dienextturn=False
    def updateEveryTurn(self):
        global shogun_exhibit,rival
        if ancestralheirloom in shogun_exhibit.contents and self.alive==False: 
            rival.explicitMention=True
            print("You rival enters the hall.")
            print("He smirks at you as he is one move away from winning. You have the option to manipulate,fight,debate,or praise your rival to stop him from winning.Choose Wisely")
            self.alive=True
            self.dienextturn=True
        elif self.dienextturn==True:
            print("You avoided you rival.He won the game.You are disgusted with yourself because of your failure")
            exit()        
    def praise(self):
        if self.alive==True:
            print("You praised your rival and thus confused him.He had second thoughts and has now lost his advantage.") 
            print("You have a chance to win the game")   
            self.dienextturn=False
        else:
            super().praise()
    def debate(self):
        if self.alive==True:
            print("Your debating shows your desperation and your rival ends the game quickly")
            exit()
        else:
            super().debate()
    def manipulate(self):
        if self.alive==True:
            print("You confuse your rival.He retraces his clues thus losing his advantage.")
            print("You yet have a chance to win the game")
            self.dienextturn=False
        else:
            super().manipulate()
    def fight(self):
        if self.alive==True:
            print("As you fight with your rival the security guard comes and throws you out.")
            print("You are out of the game")
            exit()
        else:
            super().fight()


   
#Object Placement Easter Egg Methods
    
class Dress(Portable):
    def drop(self):
        global subsaharanafrica,player,clue2,bow
        if player.currentLocation==subsaharanafrica:
            clue2.interactable=True
            bow.interactable=True
        super().drop()

class Togre(Portable):
    def drop(self):
        global steppedhordes,player,clue3,purpletogre
        if player.currentLocation==steppedhordes:
            clue3.interactable=True
            purpletogre.interactable=True
        super().drop()

class Scepter(Portable):
    def drop(self):
        global ancient_rome,player,clue4,scepter
        if player.currentLocation==ancient_rome:
            clue4.interactable=True
            scepter.interactable=True
            key1.interactable=True
        super().drop()
class Ancestralheirloom(Portable):
    def drop(self):
        global ancient_egypt,player,clue5,ancestralheirloom
        if player.currentLocation==ancient_egypt:
            clue5.interactable=True
            ancestralheirloom.interactable=True
        super().drop()
class OldestLiterature(Portable):
    def drop(self):
        global shogun_exhibit,player,clue6,oldestliterature
        if player.currentLocation==shogun_exhibit:
            clue6.interactable=True
            oldestliterature.interactable=True
        super().drop()

class Pyramid(Portable):
    def drop(self):
        global ancient_mesopotamia,player,clue7,pyramid
        if player.currentLocation==ancient_mesopotamia:
            clue7.interactable=True
            pyramid.interactable=True
            key2.interactable=True
        super().drop()
class Jadeseal(Portable):
    def drop(self):
        global ancient_americas,jadeseal,clue8,player
        if player.currentLocation==ancient_americas:
            clue8.interactable=True
            jadeseal.interactable=True
            key3.interactable=True
        super().drop()
class Statue(Portable):
    def drop(self):
        global ancient_china,statue,clue9,player
        if player.currentLocation==ancient_china:
            clue9.interactable=True
            statue.interactable=True
            key4.interactable=True
        super().drop()

class Blooddiamond(Portable):
    def drop(self):
        global ancient_greece,blooddiamond,clue10,player
        if player.currentLocation==ancient_greece:
            clue10.interactable=True
            blooddiamond.interactable=True
        super().drop()
class Final(Portable):
    def drop(self):
        global ancient_bharat,player
        if player.currentLocation==ancient_bharat:
            print("You have reached the final part of the puzzle")
            print("Please use all the four keys to end the game")
            
class Keys(Portable,Usable):
    used=False
    def use(self):
        global ancient_bharat,key1,key2,key3,key4,player
        if player.currentLocation==ancient_bharat:
            self.used=True                 
            print("You have used "+ str(self))             
        else:
            super().use()    
    
class Endgame(Thing):
    def updateEveryTurn(self):
        if key1.used==True and key2.used==True and key3.used==True and key4.used==True:
            print ("Congratulations,you won the game")
            exit()
        
   
        
  
                   


# NPC

rival= Rival("rival")
rival.aliases=["rival","enemy"]
rival.explicitmention=False

caocao=Cao("general")
caocao.aliases=["cao cao","general","king","trickster","cao"]
caocao.explicitmention=True

athena=Athena("goddess")
athena.aliases=["goddess","athena"]
athena.explicitmention=True

cleopatra= Thing ("queen")
cleopatra.aliases=["queen","pharaoh","lady","empress","cleopatra"]
cleopatra.explicitmention=True

genghiskhan= Genghis("khan")
genghiskhan.aliases=["khan","emperor","warrior","genghis khan"]
genghiskhan.explicitMention = True



# Hidden ITEMS

clue1 = Portable("clue1")
clue1.aliases = ["paper", "scroll", "clue", "script","clue1"]
clue1.description =("Go to the land of Gold and Diamond from whence the richest man came.Beware for the hidden clue to be seen the prize must be presented.")
clue1.explicitMention=False


clue2 = Portable("clue2")
clue2.aliases = ["paper", "scroll", "clue", "script","clue2"]
clue2.description =("They came from the Grassland. They came with death and under the hooves of their horses the world did shook.Beware for the hidden clue to be seen the prize must be presented.")
clue2.explicitMention=False
clue2.interactable=False

clue3 = Portable("clue3")
clue3.aliases = ["paper", "scroll", "clue", "script","clue3"]
clue3.description =("From a tiny dot they did grow and chaged the world forevermore.Beware, for the hidden clue to be seen the prize must be presented.")
clue3.explicitMention=False
clue3.interactable=False


clue4 = Portable("clue4")
clue4.aliases = ["paper", "scroll", "clue", "script","clue4"]
clue4.description =("Look at my accomplishments and wonder ye mortals. In my day I was the god of the desert that even the Sun bent down to.Beware, for the hidden clue to be seen the prize must be presented.")
clue4.explicitMention=False
clue4.interactable=False

clue5 = Portable("clue5")
clue5.aliases = ["paper", "scroll", "clue", "script","clue5"]
clue5.description =("We were masters of the sword. For a good warrior what can be more valuable than his honor and honor must be kept with the sword.Beware, for the hidden clue to be seen the prize must be presented.")
clue5.explicitMention=False
clue5.interactable=False

clue6 = Portable("clue6")
clue6.aliases = ["paper", "scroll", "clue", "script","clue6"]
clue6.description =("From our soil,civilization did rise and world of man was transformed forevemore.Beware for the hidden clue to be seen the prize must be presented.")
clue6.explicitMention=False
clue6.interactable=False

clue7 = Portable("clue7")
clue7.aliases = ["paper", "scroll", "clue", "script","clue7"]
clue7.description =("Seperated from the rest we grew on our own.A civilization to rival that of Rome.Beware for the hidden clue to be seen the prize must be presented.")
clue7.explicitMention=False
clue7.interactable=False

clue8 = Portable("clue8")
clue8.aliases = ["paper", "scroll", "clue", "script","clue8"]
clue8.description =("The Empire long united must divide and long divided must unite.Beware for the hidden clue to be seen the prize must be presented.")
clue8.explicitMention=False
clue8.interactable=False

clue9 = Portable("cLue9")
clue9.aliases = ["paper", "scroll", "clue", "script","clue9"]
clue9.description =("Our legacy is not counted in our wealth or power but the ideas we left behind.Beware for the hidden clue to be seen the prize must be presented.")
clue9.explicitMention=False
clue9.interactable=False

clue10 =Portable("clue10")
clue10.aliases = ["paper", "scroll", "clue", "script","clue10"]
clue10.description =("A land of a thousand different people made into one.At our height our wealth was the talk of legends.")
clue10.explicitMention=False
clue10.interactable=False

#Items to move around

ivorydress = Dress("beautiful dress")
ivorydress.aliases = ["prize", "dress", "gift", "item"]
ivorydress.description =("Take me to my righful master before you are given your next clue")
ivorydress.explicitMention=False

bow = Togre("bow")
bow.aliases = ["prize", "bow", "gift", "item"]
bow.description =("Place me in the hand of the great conqueor")
bow.explicitMention=False
bow.interactable=False

purpletogre = Scepter("toga")
purpletogre.aliases = ["prize", "dress", "gift", "item","toga"]
purpletogre.description =("Ye mortals you have no right to me. Take me to my divine master for ye to continue in ye path.")
purpletogre.explicitMention=False
purpletogre.interactable=False

scepter=Ancestralheirloom("scepter")
scepter.aliases = ["scepter","prize","gift","item","scepter"]
scepter.description = ("Place in the encased tomb of my master before your next path could be revealed.")
scepter.explicitMention=False
scepter.interactable=False

ancestralheirloom = OldestLiterature("sword")
ancestralheirloom.aliases = ["sword","prize","item"]
ancestralheirloom.description = ("I crave honor. Return me to the honorable warriors of past.")
ancestralheirloom.explicitMention=False
ancestralheirloom.interactable=False

oldestliterature = Pyramid("book")
oldestliterature.aliases = ["book","prize","item","gift"]
oldestliterature.description = ("I crave honor. Return me to the honorable warriors of past.")
oldestliterature.explicitMention=False
oldestliterature.interactable=False


pyramid=Jadeseal("pyramid")
pyramid.aliases = ["pyramid","prize","item","gift"]
pyramid.description = ("This is a replica of a magnificient strcuture of the past.Returnit to its rightful exhibition.")
pyramid.explicitMention=False
pyramid.interactable=False

jadeseal=Statue("seal")
jadeseal.aliases=["seal","jadeseal","prize","item","gift"]
jadeseal.description=("I am the symbol of a great civilization.Lost for so long ,pleae return me to my righful master")
jadeseal.explicitMention=False
jadeseal.interactable=False

statue=Blooddiamond("statue")
statue.aliases=["statue","athena","item","gift","prize"]
statue.description=("Forcefully taken from my home and stored where the rays of the sun couldnt reach.Take me abck to my home so I may once bathe in the sunlight")
statue.explicitMention=False
statue.interactable=False

blooddiamond=Final("diamond")
blooddiamond.aliases=["diamond","blooddiamond","prize","gift","item"]
blooddiamond.description=("Men have come from afar to see my beauty.So much blood spilled and so far away from home. Return me to the city of Rajas so I can be in peace.")
blooddiamond.explicitMention=False
blooddiamond.interactable=False

#keys
key1=Keys("key1")
key1.aliases=["key","key1"]
key1.explicitMention=False
key1.interactable=False

key2=Keys("key2")
key2.aliases=["key","key2"]
key2.explicitMention=False
key2.interactable=False

key3=Keys("key3")
key3.aliases=["key","key3"]
key3.explicitMention=False
key3.interactable=False

key4=Keys("key4")
key4.aliases=["key","key4"]
key4.explicitMention=False
key4.interactable=False

endgame=Endgame("R")


# LOCATIONS
        
musuem_entrance = Location("Entrance")
musuem_entrance.description = ("You enter through beautiful ivory gated door. Treasures from around the World Surround you.")
musuem_entrance.contents = []

ancient_egypt = Location("Egyptian Exhibition")
ancient_egypt.description = ("You find yourself enthralled by the glory of the Phraoh's. Mummified Phraoh and his treasure glistens the room golden.")
ancient_egypt.contents = [clue5,ancestralheirloom,cleopatra]

ancient_mesopotamia =Location ("Cradle of Civilization")
ancient_mesopotamia.description = ("On one side is the tablet of Hammurabi and on another is the Epic of Gilgamesh.This is simply where civilization begin.")
ancient_mesopotamia.contents = [clue7,pyramid,key2]

ancient_greece = Location("Greek Exhibit")
ancient_greece.description = ("You see a model warrior in bronze shield and spear.You wonder if that is how Achilles looked.")
ancient_greece.contents = [clue10,athena,blooddiamond]

ancient_china = Location("Han China Exhibition")
ancient_china.description = ("On one side is the picture of the Wise Confucious and another a picture of Sun Tzu. Two different men that has come to define Two Thousand years of Chinese History and you are humbled.")
ancient_china.contents = [clue9,statue,caocao,key4]

ancient_bharat = Location("Subcontinent Exhibition")
ancient_bharat.description = ("The melting pot of civlizations. The home of Ashoka,the place of thousand different people with thousand differen beliefs.")
ancient_bharat.content=[]


ancient_rome = Location("Roman Exhibition")
ancient_rome.description = ("Quo Usque Pro Roma Ibis--How Far will you go for Rome.The sentence that has come to define the edurance and ambition of this great city.Perhaps, one day you could visit the Eternal City yourself.")
ancient_rome.contents = [clue4,scepter,key1]


ancient_americas = Location("The Aztec and Maya Exhibit")
ancient_americas.description = ("You see a picture of the Great Maya pyramid and their ritual sacrifice and a shiver runs down your spine. ")
ancient_americas.contents = [clue8, jadeseal,key3]

subsaharanafrica = Location("Mali Empire Exhibit")
subsaharanafrica.description = ("You see a huge painting of Mansa Musa with his entourage and his wealth and you are kinda jealous.")
subsaharanafrica.contents = [clue2,bow]


steppedhordes = Location("The Mongol Exibit")
steppedhordes.description = ("At the center of the Exhibit there is a statue of a Mongol Warrior in Horseback.He is Subutai one of the dogs of war of Genghis. He has pludered and killed from China to Austria. You are both fascinated and terrified.")
steppedhordes.contents = [clue3, purpletogre,genghiskhan]


shogun_exhibit = Location("The Shogunate")
shogun_exhibit.description = ("Honor and Glory. That is the Shogun Life. You question your own choice. What does it mean to have honour?")
shogun_exhibit.contents = [clue6, oldestliterature,rival]



#Location Directions

musuem_entrance.setWest(ancient_bharat)
musuem_entrance.setEast(ancient_egypt)
musuem_entrance.setNorth(ancient_greece)

ancient_egypt.setWest(musuem_entrance)
ancient_egypt.setSouth(subsaharanafrica)
ancient_egypt.setNorth(ancient_mesopotamia)

ancient_mesopotamia.setNorth(ancient_rome)
ancient_mesopotamia.setSouth(ancient_egypt)

ancient_greece.setNorth(steppedhordes)
ancient_greece.setSouth(musuem_entrance)
ancient_greece.setWest(ancient_americas)
ancient_greece.setEast(ancient_rome)
                      
ancient_china.setSouth(ancient_bharat)
ancient_china.setNorth(ancient_americas)

ancient_bharat.setEast(musuem_entrance)
ancient_bharat.setNorth(ancient_china)

ancient_rome.setWest(ancient_greece)
ancient_rome.setSouth(ancient_mesopotamia)

ancient_americas.setEast(ancient_greece)
ancient_americas.setNorth(shogun_exhibit)
ancient_americas.setSouth(ancient_china)

subsaharanafrica.setNorth(ancient_egypt)

steppedhordes.setWest(shogun_exhibit)
steppedhordes.setSouth(ancient_greece)

shogun_exhibit.setEast(steppedhordes)
shogun_exhibit.setSouth(ancient_americas)

#Intro Message
print(("      Welcome to Historical Easter Egg Hunt\n\n"
       " Your job is to examine clues,prizes\n"
       " You are given some intial clue and prizes in your inventory,please check\n"
       " You must take the prizes and place them in their righful exhibiton and only then will the next clue appear\n"
       " Finally, you must also check for keys in each exhibition.You must present the four keys in the final round to win \n"
       " Beware, unique chracters will show up in your path.You must use knowledge to choose best course of action. Choosing worngly would end the game.\n"
       " You can always use the 'help' function to know what verb to use \n"
       " for starters 'clue','prize; and 'key' will refer to each clue in the game,objects to move around to get the next clue and keys to collect respectively. \n\n"
       " Finally I hope you enjoy the game and if you need to understand the verbs type-'help'.\n\n"))