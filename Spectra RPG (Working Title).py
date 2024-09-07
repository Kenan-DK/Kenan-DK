#imports
#-----------------------------------
import random

#Global variables
#-----------------------------------
name = ""
magic = ""
magic_limit = 50

#SubPrograms
#-----------------------------------
def tutorial():
    print("REMEMBER! To select an attack, enter the first letter of the attack name in capitals!")
#-----------------------------------
def Infernus_battle():
    boss_hp = 3000
    attack1 = 50
    attack2 = 60

    robin_hp = 300
    p_attack = 50
    r_death = False

    elena_hp = 250
    e_attack = 60
    e_death = False

    magic_limit = 50
    item1 = "Potion"

    turn = 1
    death = False

    print("\n""The Flame Titan Approaches!")

    while death != True:
        print("\n""Turn", turn)
        if r_death != True:
          player_act = str(input("What would You like to do? ""\n""Fight""\n""Item""\n"))
          if player_act == "F":
              fight = str(input("\n""Which attack will you use?""\n""Slash""\n""Hurricane Swing""\n"))
              fight.upper()
            
              if fight == "S":
                  print("\n""Robin used Slash!")
                  boss_hp = boss_hp - (p_attack * 1.15)

              elif fight == "H":
                  print("\n""Robin used Hurricane Swing!")
                  boss_hp = boss_hp - (p_attack * 1.35)
                  magic_limit = magic_limit - 25

          elif player_act == "I":
              print(item1)
              item = str(input("Which item will you use?""\n"))
              item.upper()
              if item == "P":
                  print("Robin used a Potion!")
                  robin_hp = robin_hp + 75

        if e_death != True:
           elena_act = str(input("\n""What should Elena do? ""\n""Fight""\n""Item""\n"))
           if elena_act == "F":
              fight = str(input("\n""Which attack will you use?""\n""Light""\n""Flare""\n"))
              fight.upper()
            
              if fight == "L":
                  print("\n""Elena used Light!")
                  boss_hp = boss_hp - (e_attack * 1.12)

              elif fight == "H":
                  print("\n""Elena used Flare!")
                  boss_hp = boss_hp - (e_attack * 1.30)
                  magic_limit = magic_limit - 10

           elif elena_act == "I":
                print(item1)
                item = str(input("Which item will you use?""\n"))
                item.upper()
                if item == "P":
                    print("Elena used a Potion!")
                    elena_hp = elena_hp + 75


        boss_act = random.randint(0,1)
        if boss_act == 0:
            print("Infernus used Roast!")
            robin_hp = robin_hp - attack1
            elena_hp = elena_hp - attack1

        elif boss_act == 1:
            print("Infernus used Ruptured Flame!")
            robin_hp = robin_hp - attack2
            elena_hp = elena_hp - attack2

        magic_limit = magic_limit + 10

        print("Robin's HP:", robin_hp)
        print("Elena's HP:", elena_hp)
        print("Magic Limit:", magic_limit)
        print("Infernus' HP:", boss_hp)

        turn = turn + 1


        if boss_hp <= 0:
            death = True
            print("YOU WIN!")
            
        if robin_hp <= 0:
            r_death = True

        if elena_hp <= 0:
            e_death = True
            
        if robin_hp <= 0 and elena_hp <= 0:            
            print("GAME OVER!")

            retry = str(input("Try again? "))
            if retry == "Y":
                Infernus_battle()

            else:
                print("The Heroes had fallen and Vallar was resurrected...")
                exit()

        
                
#-----------------------------------

def Oceaus_battle():
    boss_hp = 2000
    attack1 = 40
    attack2 = 55

    robin_hp = 300
    p_attack = 50
    r_death = False

    elena_hp = 250
    e_attack = 60
    e_death = False

    magic_limit = 50
    item1 = "Potion"

    turn = 1
    death = False

    print("The Ocean Titan Approaches!")
    while death != True:
        print("\n""Turn", turn)
        if r_death != True:
          player_act = str(input("What would You like to do? ""\n""Fight""\n""Item""\n"))
          if player_act == "F":
              fight = str(input("\n""Which attack will you use?""\n""Slash""\n""Hurricane Swing""\n""Night Slash""\n"))
              fight.upper()
            
              if fight == "S":
                  print("\n""Robin used Slash!")
                  boss_hp = boss_hp - (p_attack * 1.15)

              elif fight == "H":
                  print("\n""Robin used Hurricane Swing!")
                  boss_hp = boss_hp - (p_attack * 1.35)
                  magic_limit = magic_limit - 25

              elif fight == "N":
                  print("\n""Robin used Night Slash!")
                  boss_hp = boss_hp - (p_attack * 1.60)
                  magic_limit = magic_limit - 35

          elif player_act == "I":
              print(item1)
              item = str(input("Which item will you use?""\n"))
              item.upper()
              if item == "P":
                  print("Robin used a Potion!")
                  robin_hp = robin_hp + 75

        if e_death != True:
           elena_act = str(input("\n""What should Elena do? ""\n""Fight""\n""Item""\n"))
           if elena_act == "F":
              fight = str(input("\n""Which attack will you use?""\n""Light""\n""Flare""\n""Thundra""\n"))
              fight.upper()
            
              if fight == "L":
                  print("\n""Elena used Light!")
                  boss_hp = boss_hp - (e_attack * 1.12)

              elif fight == "H":
                  print("\n""Elena used Flare!")
                  boss_hp = boss_hp - (e_attack * 1.30)
                  magic_limit = magic_limit - 10

              elif fight == "T":
                  print("\n""Elena used Thundra!")
                  boss_hp = boss_hp - (e_attack * 1.55)
                  magic_limit = magic_limit - 20

           elif elena_act == "I":
                print(item1)
                item = str(input("Which item will you use?""\n"))
                item.upper()
                if item == "P":
                    print("Elena used a Potion!")
                    elena_hp = elena_hp + 75


        boss_act = random.randint(0,1)
        if boss_act == 0:
            print("Oceaus used Shoal Crash!")
            robin_hp = robin_hp - attack1
            elena_hp = elena_hp - attack1

        elif boss_act == 1:
            print("Oceaus used Tidal Rush!")
            robin_hp = robin_hp - attack2
            elena_hp = elena_hp - attack2

        magic_limit = magic_limit + 10

        print("Robin's HP:", robin_hp)
        print("Elena's HP:", elena_hp)
        print("Magic Limit:", magic_limit)
        print("Infernus' HP:", boss_hp)

        turn = turn + 1


        if boss_hp <= 0:
            death = True
            print("YOU WIN!")
            
        if robin_hp <= 0:
            r_death = True

        if elena_hp <= 0:
            e_death = True
            
        if robin_hp <= 0 and elena_hp <= 0:            
            print("GAME OVER!")

            retry = str(input("Try again? "))
            if retry == "Y":
                Infernus_battle()

            else:
                print("The Heroes had fallen and Vallar was resurrected...")
                exit()


    

#-----------------------------------

def Gailus_battle():
    boss_hp = 4000
    attack1 = 65
    attack2 = 80

    robin_hp = 350
    p_attack = 64

    elena_hp = 300
    e_attack = 72

    magic_limit = 70

    turn = 1

    print("The Ocean Titan Approaches!")

    

#-----------------------------------
def Navu_battle():
    boss_hp = 7000
    attack1 = 80
    attack2 = 100

    robin_hp = 500
    p_attack = 80

    elena_hp = 460
    e_attack = 85

    magic_limit = 120

    turn = 1

    print("The Ocean Titan Approaches!")

    


#-----------------------------------
def Vallar_batte():
    boss_hp = 10000
    attack1 = 40
    attack2 = 55

    robin_hp = 300
    p_attack = 50

    elena_hp = 250
    e_attack = 60

    magic_limit = 200

    turn = 1

    print("The Ocean Titan Approaches!")

#-----------------------------------   
def Secret_Boss():
    boss_hp = 20000
    attack1 = 100
    attack2 = 150
    attack3 = 120
    attack4 = 160
    attack5 = 200
    attack6 = 250

    robin_hp = 800
    p_attack = 160
    r_death = False

    elena_hp = 750
    e_attack = 180
    e_death = False

    magic_limit = 150
    item1 = "Potion"

    turn = 1
    death = False

    print("Donkey Kong, Greninja and Kirby Approach!!")

    while death != True:
        print("\n""Turn", turn)
        if r_death != True:
          player_act = str(input("What would You like to do? ""\n""Fight""\n""Item""\n"))
          if player_act == "F":
              fight = str(input("\n""Which attack will you use?""\n""Slash""\n""Hurricane Swing""\n""Kleaving Spectra""\n""Night Slash""\n""Reaper""\n"))
              fight.upper()
            
              if fight == "S":
                  print("\n""Robin used Slash!")
                  boss_hp = boss_hp - (p_attack * 1.15)

              elif fight == "H":
                  print("\n""Robin used Hurricane Swing!")
                  boss_hp = boss_hp - (p_attack * 1.35)
                  magic_limit = magic_limit - 25

              elif fight == "K":
                  print("\n""Robin used Kleaving Spectra!")
                  boss_hp = boss_hp - (p_attack * 1.60)
                  magic_limit = magic_limit - 30

              elif fight == "N":
                  print("\n""Robin used Night Slash!")
                  boss_hp = boss_hp - (p_attack * 1.75)
                  magic_limit = magic_limit - 35

              elif fight == "R":
                  print("\n""Robin used Reaper!")
                  boss_hp = boss_hp - (p_attack * 1.65)
                  robin_hp = robin_hp + 60
                  magic_limit = magic_limit - 50
                  
                  

          elif player_act == "I":
              print(item1)
              item = str(input("Which item will you use?""\n"))
              item.upper()
              if item == "P":
                  print("Robin used a Potion!")
                  robin_hp = robin_hp + 120

        if e_death != True:
           elena_act = str(input("\n""What should Elena do? ""\n""Fight""\n""Item""\n"))
           if elena_act == "F":
              fight = str(input("\n""Which attack will you use?""\n""Light""\n""Flare""\n""Thundra""\n""Blizzar""\n""Stealing Light""\n"))
              fight.upper()
            
              if fight == "L":
                  print("\n""Elena used Light!")
                  boss_hp = boss_hp - (e_attack * 1.12)

              elif fight == "F":
                  print("\n""Elena used Flare!")
                  boss_hp = boss_hp - (e_attack * 1.30)
                  magic_limit = magic_limit - 10

              elif fight == "T":
                  print("\n""Elena used Thundra!")
                  boss_hp = boss_hp - (e_attack * 1.55)
                  magic_limit = magic_limit - 20

              elif fight == "B":
                  print("\n""Elena used Blizzar!")
                  boss_hp = boss_hp - (e_attack * 1.60)
                  magic_limit = magic_limit - 30

              elif fight == "S":
                  print("\n""Elena used Stealing Light!")
                  boss_hp = boss_hp - (e_attack * 1.50)
                  elena_hp = elena_hp + 75
                  magic_limit = magic_limit - 45
                  

           elif elena_act == "I":
                print(item1)
                item = str(input("Which item will you use?""\n"))
                item.upper()
                if item == "P":
                    print("Elena used a Potion!")
                    elena_hp = elena_hp + 120

        if turn > 2:
            rika_act = random.randint(1,3)
            if rika_act == 2:
                print("Rika used Toxic!")
                boss_hp = boss_hp - 100

            if rika_act == 3:
                print("\n""Rika used Restore-All!")
                robin_hp = robin_hp + 200
                elena_hp = elena_hp + 200

        xander_act = random.randint(0,1)
        if xander_act == 0:
            print("Xander used Flame Breath!")
            boss_hp = boss_hp - 110

        if xander_act == 1:
            print("Xander used Dark Breath!")
            boss_hp = boss_hp - 125


        boss_act = random.randint(0,3)
        if boss_act == 0:
            print("Donkey Kong used Ground Slam!")
            robin_hp = robin_hp - attack1
            elena_hp = elena_hp - attack1

        elif boss_act == 1:
            print("Donkey Kong used THE CLAP!")
            robin_hp = robin_hp - attack2
            elena_hp = elena_hp - attack2

        elif boss_act == 2:
            print("Donkey Kong used Aerial Smash!")
            robin_hp = robin_hp - attack3
            elena_hp = elena_hp - attack3

        elif boss_act == 3:
            print("Donkey Kong used Coconut Gun!")
            robin_hp = robin_hp - attack4
            elena_hp = elena_hp - attack4

        if boss_hp <= 5000:
            boss_act2 = random.randint(0,1)
            if boss_act2 == 0:
               print("Donkey Kong used Hurri-Kong!")
               robin_hp = robin_hp - attack6
               elena_hp = elena_hp - attack6

            elif boss_act2 == 1:
               print("Donkey Kong used Banana Slamma!")
               robin_hp = robin_hp - attack5
               elena_hp = elena_hp - attack5

        gren_act = random.randint(0,1)
        if gren_act == 0:
            print("Greninja used Water Shuriken!")
            robin_hp = robin_hp - 25
            elena_hp = elena_hp - 25

        elif gren_act == 1:
            print("Greninja used Shadow Sneak")
            robin_hp = robin_hp - 30
            elena_hp = elena_hp - 30

        kirb_act = random.randint(0,1)
        if kirb_act == 0:
            print("Kirby used Cutter!")
            robin_hp = robin_hp - 25
            elena_hp = elena_hp - 25

        elif kirb_act == 1:
            print("Kirby used Flaming Hammer!")
            robin_hp = robin_hp - 35
            elena_hp = elena_hp - 30
            
            

        magic_limit = magic_limit + 50

        print("Robin's HP:", robin_hp)
        print("Elena's HP:", elena_hp)
        print("Magic Limit:", magic_limit)
        print("Donkey Kong's HP:", boss_hp)

        turn = turn + 1


        if boss_hp <= 0:
            death = True
            print("YOU WIN!")
            
        if robin_hp <= 0:
            r_death = True

        if elena_hp <= 0:
            e_death = True
            
        if robin_hp <= 0 and elena_hp <= 0:            
            print("GAME OVER!")

            retry = str(input("Try again? "))
            if retry == "Y":
                Secret_Boss()

            else:
                print("The Heroes had fallen and Vallar was resurrected...")
                exit()

        
    



#-----------------------------------
def chap1_battle():
    nme_type = random.randint(1,3)
    if nme_type == 1:
        enemy = "Thundreel"
        nme_hp = 200
        attack1 = 40
        nme_attack = "Bolt!"

    elif nme_type == 2:
        enemy = "Octocannon"
        nme_hp = 250
        attack1 = 50
        nme_attack = "Octo Blast!"

    elif nme_type == 3:
        enemy = "PuffBomber"
        nme_hp = 220
        attack1 = 45
        nme_attack = "Spike Bomb!"


    robin_hp = 300
    p_attack = 50
    r_death = False

    elena_hp = 250
    e_attack = 60
    e_death = False

    magic_limit = 50
    item1 = "Potion"

    turn = 1
    death = False

    print("A", enemy, "approaches!")
    while death != True:
        print("\n""Turn", turn)
        if r_death != True:
          player_act = str(input("What would You like to do? ""\n""Fight""\n""Item""\n"))
          if player_act == "F":
              fight = str(input("\n""Which attack will you use?""\n""Slash""\n""Hurricane Swing""\n"))
              fight.upper()
            
              if fight == "S":
                  print("\n""Robin used Slash!")
                  nme_hp = nme_hp - (p_attack * 1.15)

              elif fight == "H":
                  print("\n""Robin used Hurricane Swing!")
                  nme_hp = nme_hp - (p_attack * 1.35)
                  magic_limit = magic_limit - 25

          elif player_act == "I":
              print(item1)
              item = str(input("Which item will you use?""\n"))
              item.upper()
              if item == "P":
                  print("Robin used a Potion!")
                  robin_hp = robin_hp + 75

        if e_death != True:
           elena_act = str(input("\n""What should Elena do? ""\n""Fight""\n""Item""\n"))
           if elena_act == "F":
              fight = str(input("\n""Which attack will you use?""\n""Light""\n""Flare""\n"))
              fight.upper()
            
              if fight == "L":
                  print("\n""Elena used Light!")
                  nme_hp = nme_hp - (e_attack * 1.12)

              elif fight == "H":
                  print("\n""Elena used Flare!")
                  boss_hp = boss_hp - (e_attack * 1.30)
                  magic_limit = magic_limit - 10

           elif elena_act == "I":
                print(item1)
                item = str(input("Which item will you use?""\n"))
                item.upper()
                if item == "P":
                    print("Elena used a Potion!")
                    elena_hp = elena_hp + 75

        print(enemy, "used", nme_attack)
        robin_hp = robin_hp - attack1
        elena_hp = elena_hp - attack1

        print("Robin's HP:", robin_hp)
        print("Elena's HP:", elena_hp)
        print("Magic Limit:", magic_limit)
        print(enemy, "'s HP:",nme_hp)

        turn = turn + 1
        magic_limit = magic_limit + 10

        if nme_hp <= 0:
            death = True
            print("YOU WIN!")
            
        if robin_hp <= 0:
            r_death = True

        if elena_hp <= 0:
            e_death = True
            
        if robin_hp <= 0 and elena_hp <= 0:            
            print("GAME OVER!")

            retry = str(input("Try again? "))
            if retry == "Y":
                chap1_battle()

            else:
                print("The Heroes had fallen and Vallar was resurrected...")
                exit()


def chap2_battle():
    nme_type = random.randint(1,3)
    if nme_type == 1:
        enemy = "Magma Golem"
        nme_hp = 300
        attack1 = 50
        nme_attack = "Fire Punch!"

    elif nme_type == 2:
        enemy = "Wolava"
        nme_hp = 250
        attack1 = 70
        nme_attack = "Inferno Fang!"

    elif nme_type == 3:
        enemy = "Flamadillo"
        nme_hp = 320
        attack1 = 65
        nme_attack = "Magma Bowl!"


    robin_hp = 300
    p_attack = 60
    r_death = False

    elena_hp = 250
    e_attack = 70
    e_death = False

    magic_limit = 60
    item1 = "Potion"

    turn = 1
    death = False

    print("A", enemy, "approaches!")
    while death != True:
        print("\n""Turn", turn)
        if r_death != True:
          player_act = str(input("What would You like to do? ""\n""Fight""\n""Item""\n"))
          if player_act == "F":
              fight = str(input("\n""Which attack will you use?""\n""Slash""\n""Hurricane Swing""\n"))
              fight.upper()
            
              if fight == "S":
                  print("\n""Robin used Slash!")
                  nme_hp = nme_hp - (p_attack * 1.15)

              elif fight == "H":
                  print("\n""Robin used Hurricane Swing!")
                  nme_hp = nme_hp - (p_attack * 1.35)
                  magic_limit = magic_limit - 25

          elif player_act == "I":
              print(item1)
              item = str(input("Which item will you use?""\n"))
              item.upper()
              if item == "P":
                  print("Robin used a Potion!")
                  robin_hp = robin_hp + 75

        if e_death != True:
           elena_act = str(input("\n""What should Elena do? ""\n""Fight""\n""Item""\n"))
           if elena_act == "F":
              fight = str(input("\n""Which attack will you use?""\n""Light""\n""Flare""\n"))
              fight.upper()
            
              if fight == "L":
                  print("\n""Elena used Light!")
                  nme_hp = nme_hp - (e_attack * 1.12)

              elif fight == "H":
                  print("\n""Elena used Flare!")
                  boss_hp = boss_hp - (e_attack * 1.30)
                  magic_limit = magic_limit - 10

           elif elena_act == "I":
                print(item1)
                item = str(input("Which item will you use?""\n"))
                item.upper()
                if item == "P":
                    print("Elena used a Potion!")
                    elena_hp = elena_hp + 75

        print(enemy, "used", nme_attack)
        robin_hp = robin_hp - attack1
        elena_hp = elena_hp - attack1

        print("Robin's HP:", robin_hp)
        print("Elena's HP:", elena_hp)
        print("Magic Limit:", magic_limit)
        print(enemy, "'s HP:",nme_hp)

        turn = turn + 1
        magic_limit = magic_limit + 10

        if nme_hp <= 0:
            death = True
            print("YOU WIN!")
            
        if robin_hp <= 0:
            r_death = True

        if elena_hp <= 0:
            e_death = True
            
        if robin_hp <= 0 and elena_hp <= 0:            
            print("GAME OVER!")

            retry = str(input("Try again? "))
            if retry == "Y":
                chap1_battle()

            else:
                print("The Heroes had fallen and Vallar was resurrected...")
                exit()







Oceaus_battle()
tutorial()
chap1_battle()
Infernus_battle()
Secret_Boss()
    
