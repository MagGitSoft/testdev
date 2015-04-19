# -*- coding: cp1252 -*-


###''''''''''''''''''''''''''''''''''''''''''###
###~~~Definitionary~~~~~~~~~~~~~~~~~~~~~~~~~~###
###''''''''''''''''''''''''''''''''''''''''''###


''''''''''''''''''''''''
# str_choice accepts any string input that matches with 'options'-list in argument
def str_choice(text, options, complaint): #choice function with three arguments:
                                          #(text, options, complaint)
    counter = 1
    #print counter
    choicein = raw_input(text + "\n")
    choicein = choicein.lower() #converts 'choicein'-input to lowercase

    #while counter below 5 and 'choicein' string is not found in 'options'-list
    while (counter <= 4 and choicein not in options):
        if counter == 1:
            print complaint + ", ".join(options) #syntax for joining list entries in string.
            #print "\n"
        counter += 1 #same as (counter = counter + 1)
        #print counter #print attempts
        choicein = raw_input(text + "\n")
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
        print i, options[i]          #print i, then value 'i' from 'options'-list
                                     #SO: Basically prints list 'options' with index number
                                     #from entry 1 (not first entry [0]) to end of list.
            
    choicein = raw_input(text + "\n")

    #while counter below 5 and while 'choicein' isn't in accepted range of numbers (and is an int):
    while (counter <= 4 and is_int(choicein) not in range(1, len(options))):
        if counter == 1:
            print complaint
        counter += 1
        #print counter #print attempts
        choicein = (raw_input(text + "\n"))

    #if 'choicein' IS in accepted range of numbers (and is an int):
    if is_int(choicein) in range(1, len(options)):
        return int(choicein) #return the input of 'choicein' and convert to int.
        
    else:
        return 0
''''''''''''''''''''''''




###''''''''''''''''''''''''''''''''''''''''''###
###~~~Script Start~~~~~~~~~~~~~~~~~~~~~~~~~~~###
###''''''''''''''''''''''''''''''''''''''''''###

name = raw_input("What's your name?\n")
name = name.capitalize()

# Define a list of jobs
jobs = ["bum","mage", "rogue", "warrior"]

#job = output of str_choice, which gives a string
job = str_choice("What's your job? ", jobs, "That's not a job"
                       "! These are jobs: \n")

print ("\n 'Hello %s! You're the most shabby-looking %s I've run into, ever." % (name, job)
       + " What are you doing in my cave? You could have at least started"
       + " the fire for me!'\n"
       + " You wake up with a jolt, and you feel a gentle warmth on your"
       + " cheeks as you sit up. You quickly scan your surroundings,"
       + " your eyes fixate on a rabbit-like creature sitting on a"
       + " comfortable rock. Having only seen regular rabbits and hares,"
       + " you shiver at the sight of its big, floppy ears, dangling"
       + " near the floor, and the dog-sized, fluffy, and suspiciously"
       + " cute animal sends shivers down your back.\n")


rabbitcave = ["Game Over",
              "punch the rabbit in the face",
              "take a deep breath, consider surroundings",
              "explain your sorry state",
              "grab your backpack and sprint out of the cave"]

#rabbitcaveopt = output of int_choice, which gives an int
rabbitcaveopt = int_choice("What do you do? ", rabbitcave, "Come on, you gotta pick a number!")



''''''''''''''''''''''''''''''''''''''''''''''''


rabbitcaveend = ["\n Aww, you lost. There's a very simple reason for that."
                 + " You have to actually choose to do something,"
                 + " otherwise you will starve or thirst to death!"
                 + " ...unless, of course, some other cause of death"
                 + " reaches you first... which is what actually happened."
                 + " Please, please, applaud not, for I am without both"
                 + " pen and paper, and I may therefore not scribble my name."
                 + "\n So there, you may go now. This game is over. Shoo, shoo!",
                 
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
                 
                 "\n "
                 + "test3",
                 
                 "test4",

                 "test5"]

print rabbitcaveend[rabbitcaveopt]

