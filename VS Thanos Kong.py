import random

def BossFight():
    Boss_HP = 2000
    Attack_1 = "Jenova Slam"
    Att_1_dmg = 35
    Attack_2 = "Hyper Slash"
    Att_2_dmg = 50
    Attack_3 = "Coconut Gun"
    Att_3_dmg = 60
    Special = "Ancient Meteor"
    special_dmg = 70
    Boss_death = False

    name = "Mario"
    player_HP = 350
    magic_limit = 50
    

    attack = 65
    item1 = "Potion"
    item2 = "Hyper Potion"

    turn = 1

    print("\n""Sephikong Approaches!")


    while Boss_death != True:
        print("\n""Turn", turn)
        
        action = str(input("What would you like to do?" "\n" "Fight (f)" "\n " "Magic (m)" "\n" "Item (i)" "\n" ))

        if action == "f":
            print(name, "used Ground-Pound")
            slash_dmg = attack * 1.5
            Boss_HP = Boss_HP - slash_dmg

        if action == "m":
            if magic_limit <= 0:
                print("You can't use magic!")
            else:     
                materia = str(input("What magic will you use?""\n""Fire (f)""\n""Ice (i)""\n""Tail Slap (t)" ))

                if materia == "f":
                   print(name, "used a Fire Flower")
                   print(name, "Became Fire Mario!")
                   fire_dmg = attack * 2
                   magic_limit = magic_limit - 5
                   Boss_HP = Boss_HP - fire_dmg

                elif materia == "i":
                   print(name, "used an Ice Flower")
                   print(name, "Became Ice Mario!")
                   quake_dmg = (attack * 2) + 5
                   magic_limit = magic_limit - 5
                   Boss_HP = Boss_HP - quake_dmg

                elif materia == "i":
                   print(name, "used a Super leaf")
                   print(name, "Became Tanooki Mario!")
                   quake_dmg = (attack * 1.7)
                   for x in range (2):
                       magic_limit = magic_limit - 5
                       Boss_HP = Boss_HP - quake_dmg
            
                                            
        elif action == "i":
            print(item1, item2)
            item = str(input("select an item""\n""potion (p)""\n""hyper potion (h)"))
            print(item)
            if item == "p":
                print(name, "used a Potion!")
                player_HP = player_HP + 65

            elif item == "h":
                print(name, "used a Hyper Potion!")
                player_HP = player_HP + 100

        
        kagamine_act = random.randint(0,2)
        if kagamine_act == 0:
            print("Kagamine Rin used 1,2 kung fu!")
            RinDMG = (50 * 1.30)
            boss_HP = Boss_HP - RinDMG

            print("Kagamine Len used 1,2 kung fu!")
            LenDMG = (60 * 1.20)
            boss_HP = Boss_HP - LenDMG

        elif kagamine_act == 1:
            print("Kagamine Rin and Kagamine Len used Roadroller Da!")
            KagamineDMG = (70 * 1.20)
            boss_HP = Boss_HP - KagamineDMG

        elif kagamine_act == 2:
            print("Kagamine Rin shared her lemonade!")
            player_HP = player_HP + 30

            print("Kagamine Len shared some of MEIKO's coffee!")
            player_HP = player_HP + 40

            

        boss_action = random.randint(0, 2)
        if boss_action == 0:
            print("Sephikong used", Attack_1)
            player_HP = player_HP - Att_1_dmg

        elif boss_action == 1:
            print("Sephikong used", Attack_2)
            player_HP = player_HP - Att_2_dmg

        elif boss_action == 2:
            print("Sephikong used", Attack_3)
            player_HP = player_HP - Att_3_dmg
            
        if Boss_HP <= (Boss_HP // 2):
            boss_act2 = random.randint(0,2)
            if boss_act2 == 1:
                print("Sephikong used", Special)
                player_HP = player_HP - special_dmg


        print(name, "'s HP:", player_HP)
        print("Sephikong's HP:", Boss_HP)
        
        if player_HP <= 0:
            print("GAME OVER")
            retry = str(input("Try again?:"))
            if retry == "Y":
                        BossFight(Hero_Stats)

            else:
                        print("You Died!")
                        exit()
                        


        elif Boss_HP <= 0:
            print("YOU WIN!")
            Boss_death = True


        turn = turn + 1



BossFight()
