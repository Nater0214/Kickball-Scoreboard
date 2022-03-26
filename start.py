# start.py
# The starting and setup for the program


# Imports
from os import system as cmdline
from inputloop import inputloop


# Methods
def start():
    cmdline('cls')
    
    print("Welcome to Kickball Scoreboard!\nYou will need to read the README file to understand this well")
    inp = inputloop("Start how?", "options", ['p', 'n', 'f'])