# scoreboard.py
# Methods and variables for the scoreboard


# Values
class __Values:
    """Values for the scoreboard"""
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

values = __Values()


class __DisplayValues:
    """Values that will actually be displayed to the user"""
    # I put a bunch of placeholders here lol
    team1 = "Lol"
    team2 = " Ez"

    score1 = "69"
    score2 = "4 "

    inning_num = " 0"
    inning_part = "Pre"

    balls = "0"
    strikes = "0"
    fouls = "0"

    o1 = "○"
    o2 = "●"
    o3 = "○"

    b1 = "○"
    b2 = "●"
    b3 = "○"

display_values = __DisplayValues()


def display():
    __format()
    print(f"┌───────┬─────┬─────┐\n│{display_values.team1}: {display_values.score1}│{display_values.balls}-{display_values.strikes}-{display_values.fouls}│  {display_values.b2}  │\n│{display_values.team2}: {display_values.score2}│{display_values.o1} {display_values.o2} {display_values.o3}│{display_values.b3}   {display_values.b1}│\n└───────┴─────┴─────┘")


def __format():
    # Team Names
    if len(values.team1) == 2:
        display_values.team1 = f" {values.team1}"
    else:
        display_values.team1 = values.team1

    if len(values.team2) == 2:
        display_values.team2 = f" {values.team2}"
    else:
        display_values.team2 = values.team2
    
    # Scores
    display_values.score1 = str(values.score1)
    if len(display_values.score1) == 1:
        display_values.score1 = f"{display_values.score1} "
    
    display_values.score2 = str(values.score2)
    if len(display_values.score2) == 1:
        display_values.score2 = f"{display_values.score2} "
    
    # Inning num and part
    display_values.inning_num = str(values.inning_num)
    if len(display_values.inning_num) == 1:
        display_values.inning_num = f" {display_values.inning_num}"
    
    if values.inning_part == 0:
        display_values.inning_part = "Pre"
    elif values.inning_part == 1:
        display_values.inning_part = "Top"
    elif values.inning_part == 2:
        display_values.inning_part = "Mid"
    elif values.inning_part == 3:
        display_values.inning_part = "Bot"
    elif values.inning_part == 4:
        display_values.inning_part = "End"
    
    # Balls, Strikes, & Fouls
    display_values.balls = str(values.balls)
    display_values.strikes = str(values.strikes)
    display_values.fouls = str(values.fouls)

    # Outs
    if values.outs >= 1:
        display_values.o1 = "●"
    else:
        display_values.o1 = "○"

    if values.outs >= 2:
        display_values.o2 = "●"
    else:
        display_values.o2 = "○"

    if values.outs >= 3:
        display_values.o3 = "●"
    else:
        display_values.o3 = "○"

    # Bases
    if values.b1:
        display_values.b1 = "●"
    else:
        display_values.b1 = "○"

    if values.b2:
        display_values.b2 = "●"
    else:
        display_values.b2 = "○"

    if values.b3:
        display_values.b3 = "●"
    else:
        display_values.b3 = "○"