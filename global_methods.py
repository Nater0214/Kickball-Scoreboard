# global_methods.py
# Functions that a lot of the scripts use
# I put them here so I only have to define them once


# Imports
from os import system as cmdline


# Methods
clear_console = lambda: cmdline('cls')