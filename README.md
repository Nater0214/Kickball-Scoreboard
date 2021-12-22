# Kickball Scoreboard
This is a simple (not simple) program that displays a kickball scoreboard, the original being in console, and version 2 being in a gui (I'm still working on this one.)
**This uses standard FAST ground rules for plays. This is _not_ a manual on how to play kickball.**

## How to use:
### On startup, the user will be greeted with a prompt.
- p:
  - Preset; For games that have already started.
- f:
  - File; Loads a saved game from a file. (More on this later)
- n:
  - New; Starts a new game.

If none of these options are input, an exception will be raised.

**Note: Team names are expected to be 2 or 3 characters. These names will automatically be capitalized.**

### After filling in all of thses prompts, a scoreboard will be displayed. There is an input waiting for user input. You can put different things in the input to do different things. Here they are:
##### a:
Advance; Advance the inning  
Used to start the game when the new option is used at startup.  
Used in other cases to move from the middle or end of an inning.
##### e:
Exit; Stop the program, giving the user options on what to do.  
After confirming the exit, the user has the choice to save the game to a file, where they can then use the file option on startup to load that game.  
If the user chooses to not save the game to a file, the game will end.  
If it is unfair to the second team, the user will be alerted of this, and have the option to not exit.  
If the user does choose to end the game, the final board will be printed, along with a statement stating who won.

#### All further options can only be used in the top and bottom of an inning

##### s:
Strike; Adds a strike
##### b:
Ball; Adds a ball to the count
##### f:
Foul; Adds a foul to the count
##### o:
Out; Adds an out  
**_Only_ use this for catch-outs, tag, and force-outs where the runner was _not originally on base_. Strikeouts are done automatically, and outs on base are done later.**
##### hr:
Homerun; Scores a homerun  
Adds all points automatically
##### ba:
Base advancement; Advance a runner on base  
After using this option, 2 more blank inputs will follow, assuming the user input correct information. Here are the steps:  
1. Input the starting base. 0 is used for a kicker running after they kicked.
2. Input the destination base. 4 is used for a runner getting home. The points will automatically be added. Use '!' instead to take a runner on the before said base out.

**_Runners can not go over each other. Do the operations with higher numbered bases first._ For example, if runners on 1st and 2nd advanced, advance 2nd to 3rd before advancing 1st to 2nd.**