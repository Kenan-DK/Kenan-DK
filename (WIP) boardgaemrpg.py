import random

class character():
    name = ""
    weapon = ""
    maxHP = 20
    HP = 20
    Attack = 20
    Magic = 20
    Defense = 20
    skills = [["", power], ["", power], ["", power]]
    items = []
    coins = 0


def item_space():
    if len(items) >= 0 and coins >= 10:
        randitem = random.randint(1,5)
        coins = coins - 10

        if randitem == 1:
            item = "Potion"
            items.append(item)

        elif randitem == 2:
            item = "Bolt-in-a-Bottle"
            items.append(item)

        elif randitem == 3:
            item = "Great Potion"
            items.append(item)

        elif randitem == 4:
            item = "Master Potion"
            items.append(item)

        elif randitem == 5:
            item = "Drain Vial"
            items.append(item)
            

    elif len(items) == 3:
        print("You have no room for items")




def chance_space():
    wheel = random.randint(1,5)
    if wheel == 1:
        coins = coins + 5

    elif wheel == 2:
        coins = coins + 10

    elif wheel == 3:
        HP = HP + (maxHP // 2)

    elif wheel == 4:
        item = "Potion"
        items.append(item)

    elif wheel == 5:
        coins = coins - 5

    


def dojo_space():
    if len(skills) == 3:
        print("You can't learn anything new")

    else:
        newskill = random.randint(1,8)

        if newskill == 1:
            skill = "Slash"
            power = 30

        elif newskill == 2:
            skill = "Dual Slash"
            power = 40

        elif newskill == 3:
            skill = "Mighty Slash"
            power = 60

        elif newskill == 4:
            skill = "Ember"
            power = 35

        elif newskill == 5:
            skill = "Flare"
            power = 50

        elif newskill == 6:
            skill = "Blaze"
            power = 80

        elif newskill == 7:
            skill = "Magic Blade"
            power = 90




def reg_space():
    coins = coins + 3




def board_game():
    board = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11",
             "12", "13", "14", "15", "16", "17", "18", "19", "20", "21", "22", "23",
             "24", "25", "26", "27", "28", "29", "30", "31", "32", "34", "35", "36",
             "37", "38", "39", "40", "41", "42", "43", "44", "45", "46", "47", "48",
             "49", "50", "51", "52", "53", "54", "55", "56", "57", "58", "59", "60",]

    chance = [3, 11, 18, 28, 34, 41, 52]
    enemy = [2, 8, 10, 12, 15, 17, 21, 26, 33, 37, 42, 45, 48, 49, 53, 57]
    dojo = [7, 13, 20, 22, 31, 44, 54]
    item = [5, 16, 20, 25, 32, 38, 43, 51, 56]

    player_space = board[0]
    dice = [1, 2, 3, 4, 5, 6]
    dicex = [2, 2, 3, 4, 1, 1]
    items = []
    turn = 1

    while player_space != board[61]:
        die = input("which dice?""\n""Dice (d)""\n""Dice EX (x)""\n")

        if die == "d":
            roll = random.randint(1,6)
            player_space = player_space + dice[roll]

        elif die == "x":
            roll = random.randint(1,6)
            player_space = player_space + dicex[roll]

        print(player_space)

        if player_space in chance:
            print("Chance Time!")

        elif player_space in enemy:
            print("Enemy Time!")

        elif player_space in dojo:
            print("Dojo Time!")

        elif player_space in item:
            print("Item Time")



    

    




    
