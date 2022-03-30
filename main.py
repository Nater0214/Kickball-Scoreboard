# main.py
# The main file for this mess


# Imports
import scoreboard
from start import start

scoreboard.values = start()

while True: # Main loop
    scoreboard.display()
    inp = input()