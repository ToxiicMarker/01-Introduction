#!/usr/bin/env python3

import utils,sys,time

utils.check_version((3,7))
utils.clear()

def cls():
    print('\n'*50)

def print_slow(str):
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

print_fast("Salutataions!")
time.sleep(0.75)
print_slow ("\nMy name is Mark Daniel Borkowski!")
time.sleep (0.5)
cls()

name = ''
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
input("\n What is your favorite game?")
print_slow("\n Awesome! I am not sure if I know that one...")
time.sleep(3)
cls()

print_slow("\n I mostly play MOBAs or Multiplayer Online Battle Areas.")
time.sleep(0.5)
print_slow("\n I know,")
time.sleep(0.25)
print_slow(" it is a mouthful.") 
time.sleep(0.5) 
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

game = ''
while (game != 'dota2' and game != 'defense of the ancients 2'):
    game = input("\n What is my favorite game?")
    game = game.lower().strip()
    if (game == 'dota2' or 'defense of the ancients 2'):
        print_fast('\nGreat job,')
        time.sleep(0.5)
        print_slow(' you remmebered!')
    else:
        print_fast('\nThat...')
        time.sleep(0.4)
        print_slow('was not the game I mentioned.')