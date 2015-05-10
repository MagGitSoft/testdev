# -*- coding: cp1252 -*-
import random
import tables

###''''''''''''''''''''''''''''''''''''''''''###
###~~~Definitionary~~~~~~~~~~~~~~~~~~~~~~~~~~###
###''''''''''''''''''''''''''''''''''''''''''###
''''''''''''''''''''''''
'''
def combat(player, opponent):
    while player.hp or opponenthp <= 0:
        

'''
''''''''''''''''''''''''
def dice(sides, throws):
    rolls = [0] * 7
    for i in range(throws):
        if sides == 4:
            roll = random.randint(1, 4)
            if roll == 1:
                
        if sides == 6:
            return random.randint(1, 6) 
    else:
        return 0
        
''''''''''''''''''''''''
def monster(species, name):
    name = name
    species = species
    hp = 100
    atk = dice(4, 1)
    init = random.randint(1, 20)
''''''''''''''''''''''''
def playerstats(name, job):
    name = name
    job = job
    hp = 100
    atk = dice(6, 1)
    init = random.randint(1, 20)
    
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

player = playerstats(name, job)
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

rabbit = monster("barbit", "Barbit")
