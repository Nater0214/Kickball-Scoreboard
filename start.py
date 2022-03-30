# start.py
# The starting and setup for the program


# Imports
from os import system as cmdline
from inputloop import inputloop

from scoreboard import values as scoreboard_values

# Methods
def start():
    """Starts the entire thing and gets things ready"""
    cmdline('cls')

    print("Welcome to Kickball Scoreboard!\nYou will need to read the README file to understand this well")
    inp = inputloop("Start how?", ':', 'options', ('p', 'n', 'f'))

    if inp == 'p':
        _preset()

    return scoreboard_values


def __preset():
    """Start from an already started game"""

    # Team names
    scoreboard_values.team1 = inputloop("First team", ':', 'len', (2, 3)).capitalize()
    scoreboard_values.team2 = inputloop("Second team", ':', 'len', (2, 3)).capitalize()

    # Scores
    scoreboard_values.score1 = inputloop(f"{scoreboard_values.team1}'s score", ':', 'int', ('>=', 0))
    scoreboard_values.score2 = inputloop(f"{scoreboard_values.team2}'s score", ':', 'int', ('>=', 0))

    # Innings
    scoreboard_values.inning_num = inputloop("Inning", ':', 'int', ('>=', 1))
    inp = inputloop("Inning part", ':', 'options', ('t', 'm', 'b', 'e'))
    if inp == 't':
        scoreboard_values.inning_part = 1
    elif inp == 'm':
        scoreboard_values.inning_part = 2
    elif inp == 'b':
        scoreboard_values.inning_part = 3
    elif inp == 'e':
        scoreboard_values.inning_part = 4
    
    if scoreboard_values.inning_part in (2, 4):
        return
    
    # Balls, strikes, fouls, and outs
    scoreboard_values.balls = inputloop("Balls", ':', 'range', (0, 3))
    scoreboard_values.strikes = inputloop("Strikes", ':', 'range', (0, 2))
    scoreboard_values.fouls = inputloop("Fouls", ':', 'range', (0, 3))
    scoreboard_values.outs = inputloop("Outs", ':', 'range', (0, 2))

    # Bases
    inp = inputloop("Base 1", ':', 'options', ('y', 'n'))
    if inp == 'y':
        scoreboard_values.b1 = True
    inp = inputloop("Base 2", ':', 'options', ('y', 'n'))
    if inp == 'y':
        scoreboard_values.b2 = True
    inp = inputloop("Base 3", ':', 'options', ('y', 'n'))
    if inp == 'y':
        scoreboard.values.b3 = True