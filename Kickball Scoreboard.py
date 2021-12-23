#imports
from os import system


#deffinitions
class scoreboard_values: #holds the values of the scoreboard and methods that use them
    team1 = ""
    team2 = ""
    score1 = 0
    score2 = 0
    inning_num = 0
    inning_part = 0
    balls = 0
    strikes = 0
    fouls = 0
    outs = 0
    b1 = False
    b2 = False
    b3 = False
    
    def format():
        if len(scoreboard_values.team1) == 2: #for 2 letter team names
            scoreboard_display_values.team1 = " " + scoreboard_values.team1
        else:
            scoreboard_display_values.team1 = scoreboard_values.team1

        if len(scoreboard_values.team2) == 2: #for 2 letter team names
            scoreboard_display_values.team2 = " " + scoreboard_values.team2
        else:
            scoreboard_display_values.team2 = scoreboard_values.team2

        if scoreboard_values.score1 < 10: #for scores less than 10
            scoreboard_display_values.score1 = str(scoreboard_values.score1) + " "
        else:
            scoreboard_display_values.score1 = str(scoreboard_values.score1)
        if scoreboard_values.score2 < 10: #for scores less than 10
            scoreboard_display_values.score2 = str(scoreboard_values.score2) + " "
        else:
            scoreboard_display_values.score2 = str(scoreboard_values.score2)

        if scoreboard_values.inning_num < 10: #for inning_nums less than 10
            scoreboard_display_values.inning_num = str(scoreboard_values.inning_num) + " "
        else:
            scoreboard_display_values.inning_num = str(scoreboard_values.inning_num)

        if scoreboard_values.inning_part == 0:
            scoreboard_display_values.inning_part = "Pre"
        elif scoreboard_values.inning_part == 1:
            scoreboard_display_values.inning_part = "Top"
        elif scoreboard_values.inning_part == 2:
            scoreboard_display_values.inning_part = "Mid"
        elif scoreboard_values.inning_part == 3:
            scoreboard_display_values.inning_part = "Bot"
        elif scoreboard_values.inning_part == 4:
            scoreboard_display_values.inning_part = "End"

        scoreboard_display_values.balls = str(scoreboard_values.balls) #for balls, strikes and fouls
        scoreboard_display_values.strikes = str(scoreboard_values.strikes)
        scoreboard_display_values.fouls = str(scoreboard_values.fouls)

        scoreboard_display_values.outs = "" #for outs
        for i in range(scoreboard_values.outs):
            scoreboard_display_values.outs += "● "
        while len(scoreboard_display_values.outs) < 5:
            scoreboard_display_values.outs += "○ "
        scoreboard_display_values.outs = scoreboard_display_values.outs[0:5]

        if scoreboard_values.b1: #for b1
            scoreboard_display_values.b1 = "●"
        else:
            scoreboard_display_values.b1 = "○"
        if scoreboard_values.b2: #for b2
            scoreboard_display_values.b2 = "●"
        else:
            scoreboard_display_values.b2 = "○"
        if scoreboard_values.b3: #for b3
            scoreboard_display_values.b3 = "●"
        else:
            scoreboard_display_values.b3 = "○"
    
    def save():
        txt = "{} vs {}.txt"
        file = open(txt.format(scoreboard_values.team1, scoreboard_values.team2), "w")
        file.write("")
        file.close()

        file = open(txt.format(scoreboard_values.team1, scoreboard_values.team2), "a")
        file.write(str(scoreboard_values.team1) + "\n")
        file.write(str(scoreboard_values.team2) + "\n")
        file.write(str(scoreboard_values.score1) + "\n")
        file.write(str(scoreboard_values.score2) + "\n")
        file.write(str(scoreboard_values.inning_num) + "\n")
        file.write(str(scoreboard_values.inning_part) + "\n")
        file.write(str(scoreboard_values.balls) + "\n")
        file.write(str(scoreboard_values.strikes) + "\n")
        file.write(str(scoreboard_values.fouls) + "\n")
        file.write(str(scoreboard_values.outs) + "\n")
        file.write(str(scoreboard_values.b1) + "\n")
        file.write(str(scoreboard_values.b2) + "\n")
        file.write(str(scoreboard_values.b3) + "\n")
        file.close()
        exit()


class scoreboard_display_values: #holds the values that will get displayed and the methods that use them
    team1 = ""
    team2 = ""
    score1 = 0
    score2 = 0
    inning_num = 0
    inning_part = "pre"
    balls = 0
    strikes = 0
    fouls = 0
    outs = 0
    b1 = False
    b2 = False
    b3 = False
    
    def display():
        system("cls")
        txt = "┏━━━━━━━┯━━━━━┯━━━━━┯━━━┓\n┃{}: {}│{}-{}-{}│  {}  │{}┃\n┃{}: {}│{}│{}   {}│ {}┃\n┗━━━━━━━┷━━━━━┷━━━━━┷━━━┛"
        print(
            txt.format(
                scoreboard_display_values.team1,
                scoreboard_display_values.score1,
                scoreboard_display_values.balls,
                scoreboard_display_values.strikes,
                scoreboard_display_values.fouls,
                scoreboard_display_values.b2,
                scoreboard_display_values.inning_part,
                scoreboard_display_values.team2,
                scoreboard_display_values.score2,
                scoreboard_display_values.outs,
                scoreboard_display_values.b3,
                scoreboard_display_values.b1,
                scoreboard_display_values.inning_num,
            )
        )


class start: #methods for initial start
    def preset():
        inp = input("First team: ") #first team
        if len(inp) not in [2, 3]:
            raise ValueError("Expected length of 2 or 3")
        scoreboard_values.team1 = inp.capitalize()

        inp = input("Second team: ") #second team
        if len(inp) not in [2, 3]:
            raise ValueError("Expected length of 2 or 3")
        scoreboard_values.team2 = inp.capitalize()

        txt = "{}'s Score: " #first team's score
        inp = int(input(txt.format(scoreboard_values.team1)))
        scoreboard_values.score1 = inp

        txt = "{}'s Score: " #second team's score
        inp = int(input(txt.format(scoreboard_values.team2)))
        scoreboard_values.score2 = inp

        inp = int(input("Inning: ")) #inning
        scoreboard_values.inning_num = inp

        inp = input("'Top', 'Mid', 'Bot', or 'End': ") #part of inning
        if inp == "Top":
            scoreboard_values.inning_part = 1
        elif inp == "Mid":
            scoreboard_values.inning_part = 2
        elif inp == "Bot":
            scoreboard_values.inning_part = 3
        elif inp == "End":
            scoreboard_values.inning_part = 4
        else:
            raise ValueError("Expected 'Top', 'Mid', 'Bot', or 'End'")

        if scoreboard_values.inning_part in [1, 3]:
            inp = int(input("Balls: ")) #balls
            scoreboard_values.balls = inp

            inp = int(input("Strikes: ")) #strikes
            scoreboard_values.strikes = inp

            inp = int(input("Fouls: ")) #fouls
            scoreboard_values.fouls = inp

            inp = int(input("Outs: ")) #outs
            scoreboard_values.outs = inp

            inp = input("Runner on 1st (y/n)? ") #base 1
            if inp == "y":
                scoreboard_values.b1 = True
            elif inp == "n":
                scoreboard_values.b1 = False
            else:
                raise ValueError("Expexted y/n")

            inp = input("Runner on 2nd (y/n)? ") #base 2
            if inp == "y":
                scoreboard_values.b2 = True
            elif inp == "n":
                scoreboard_values.b2 = False
            else:
                raise ValueError("Expexted y/n")

            inp = input("Runner on 3rd (y/n)? ") #base 3
            if inp == "y":
                scoreboard_values.b3 = True
            elif inp == "n":
                scoreboard_values.b3 = False
            else:
                raise ValueError("Expexted y/n")

    def file():
        inp = input("First team: ") #first team
        if len(inp) not in [2, 3]:
            raise ValueError("Expected length of 2 or 3")
        txt = inp.capitalize()
        txt += " vs "
    
        inp = input("Second team: ") #second team
        if len(inp) not in [2, 3]:
            raise ValueError("Expected length of 2 or 3")
        txt += inp.capitalize()
        txt += ".txt"
        try:
            file = open(txt, "r")
        except:
            raise FileNotFoundError("Saved game not found. Did you put in the wrong teams?")
        scoreboard_values.team1 = file.readline().strip("\n")
        scoreboard_values.team2 = file.readline().strip("\n")
        scoreboard_values.score1 = int(file.readline())
        scoreboard_values.score2 = int(file.readline())
        scoreboard_values.inning_num = int(file.readline())
        scoreboard_values.inning_part = int(file.readline())
        scoreboard_values.balls = int(file.readline())
        scoreboard_values.strikes = int(file.readline())
        scoreboard_values.fouls = int(file.readline())
        scoreboard_values.outs = int(file.readline())
        scoreboard_values.b1 = bool(file.readline())
        scoreboard_values.b2 = bool(file.readline())
        scoreboard_values.b3 = bool(file.readline())
        file.close()

    def new():
        inp = input("First team: ") #first team
        if len(inp) not in [2, 3]:
            raise ValueError("Expected length of 2 or 3")
        scoreboard_values.team1 = inp.capitalize()

        inp = input("Second team: ") #second team
        if len(inp) not in [2, 3]:
            raise ValueError("Expected length of 2 or 3")
        scoreboard_values.team2 = inp.capitalize()


class change: #methods for changing a scoreboard value
    def get(inp):
        if scoreboard_values.inning_part not in [1, 3,]: #checks if the inning is not in play
            if inp == "a":
                if scoreboard_values.inning_num == 0: #start the game
                    scoreboard_values.inning_part = 1
                    scoreboard_values.inning_num = 1
                elif scoreboard_values.inning_part in [2, 4]: #advance the inning
                    scoreboard_values.inning_part += 1
                    change.process("advance_inning")
            elif inp == "e": #exit
                inp = input("Exit? (y to confirm): ")
                if inp == "y":
                    exit()
                else:
                    return

            return
        if inp == "s": #strike
            scoreboard_values.strikes += 1
            change.process("strikes")

        elif inp == "b": #ball
            scoreboard_values.balls += 1
            change.process("balls")

        elif inp == "f":
            scoreboard_values.fouls += 1
            if scoreboard_values.strikes < 2:
                scoreboard_values.strikes += 1
            change.process("fouls")

        elif inp == "o": #out
            scoreboard_values.outs += 1
            change.process("outs")

        elif inp == "hr": #homerun
            change.process("homerun")

        elif inp == "ba": #runner moved
            change.process("base_advancement")

        elif inp == "e": #exit
            inp = input("Exit? (y to confirm): ")
            if inp == "y":
                change.process("end")
            else:
                return
        else:
            return    
    def process(change):
        if change == "strikes": #strike
            if scoreboard_values.strikes == 3:
                scoreboard_values.outs += 1
                change.process("outs")

        elif change == "balls": #ball
            if scoreboard_values.balls == 4:
                scoreboard_values.balls = 0
                change.process("walk")

        elif change == "fouls":
            if scoreboard_values.fouls == 4:
                scoreboard_values.outs += 1
                change.process("outs")

        elif change == "outs": #out
            scoreboard_values.balls = 0
            scoreboard_values.strikes = 0
            scoreboard_values.fouls = 0
            if scoreboard_values.outs == 3:
                scoreboard_values.inning_part += 1
                change.process("advance_inning")

        elif change == "homerun": #homerun
            temp = 1
            if scoreboard_values.b1:
                temp += 1
            if scoreboard_values.b2:
                temp += 1
            if scoreboard_values.b3:
                temp += 1
            add_score(temp)
            scoreboard_values.b1 = False
            scoreboard_values.b2 = False
            scoreboard_values.b3 = False
            scoreboard_values.balls = 0
            scoreboard_values.strikes = 0

        elif change == "base_advancement": #runner moved
            inp = input()
            if inp == "0":
                inp = input()
                if inp == "1":
                    if not (scoreboard_values.b1):
                        scoreboard_values.b1 = True
                elif inp == "2":
                    if not (scoreboard_values.b1 or scoreboard_values.b2):
                        scoreboard_values.b2 = True
                elif inp == "3":
                    if not (scoreboard_values.b1 or scoreboard_values.b2 or scoreboard_values.b3):
                        scoreboard_values.b3 = True
                elif inp == "4":
                    if not (scoreboard_values.b1 or scoreboard_values.b2 or scoreboard_values.b3):
                        add_score(1)
                else:
                    return
                scoreboard_values.balls = 0
                scoreboard_values.strikes = 0
                scoreboard_values.fouls = 0

            elif inp == "1":
                if not (scoreboard_values.b1):
                    return
                inp = input()
                if inp == "2":
                    if not (scoreboard_values.b2):
                        scoreboard_values.b2 = True
                elif inp == "3":
                    if not (scoreboard_values.b2 or scoreboard_values.b3):
                        scoreboard_values.b3 = True
                elif inp == "4":
                    if not (scoreboard_values.b2 or scoreboard_values.b3):
                        add_score(1)
                elif inp == "!":
                    scoreboard_values.b1 = False
                    scoreboard_values.outs += 1
                    change.process("outs")
                else:
                    return
                scoreboard_values.b1 = False

            elif inp == "2":
                if not (scoreboard_values.b2):
                    return
                inp = input()
                if inp == "3":
                    if not (scoreboard_values.b3):
                        scoreboard_values.b3 = True
                elif inp == "4":
                    if not (scoreboard_values.b3):
                        add_score(1)
                elif inp == "!":
                    scoreboard_values.b1 = False
                    scoreboard_values.outs += 1
                    change.process("outs")
                else:
                    return
                scoreboard_values.b2 = False

            elif inp == "3":
                if not (scoreboard_values.b3):
                    return
                inp = input()
                if inp == "4":
                    add_score(1)
                elif inp == "!":
                    scoreboard_values.b1 = False
                    scoreboard_values.outs += 1
                    change.process("outs")
                else:
                    return
                scoreboard_values.b3 = False

        elif change == "advance_inning": #advance the inning
            scoreboard_values.b1 = False
            scoreboard_values.b2 = False
            scoreboard_values.b3 = False
            if scoreboard_values.inning_part == 5:
                scoreboard_values.inning_part = 1
                scoreboard_values.inning_num += 1

        elif change == "end":
            inp = input("Save game to file to continue later? ")
            if inp == "y":
                scoreboard_values.save()
            elif inp == "n":
                scoreboard_values.format()
                scoreboard_display_values.display()
                if scoreboard_values.inning_part in [1, 2]:
                    if scoreboard_values.score1 >= scoreboard_values.score2:
                        txt = "{} needs to kick before teams' plays can be even. End anyway? "
                        inp = input(txt.format(scoreboard_values.team2))
                        if inp == "y":
                            pass
                        else:
                            return

                txt = "Final. {} wins."
                if scoreboard_values.score1 > scoreboard_values.score2:
                    print(txt.format(scoreboard_values.team1))
                elif scoreboard_values.score2 > scoreboard_values.score1:
                    print(txt.format(scoreboard_values.team2))
                else:
                    print("Final. Tie.")
                exit()
            else:
                return


def add_score(value): #add the score to the team
    if scoreboard_values.inning_part == 1:
        scoreboard_values.score1 += value
    elif scoreboard_values.inning_part == 3:
        scoreboard_values.score2 += value


inp = input("Start game from where (p/f/n)? ")

if inp == "p":
    start.preset()
elif inp == "f":
    start.file()
elif inp == "n":
    start.new()
else:
    raise ValueError("Expected p/f/n")

while True:
    scoreboard_values.format()
    scoreboard_display_values.display()
    inp = input()
    change.get(inp)