# main.py
# The main file for this mess


# Imports
from global_methods import *

import scoreboard
from start import start

scoreboard.values = start()

while True: # Main loop
    clear_console()
    scoreboard.display()
    inp = input()