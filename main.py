#!/usr/bin/env python3

import utils,sys,time #Added sys and time to simulate typing

utils.check_version((3,7))
utils.clear()

def cls():
    print('\n'*50)

def print_slow(str): #Humanlike typing speeds. I got the code from stack overflow at https://stackoverflow.com/questions/4099422/printing-slowly-simulate-typing from this user https://stackoverflow.com/users/1366738/sebastian.
    for letter in str:
        sys.stdout.write(letter)
        sys.stdout.flush()
        time.sleep(0.1)

def print_fast(str):
    for letter in str:
        sys.stdout.write(letter)
        sys.stdout.flush()
        time.sleep(0.075)

def print_super_slow(str):
    for letter in str:
        sys.stdout.write(letter)
        sys.stdout.flush()
        time.sleep(0.5)




def print_h(str): #For the hand
    for letter in str:
        sys.stdout.write(letter)
        sys.stdout.flush()
        time.sleep(0.01)


print_fast("Salutataions!") #Greeetings
time.sleep(0.75)
print_slow ("\nMy name is Mark Daniel Borkowski!")
time.sleep (0.5)
cls()

name = '' #What's my name?
while (name != 'mark'):
    name = input("\n What is my first name?")
    name = name.lower().strip()
    if (name == 'mark'):
        print_slow('\nNice,')
        time.sleep(0.5)
    else:
        print_slow('\nClose, but that is not my first name.')
print_slow(" I am glad you are paying attention!")
time.sleep(1)
input("\n What is your favorite game?") #I figured there were too many games that I could make a tailored response for so I just had one response
print_slow("\n Awesome! I am not sure if I know that one...") #Another time perhaps
time.sleep(3)
cls()

print_slow("\n I mostly play MOBAs or Multiplayer Online Battle Areas.") #I kinda like these a bit too much
time.sleep(0.5)
print_slow("\n I know,")
time.sleep(0.25)
print_slow(" it is a mouthful.") 
time.sleep(0.5) 

print_h("░▄▀▄▀▀▀▀▄▀▄░░░░░░░░░") #Annoying Dogo
print_h("░█░░░░░░░░▀▄░░░░░░▄░")
print_h("█░░▀░░▀░░░░░▀▄▄░░█░█")
print_h("█░▄░█▀░▄░░░░░░░▀▀░░█")
print_h("█░░▀▀▀▀░░░░░░░░░░░░█")
print_h("█░░░░░░░░░░░░░░░░░░█")
print_h("█░░░░░░░░░░░░░░░░░░█")
print_h("░█░░▄▄░░▄▄▄▄░░▄▄░░█░")
print_h("░█░▄▀█░▄▀░░█░▄▀█░▄▀░")
print_h("░░▀░░░▀░░░░░▀░░░▀░░░")

print_super_slow("\n Haha!") 
time.sleep(0.5) 
print_slow("\n MOBAs started from a Worcraft Mod called Defense of the Ancients or DOTA.")
print_slow("\n Some of the games I play include DOTA 2, League of Legends, Subnautica, Rust,")
time.sleep(0.4)
print_super_slow(" Undertale,") 
print_slow(' INSIDE, and Warframe.')
time.sleep(2)
print_slow("\n If I had to pick a favorite game it would have to be...")
time.sleep(4)
print_super_slow(" DOTA2!")
time.sleep(0.5)
cls()

game = '' #Favorite game question!
while (game != 'dota2' and game != 'defense of the ancients 2'):
    game = input("\n What is my favorite game?")
    game = game.lower().strip()
    if (game == 'dota2'):
        print_fast('\nGreat job,')
        time.sleep(0.5)
        print_slow(' you remmebered!')
    else:
        print_fast('\nThat')
        print_super_slow('...')
        time.sleep(0.4)
        print_slow(' was not the game I mentioned.')
cls()
print_slow('\nMy concerns for this class are mostly related to the amount of time I would like to spend on projects versus the amount of time I') #Concerns, no transition....
time.sleep(1)
print_fast(' actually have')
print_super_slow('...')
print_slow('\nI hope to get faster at coding and stuff so I can keep getting extra practice and experience in this class!')
print_fast('\nI am actually pretty surprised that you stuck around for this long.')

enter = ''
while (enter != 'yes'):
    enter = input('\n Am I entertaining you?')
    enter = enter.lower().strip()
    if (enter == 'yes'):
        print_fast("\n That's what I like to hear!")
    else:
        print_slow("\n I am sorry you have to sit through")
        time.sleep (3)
        print_super_slow(" t h i s .")

print_slow('\nI am excited about learning how to code because I want to make my own games!') #I am excited!
print_fast('\nI am also excited to learn more about digital art and Hungarian!')
time.sleep(2)

cls()
print_fast('Did I mention that my stack overflow user ID is:16580074?') #stack overflow ID
time.sleep(1)
print_slow('\nWell,')
time.sleep(0.5)
print_slow(' it is.')
time.sleep(2)
print_fast('\nAre you waiting for an input?') #Jokes on the person running this! It's not an input!
time.sleep(4)
print_slow('There will be no input')
print_super_slow('. . .')
time.sleep(1)
cls()
print_fast("\nDid I mention that my GitHub URL is https://github.com/ToxiicMarker !") #GitHub Username
print_slow('\nThis would make my username...')

Git_Hub = '' #GitHub Question
while (Git_Hub != 'toxiicmarker'):
    Git_Hub = input('\nWhat is my username?')
    Git_Hub = Git_Hub.lower().strip()
    if(Git_Hub == 'toxiicmarker'):
        print_fast("\nGood job!")
        print_fast("( ͡ᵔ ͜ʖ ͡ᵔ )")
    elif(Git_Hub == 'toxicmarker'):
        time.sleep(1)
        print_fast("\n Two i's")
        print_slow("\n ಠ╭╮ಠ")
    else:
        print_slow("\nIt is literally right")
        print(" there")
        time.sleep(1)
        print_super_slow(" ^ ^ ^ ༼ つ ಥ_ಥ ༽つ ^ ^ ^ ")
print_slow("\nI think that is all for today!")
cls()
print_slow('I hope you enjoyed this as much as I did!') #Goodbye
print_h("\n-+88_")
print_h("\n_+880_")
print_h("\n_++88_")
print_h("\n_++88_")
print_h("\n__+880_________________________++_")
print_h("\n__+888________________________+88_")
print_h("\n__++880______________________+88_")
print_h("\n__++888_____+++88__________+++8_")
print_h("\n__++8888__+++8880++88____+++88_")
print_h("\n__+++8888+++8880++8888__++888_")
print_h("\n___++888++8888+++888888++888_")
print_h("\n___++88++8888++8888888++888_")
print_h("\n___++++++888888888888888888_")
print_h("\n____++++++88888888888888888_")
print_h("\n____++++++++000888888888888_")
print_h("\n_____+++++++000088888888888_")
print_h("\n______+++++++00088888888888_")
print_h("\n_______+++++++088888888888_")
print_h("\n_______+++++++088888888888_")
print_h("\n________+++++++8888888888_")
print_h("\n________+++++++0088888888_")
print_h("\n________++++++0088888888_")
print_h("\n________+++++0008888888_")
print_h("\n________#############_")
print_slow("\nHave a nice day.")























