def preset_start():
    inp = input("First team: ") #first team
    if len(inp) not in [2, 3]:
        raise ValueError("Expected length of 2 or 3")
    scoreboard_values["team1"] = inp.capitalize()

    inp = input("Second team: ") #second team
    if len(inp) not in [2, 3]:
        raise ValueError("Expected length of 2 or 3")
    scoreboard_values["team2"] = inp.capitalize()

    txt = "{}'s Score: " #first team's score
    inp = int(input(txt.format(scoreboard_values["team1"])))
    scoreboard_values["score1"] = inp

    txt = "{}'s Score: " #second team's score
    inp = int(input(txt.format(scoreboard_values["team2"])))
    scoreboard_values["score2"] = inp

    inp = int(input("Inning: ")) #inning
    scoreboard_values["inning_num"] = inp

    inp = input("'Top', 'Mid', 'Bot', or 'End': ") #part of inning
    if inp == "Top":
        scoreboard_values["inning_part"] = 1
    elif inp == "Mid":
        scoreboard_values["inning_part"] = 2
    elif inp == "Bot":
        scoreboard_values["inning_part"] = 3
    elif inp == "End":
        scoreboard_values["inning_part"] = 4
    else:
        raise ValueError("Expected 'Top', 'Mid', 'Bot', or 'End'")

    if scoreboard_values["inning_part"] in [1, 3]:
        inp = int(input("Balls: ")) #balls
        scoreboard_values["balls"] = inp

        inp = int(input("Strikes: ")) #strikes
        scoreboard_values["strikes"] = inp

        inp = int(input("Fouls: ")) #fouls
        scoreboard_values["fouls"] = inp

        inp = int(input("Outs: ")) #outs
        scoreboard_values["outs"] = inp

        inp = input("Runner on 1st? ") #base 1
        if inp == "y":
            scoreboard_values["b1"] = True
        elif inp == "n":
            scoreboard_values["b1"] = False
        else:
            raise ValueError("Expexted 'Yes' or 'No'")

        inp = input("Runner on 2nd? ") #base 2
        if inp == "y":
            scoreboard_values["b2"] = True
        elif inp == "n":
            scoreboard_values["b2"] = False
        else:
            raise ValueError("Expexted 'Yes' or 'No'")

        inp = input("Runner on 3rd? ") #base 3
        if inp == "y":
            scoreboard_values["b3"] = True
        elif inp == "n":
            scoreboard_values["b3"] = False
        else:
            raise ValueError("Expexted 'Yes' or 'No'")
    else:
        scoreboard_values["balls"] = 0
        scoreboard_values["strikes"] = 0
        scoreboard_values["fouls"] = 0
        scoreboard_values["outs"] = 0
        scoreboard_values["b1"] = False
        scoreboard_values["b2"] = False
        scoreboard_values["b3"] = False


def new_start():
    inp = input("First team: ") #first team
    if len(inp) not in [2, 3]:
        raise ValueError("Expected length of 2 or 3")
    scoreboard_values["team1"] = inp.capitalize()

    inp = input("Second team: ") #second team
    if len(inp) not in [2, 3]:
        raise ValueError("Expected length of 2 or 3")
    scoreboard_values["team2"] = inp.capitalize()

    scoreboard_values["score1"] = 0
    scoreboard_values["score2"] = 0
    scoreboard_values["inning_num"] = 0
    scoreboard_values["inning_part"] = 0
    scoreboard_values["balls"] = 0
    scoreboard_values["strikes"] = 0
    scoreboard_values["fouls"] = 0
    scoreboard_values["outs"] = 0
    scoreboard_values["b1"] = False
    scoreboard_values["b2"] = False
    scoreboard_values["b3"] = False


def format_scoreboard_values():
    if len(scoreboard_values["team1"]) == 2: #for 2 letter team names
        scoreboard_display_values["team1"] = " " + scoreboard_values["team1"]
    else:
        scoreboard_display_values["team1"] = scoreboard_values["team1"]

    if len(scoreboard_values["team2"]) == 2: #for 2 letter team names
        scoreboard_display_values["team2"] = " " + scoreboard_values["team2"]
    else:
        scoreboard_display_values["team2"] = scoreboard_values["team2"]

    if scoreboard_values["score1"] < 10: #for scores less than 10
        scoreboard_display_values["score1"] = str(scoreboard_values["score1"]) + " "
    else:
        scoreboard_display_values["score1"] = str(scoreboard_values["score1"])
    if scoreboard_values["score2"] < 10: #for scores less than 10
        scoreboard_display_values["score2"] = str(scoreboard_values["score2"]) + " "
    else:
        scoreboard_display_values["score2"] = str(scoreboard_values["score2"])

    if scoreboard_values["inning_num"] < 10: #for inning_nums less than 10
        scoreboard_display_values["inning_num"] = str(scoreboard_values["inning_num"]) + " "
    else:
        scoreboard_display_values["inning_num"] = str(scoreboard_values["inning_num"])

    if scoreboard_values["inning_part"] == 0:
        scoreboard_display_values["inning_part"] = "Pre"
    elif scoreboard_values["inning_part"] == 1:
        scoreboard_display_values["inning_part"] = "Top"
    elif scoreboard_values["inning_part"] == 2:
        scoreboard_display_values["inning_part"] = "Mid"
    elif scoreboard_values["inning_part"] == 3:
        scoreboard_display_values["inning_part"] = "Bot"
    elif scoreboard_values["inning_part"] == 4:
        scoreboard_display_values["inning_part"] = "End"

    scoreboard_display_values["balls"] = str(scoreboard_values["balls"]) #for balls, strikes and fouls
    scoreboard_display_values["strikes"] = str(scoreboard_values["strikes"])
    scoreboard_display_values["fouls"] = str(scoreboard_values["fouls"])

    scoreboard_display_values["outs"] = "" #for outs
    for i in range(scoreboard_values["outs"]):
        scoreboard_display_values["outs"] += "● "
    while len(scoreboard_display_values["outs"]) < 5:
        scoreboard_display_values["outs"] += "○ "
    scoreboard_display_values["outs"] = scoreboard_display_values["outs"][0:5]

    if scoreboard_values["b1"]: #for b1
        scoreboard_display_values["b1"] = "●"
    else:
        scoreboard_display_values["b1"] = "○"
    if scoreboard_values["b2"]: #for b2
        scoreboard_display_values["b2"] = "●"
    else:
        scoreboard_display_values["b2"] = "○"
    if scoreboard_values["b3"]: #for b3
        scoreboard_display_values["b3"] = "●"
    else:
        scoreboard_display_values["b3"] = "○"


def display_scoreboard(): #reprint the scoreboard
    txt = "┏━━━━━━━┯━━━━━┯━━━━━┯━━━┓\n┃{}: {}│{}-{}-{}│  {}  │{}┃\n┃{}: {}│{}│{}   {}│ {}┃\n┗━━━━━━━┷━━━━━┷━━━━━┷━━━┛"
    print(
        txt.format(
            scoreboard_display_values["team1"],
            scoreboard_display_values["score1"],
            scoreboard_display_values["balls"],
            scoreboard_display_values["strikes"],
            scoreboard_display_values["fouls"],
            scoreboard_display_values["b2"],
            scoreboard_display_values["inning_part"],
            scoreboard_display_values["team2"],
            scoreboard_display_values["score2"],
            scoreboard_display_values["outs"],
            scoreboard_display_values["b3"],
            scoreboard_display_values["b1"],
            scoreboard_display_values["inning_num"],
        )
    )


def get_user_change(param): #inspect the user input and do an according action
    if scoreboard_values["inning_part"] not in [1, 3,]: #checks if the inning is not in play
        if param == "a":
            if scoreboard_values["inning_num"] == 0: #start the game
                scoreboard_values["inning_part"] = 1
                scoreboard_values["inning_num"] = 1
            elif scoreboard_values["inning_part"] in [2, 4]: #advance the inning
                scoreboard_values["inning_part"] += 1
                process_change("advance_inning")
        elif param == "e": #exit
            inp = input("Exit? (y to confirm): ")
            if inp == "y":
                exit()
            else:
                return

        return
    if param == "s": #strike
        scoreboard_values["strikes"] += 1
        process_change("strikes")

    elif param == "b": #ball
        scoreboard_values["balls"] += 1
        process_change("balls")

    elif param == "f":
        scoreboard_values["fouls"] += 1
        if scoreboard_values["strikes"] < 2:
            scoreboard_values["strikes"] += 1
        process_change("fouls")

    elif param == "o": #out
        scoreboard_values["outs"] += 1
        process_change("outs")

    elif param == "hr": #homerun
        process_change("homerun")

    elif param == "ba": #runner moved
        process_change("base_advancement")

    elif param == "e": #exit
        inp = input("Exit? (y to confirm): ")
        if inp == "y":
            process_change("end")
        else:
            return
    else:
        return


def process_change(change):
    if change == "strikes": #strike
        if scoreboard_values["strikes"] == 3:
            scoreboard_values["outs"] += 1
            process_change("outs")

    elif change == "balls": #ball
        if scoreboard_values["balls"] == 4:
            scoreboard_values["balls"] = 0
            process_change("walk")

    elif change == "fouls":
        if scoreboard_values["fouls"] == 4:
            scoreboard_values["outs"] += 1
            process_change("outs")

    elif change == "outs": #out
        scoreboard_values["balls"] = 0
        scoreboard_values["strikes"] = 0
        scoreboard_values["fouls"] = 0
        if scoreboard_values["outs"] == 3:
            scoreboard_values["inning_part"] += 1
            process_change("advance_inning")

    elif change == "homerun": #homerun
        temp = 1
        if scoreboard_values["b1"]:
            temp += 1
        if scoreboard_values["b2"]:
            temp += 1
        if scoreboard_values["b3"]:
            temp += 1
        add_score(temp)
        scoreboard_values["b1"] = False
        scoreboard_values["b2"] = False
        scoreboard_values["b3"] = False
        scoreboard_values["balls"] = 0
        scoreboard_values["strikes"] = 0

    elif change == "base_advancement": #runner moved
        inp = input()
        if inp == "0":
            inp = input()
            if inp == "1":
                if not (scoreboard_values["b1"]):
                    scoreboard_values["b1"] = True
            elif inp == "2":
                if not (scoreboard_values["b1"] or scoreboard_values["b2"]):
                    scoreboard_values["b2"] = True
            elif inp == "3":
                if not (scoreboard_values["b1"] or scoreboard_values["b2"] or scoreboard_values["b3"]):
                    scoreboard_values["b3"] = True
            elif inp == "4":
                if not (scoreboard_values["b1"] or scoreboard_values["b2"] or scoreboard_values["b3"]):
                    add_score(1)
            else:
                return
            scoreboard_values["balls"] = 0
            scoreboard_values["strikes"] = 0
            scoreboard_values["fouls"] = 0

        elif inp == "1":
            if not (scoreboard_values["b1"]):
                return
            inp = input()
            if inp == "2":
                if not (scoreboard_values["b2"]):
                    scoreboard_values["b2"] = True
            elif inp == "3":
                if not (scoreboard_values["b2"] or scoreboard_values["b3"]):
                    scoreboard_values["b3"] = True
            elif inp == "4":
                if not (scoreboard_values["b2"] or scoreboard_values["b3"]):
                    add_score(1)
            elif inp == "!":
                scoreboard_values["b1"] = False
                scoreboard_values["outs"] += 1
                process_change("outs")
            else:
                return
            scoreboard_values["b1"] = False

        elif inp == "2":
            if not (scoreboard_values["b2"]):
                return
            inp = input()
            if inp == "3":
                if not (scoreboard_values["b3"]):
                    scoreboard_values["b3"] = True
            elif inp == "4":
                if not (scoreboard_values["b3"]):
                    add_score(1)
            elif inp == "!":
                scoreboard_values["b1"] = False
                scoreboard_values["outs"] += 1
                process_change("outs")
            else:
                return
            scoreboard_values["b2"] = False

        elif inp == "3":
            if not (scoreboard_values["b3"]):
                return
            inp = input()
            if inp == "4":
                add_score(1)
            elif inp == "!":
                scoreboard_values["b1"] = False
                scoreboard_values["outs"] += 1
                process_change("outs")
            else:
                return
            scoreboard_values["b3"] = False

    elif change == "advance_inning": #advance the inning
        scoreboard_values["b1"] = False
        scoreboard_values["b2"] = False
        scoreboard_values["b3"] = False
        if scoreboard_values["inning_part"] == 5:
            scoreboard_values["inning_part"] = 1
            scoreboard_values["inning_num"] += 1

    elif change == "end":
        inp = input("Save game to file to continue later? ")
        if inp == "y":
            txt = "{} vs {}.txt"
            file = open(txt.format(scoreboard_values["team1"], scoreboard_values["team2"]), "w")
            file.write(str(scoreboard_values))
            file.close()
            exit()
        elif inp == "n":
            format_scoreboard_values()
            display_scoreboard()
            if scoreboard_values["inning_part"] in [1, 2]:
                if scoreboard_values["score1"] >= scoreboard_values["score2"]:
                    txt = "{} needs to kick before teams' plays can be even. End anyway? "
                    inp = input(txt.format(scoreboard_values["team2"]))
                    if inp == "y":
                        pass
                    else:
                        return
            
            txt = "Final. {} wins."
            if scoreboard_values["score1"] > scoreboard_values["score2"]:
                print(txt.format(scoreboard_values["team1"]))
            elif scoreboard_values["score2"] > scoreboard_values["score1"]:
                print(txt.format(scoreboard_values["team2"]))
            else:
                print("Final. Tie.")
            exit()
        else:
            return


def add_score(value): #add the score to the team
    if scoreboard_values["inning_part"] == 1:
        scoreboard_values["score1"] += value
    elif scoreboard_values["inning_part"] == 3:
        scoreboard_values["score2"] += value


scoreboard_values = {}
scoreboard_display_values = {}
inp = input("Start game from where? (p/f/n)? ")

if inp == "p":
    preset_start()
elif inp == "f":
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
    txt = file.read()
    scoreboard_values = eval(txt)
    file.close()
elif inp == "n":
    new_start()
else:
    raise ValueError("Expected p, f, or n")

while True:
    format_scoreboard_values()
    display_scoreboard()
    inp = input()
    get_user_change(inp)
