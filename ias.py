# -*- coding: cp1252 -*-
import sys
import random
from tables import *
import numpy
from pandas import DataFrame, read_csv

###''''''''''''''''''''''''''''''''''''''''''###
###~~~Definitionary~~~~~~~~~~~~~~~~~~~~~~~~~~###
###''''''''''''''''''''''''''''''''''''''''''###
''''''''''''''''''''''''
'''
class StatsTable(IsDescription):
    #tables.open_file(filename, mode='r', title='',
    #root_uep='/', filters=None, **kwargs)
    h5file = open_file("iastables.h5", mode = "w", title = "Test file")
    #File.create_group(where, name, title='',
    #filters=None, createparents=False)
    group = h5file.create_group("/", 'mobinfo', 'Mobstats, playerstats etc.')
    #ile.create_table(where, name, description=None, title='',
    #filters=None, expectedrows=10000, chunkshape=None,
    #byteorder=None, createparents=False, obj=None)
    table = h5file.create_table()
        
    #columns
    
    name      = StringCol(16)   # 16-character String
    idnumber  = Int64Col()      # Signed 64-bit integer
    ADCcount  = UInt16Col()     # Unsigned short integer
    TDCcount  = UInt8Col()      # unsigned byte
    grid_i    = Int32Col()      # 32-bit integer
    grid_j    = Int32Col()      # 32-bit integer
    pressure  = Float32Col()    # float  (single-precision)
    energy    = Float64Col()    # double (double-precision)

    idnumber = Int64Col()       #Signed 64-bit integer
    name = StringCol(16)        #16 character string
    surname = StringCol(16)     #--||--
    hpbase = Int32Col()         #32-bit integer
    manabase = Int32Col()       #--||--
    
    h5file.close()
    '''
''''''''''''''''''''''''
def dice(sides, throws):
    rolls = [0] * 21 #rolls = list with the value 0 in 7 additions
    for i in range(throws):
        
        #4-sided die
        if sides == 4:
            roll = random.randint(1, 4)#random int between (x, y)
            #checks what int is output and adds 1 to corresponding index
            if roll in range(1, 5):
                rolls[roll] += 1
                
        #6-sided die
        if sides == 6:
            roll = random.randint(1, 6)
            if roll in range(1, 7):
                rolls[roll] += 1
        
        if sides == 20:
            roll = random.randint(1, 20)
            if roll in range(1, 21):
                rolls[roll] += 1
    
    
    roll_result = []
    #loop over chosen elements (here, entire rolls list)
    for i in range(1,len(rolls)):
        #for hvert tall mellom 0 og frekvens på indeks i
        for n in range(0, rolls[i]):
            #legg til frekvens antall i'er (terningkast på gjeldende indeks)
            #i listen roll_result
            roll_result.append(i)
    #Loops over all frequencies of throws,
    #then adds 'i' frequency number of
    #times into roll_result
    return rolls, roll_result
    
''''''''''''''''''''''''
#def diceval(rolls):
    
''''''''''''''''''''''''
class Monster:
    def __init__(self, name, species, hp, damage):
        self.name = name
        self.species = species
        self.hp = 100
        self.damage = 5
        self.atk = dice(4, 1)
        self.initiative = 1

    #def unconscious(self):
        #return self.hp <= 0 and self.hp > -10
    
    def undefeated(self):
        return self.hp > 0
            
''''''''''''''''''''''''
class Player:
    def __init__(self, name, job):
        self.name = name
        self.hp = 100
        self.mana = 100
        self.damage = 5
        self.job = job
        self.initiative = 1
    def attackDmg(self):
        return random.randint(5,20)
    def alive(self):
        return self.hp > 0
        if self.hp <= 0:
            print ("Du er dævv.")
            sys.exit("Virkelig, skikkelig dævv...")

''''''''''''''''''''''''
def combat(player, monster):
    turn = 0
    turn += 1
    
    count = 1
    while count == 1:
        #playerini = random.randint(1, 3)
        #monsterini = 1
        playerini = dice(20, 1)[1][0] + player.initiative
        monsterini = dice(20, 1)[1][0] + monster.initiative
        
        if monsterini > playerini:
            print ("%s goes first!" % (monster.name))
            inidmg = monster.damage
            player.hp -= inidmg
            print ("%s does %s damage!" % (monster.name, str(inidmg)))
            count += 1
            break
        
        elif playerini > monsterini:
            print ("You go first!")
            count += 1
            break
        
        else:
            count = 1
    mon_ini = monster.initiative
    mon_ini_str = str(mon_ini)
    plr_ini = player.initiative
    plr_ini_str = str(plr_ini)    
    print
    print ("Monster initiative roll:", str(monsterini), \
           "(", (monsterini - mon_ini), "+" \
           , mon_ini_str, ")")
    print ("Player initiative roll: " + str(playerini) + \
           " (", (playerini - plr_ini), "+" \
           , plr_ini_str, ")")
    
    while monster.undefeated() and player.alive():
        print ("\nTurn: ", turn)
        print ("Monster health:", monster.hp)
        print ("Player health: ", player.hp)
        
        fightchoice = input("Attack, heal or run?\n")        
        if fightchoice == ("attack" or "a"):
            dmgDealt = player.attackDmg()
            monster.hp -= dmgDealt
            print ("You dealt", dmgDealt, "damage!")
            
        elif fightchoice == "heal":
            player.hp += 50
        else:
            
            if fightchoice == "run":
                print ("You ran from the %s" % monster.species)
                break
            elif player.alive != True:
                print ("You've been defeated!")
                break
            else:
                print ("%s is defeated!" % monster.species)
                break
        
        
        monsterDmg = monster.damage
        player.hp -= monsterDmg
        print ("%s dealt %s damage to you!" % (monster.species, monsterDmg)) 
    
    if monster.undefeated == False and player.alive == True:
        print ("Congratulations, you won the battle!")
        
''''''''''''''''''''''''

# str_choice accepts any string input that matches with 'options'-list in argument
def str_choice(text, options, complaint): #choice function with three arguments:
                                          #(text, options, complaint)
    counter = 1
    #print counter
    choicein = input(text + "\n")
    choicein = choicein.lower() #converts 'choicein'-input to lowercase

    #while counter below 5 and 'choicein' string is not found in 'options'-list
    while (counter <= 4 and choicein not in options):
        if counter == 1:
            print (complaint + ", ".join(options)) #syntax for joining list entries in string.
            #print "\n"
        counter += 1 #same as (counter = counter + 1)
        #print counter #print attempts
        choicein = input(text + "\n")
        choicein = choicein.lower()

    if choicein in options:
        return choicein
    else:
        return options[0]
''''''''''''''''''''''''
#
#
#
''''''''''''''''''''''''
def is_int(intcheck): #int checking function
    try:
        return int(intcheck)
    except ValueError:
        return False
''''''''''''''''''''''''
#
#
#
''''''''''''''''''''''''
# int_choice accepts an integer input between 1 and the length of 'options'-list
def int_choice(text, options, complaint):
    counter = 1
    #print counter
    
    for i in range(1, len(options)): #for integer 'i' from 1 to length of 'options'-list
        print (i, options[i])        #print i, then value 'i' from 'options'-list
                                     #So: Basically prints list 'options' with index number
                                     #from entry 1 (not first entry [0]) to end of list.
            
    choicein = input(text + "\n")

    #while counter below 5 and while 'choicein' isn't in accepted range of numbers (and is an int):
    while (counter <= 4 and is_int(choicein) not in range(1, len(options))):
        if counter == 1:
            print (complaint)
        counter += 1
        #print counter #print attempts
        choicein = (input(text + "\n"))

    #if 'choicein' IS in accepted range of numbers (and is an int):
    if is_int(choicein) in range(1, len(options)):
        return int(choicein) #return the input of 'choicein' and convert to int.
        
    else:
        return 0
''''''''''''''''''''''''




###''''''''''''''''''''''''''''''''''''''''''###
###~~~Script Start~~~~~~~~~~~~~~~~~~~~~~~~~~~###
###''''''''''''''''''''''''''''''''''''''''''###

name = input("What's your name?\n")
name = name.capitalize()

# Define a list of jobs
jobs = ["bum","mage", "rogue", "warrior"]

#job = output of str_choice, which gives a string
job = str_choice("What's your job? ", jobs, "That's not a job"
                       "! These are jobs: \n")

player = Player(name, job)
print (player)

print ("\n 'Hello %s! You're the most shabby-looking %s I've" % (name, job)
       + " run into, ever. What are you doing in my cave? You could've at"
       + " least started the fire for me while I was gone, sleepyhead!'\n"
       + " You wake up with a jolt, and you feel a gentle warmth on your"
       + " cheeks as you sit up. You quickly scan your surroundings."
       + " The cave is small, no bigger than a decent shed. Along the inner"
       + " wall there's a makeshift table and a rock to sit on. Only"
       + " a couple feet away there's an unlit torch stuck in some dirt in"
       + " the ground. Next to that, there's a backpack with some leaves"
       + " and shears. Your eyes fixate on a huge, upright rabbit sitting on"
       + " a comfortable rock chair, if you can call it that. Having only"
       + " seen regular rabbits and hares before, you're startled."
       + " You shiver at the sight of its big, floppy ears, dangling"
       + " near the floor, and the dog-sized, fluffy, and suspiciously"
       + " cute animal sends shivers down your back.\n")


rabbitcave = ["Game Over",
              "punch the rabbit in the face",
              "take a deep breath, consider surroundings",
              "explain your sorry state",
              "grab your backpack and sprint out of the cave",
              "go outside"]

#rabbitcaveopt = output of int_choice, which gives an int
rabbitcaveopt = int_choice("What do you do? ",
                           rabbitcave,
                           "Come on, you gotta pick a number!")



''''''''''''''''''''''''''''''''''''''''''''''''


rabbitcaveend = ["\n Aww, you lost. There's a very simple reason for that."
                 + " You have to actually choose to do something,"
                 + " otherwise you will starve or thirst to death!"
                 + " ...unless, of course, some other cause of death"
                 + " reaches you first... which is what actually happened."
                 + " Please, please, applaud not, for I am without both"
                 + " pen and paper, and I may therefore not scribble my name."
                 + "\n So there, you may go now. This game is over. Shoo, shoo!",
                 #Option 1
                 "\n You jump out of your sheets, and quickly take a step towards"
                 + " the rabbit. Your arm, from its pulled-back position, fires"
                 + " towards the rabbit at speeds you didn't think your arms could."
                 + " The fire next to you started to crackle violently from the"
                 + " vibrations now emanating from your stomping feet, nearly like"
                 + " a cheering crowd. You notice time seemingly slow down from the"
                 + " abrupt wake-up, and only inches from the rabbits face, when"
                 + " Benny the bouncy bunny springs from his throne, stabs you with"
                 + " its fluffy behind. You barely catch a glimpse of a red barb"
                 + " and a few trailing drops as it leaves your forearm, before"
                 + " you realize that the rabbit is behind you.",
                 #Option 2
                 "\n You take a look around you as you cautiously rise from your"
                 + " sleeping gear. The entrance of the cave seems to be small"
                 + " enough that you'd have to be on all fours to get through."
                 + " The ceiling is only about two feet taller than you. The"
                 + " table has a knife on it and some chopped up herbs. The"
                 + " backpack has some herbs that you recognize, and some you"
                 + " don't, but from what you gather, it looks like dinner."
                 + " The rabbit, now poking the seemingly newly lit fire with"
                 + " a stick, takes quick glances at you.",
                 #Option 3
                 "\n Wooow, last night must have been the wildest party! The drinks"
                 + " are still lingering! That must have been some potent stuff"
                 + ", never thought I'd see a talking rabbit. So what part of"
                 + " my subconscious are you? Angela the angel or Dean the devil?",
                 #Option 4
                 "\n You make a split-second decision to run at the sight of"
                 + " mr. furryneck. You reach for your backpack, but you"
                 + " only grab at the air a few times. You jump up and sprint"
                 + " for the only exit, but you realize just a moment too late"
                 + " that it's far too tight to get out upright, so in a heroic"
                 + " attempt to dodge a headbang, you dive. You get down on"
                 + " all fours and tumble into the upper edge. Your head hurts"
                 + " for just a blink, before you black out.",
                 #Option 5
                 "You go outside."]

print (rabbitcaveend[rabbitcaveopt])

if rabbitcaveopt == 5:
    print ("You step outside to find a similar rabbit to the one inside. Only"
           + " this one looks angrier. It jumps towards you and you slide"
           + " aside to dodge it. You've been attacked, oh my!")

rabbit = Monster("Wild Barbit", "Barbit", 100, 5)