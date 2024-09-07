#imports
#-----------------------------------
import random
import time

#Global variables
#-----------------------------------
name = ""
magic = ""
magic_limit = 50

enemy_type = ""


#SubPrograms
#-----------------------------------
#Boss Fight
#-----------------------------------
def BossFight(Hero_Stats):
    Boss_HP = 1000
    Attack_1 = "Jenova Slam"
    Att_1_dmg = 35
    Attack_2 = "Hyper Slash"
    Att_2_dmg = 50
    Attack_3 = "Coconut Gun"
    Att_3_dmg = 60
    Special = "Ancient Meteor"
    special_dmg = 70


    player_HP = 250
    magic_limit = 50
    

    attack = 50
    item1 = "Potion"
    item2 = "Hyper Potion"

    turn = 1

    print("\n""Sephikong Approaches!")


    while Boss_death != True:
        print("\n""Turn", turn)
        
        action = str(input("What would you like to do?" "\n" "Fight" "\n " "Magic" "\n" "Item" "\n" ))

        if action == "F":
            print(name, "used Slash")
            slash_dmg = attack * 1.5
            Boss_HP = Boss_HP - slash_dmg

        if action == "M":
            materia = str(input("What magic will you use?: " ))

            if materia == "F":
               print(name, "used Fire2")
               fire_dmg = attack * 2
               magic_limit = magic_limit - 5
               Boss_HP = Boss_HP - fire_dmg

            elif materia == "Q":
               print(name, "used Quake2")
               quake_dmg = (attack * 2) + 10
               magic_limit = magic_limit - 5
               Boss_HP = Boss_HP - quake_dmg

            elif materia == "I":
               print(name, "used Ice2")
               quake_dmg = (attack * 1.8)
               magic_limit = magic_limit - 5
               Boss_HP = Boss_HP - quake_dmg
            
                                            
        elif action == "I":
            print(item1, item2)
            item = str(input("select an item: "))
            print(item)
            if item == "P":
                print(name, "used a potion!")
                player_HP = player_HP + 60

            elif item == "H":
                print(name, "used a Hyper Potion!")
                player_HP = player_HP + 100

        


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
                        print("You Died, and Gaia was Destroyed...")
                        exit()
                        


        elif Boss_HP <= 0:
            print("YOU WIN!")
            Boss_death = True


        turn = turn + 1

        
    

    
    
#Random enemy encounter
#-----------------------------------
def Chap1_battle(Hero_Stats):
    attack = 50
    player_HP = 250
    NME_death = False

    NME = random.randint(0, 1)
    
    if NME == 0:
        enemy_type = "Shinra Guard"
        enemyHP = 120

    elif NME == 1:
        enemy_type = "Shinra SOLIDER 2nd Class"
        enemyHP = 180


    turn = 1

    print("\n","A", enemy_type, "appeared!")

    while NME_death != True:
        print("\n""Turn", turn)
        
        action = str(input("What would you like to do?" "\n" "Fight" "\n " "Magic" "\n" "Item" "\n" ))

        if action == "F":
            print(name, "used Slash!")
            slash_dmg = attack * 1.2
            enemyHP = enemyHP - slash_dmg

        elif action == "M":
            materia = str(input("What Materia will you use?: "))
            if materia == "F":
               print(name, "used Fire" )
               fire_dmg = attack * 1.2
               Boss_HP = Boss_HP - magic_dmg

            elif materia == "Q":
               print(name, "used Quake")
               quake_dmg = (attack * 1.2)
               enemyHP = enemyHP - quake_dmg

            elif materia == "I":
               print(name, "used Ice")
               quake_dmg = (attack * 1.2) 
               enemyHP = enemyHP - quake_dmg
                      
        elif action == "I":
            print(item1, item2)
            item = str(input("select an item: "))
            if item == "P":
                print(name, "used a potion!")
                player_HP = player_HP + 60


        enemy_act = random.randint(0,1)
        if enemy_act == 0:
            print(enemy_type, "used Slash!")
            player_HP = player_HP - 30

        elif enemy_act == 1:
            print(enemy_type, "used Buster!")
            player_HP = player_HP - 40
            

        print(name, "'s HP:", player_HP)
        print(enemy_type, ":", enemyHP)

        turn = turn + 1
        

        if enemyHP <= 0:
            print ("You Win!")
            NME_death = True

        
        if player_HP <= 0:
            print("GAME OVER")
            retry = str(input("Try again?:"))
            if retry == "Y":
                        Chap1_battle(Hero_Stats)

            else:
                        print("You Died, and Gaia was Destroyed...")
                        exit()
                        

#-----------------------------------------------------

def Ylisse_battle(Hero_Stats):
    attack = 50
    player_HP = 250
    NME_death = False

    NME = random.randint(0, 2)
    if NME == 0:
        enemy_type = "Plegian Brigand"
        enemyHP = 260

    elif NME == 1:
        enemy_type = "Plegian Theif"
        enemyHP = 0


    elif NME == 2:
        enemy_type = "Plegian Cavalier"
        enemyHP = 365

    turn = 1

    print("\n""A", enemy_type, "appeared!")

    while NME_death != True:
        print("\n""Turn", turn)
        
        action = str(input("What would you like to do?" "\n" "Fight" "\n" "Item" "\n" ))

        if action == "F":
            print(name, "used Slash")
            slash_dmg = attack * 1.2
            enemyHP = enemyHP - slash_dmg
                      
        elif action == "I":
            print(item1, item2)
            item = str(input("select an item: "))
            if item == "P":
                print(name, "used a Vulnary!")
                player_HP = player_HP + 60

        chrom_act = random.randint(0,1)

        if chrom_act == 0:
            print("Chrom Used Falchion!")
            enemyHP = enemyHP - 60

        elif chrom_act == 1:
            print("Chrom Used Aether!")
            enemyHP = enemyHP - 60



        enemy_act = random.randint(0,1)
        if enemy_act == 0:
            print(enemy_type, "used Slash!")
            player_HP = player_HP - 60

        elif enemy_act == 1:
            print(enemy_type, "used Quick Slash!")
            player_HP = player_HP - (25 * 2)


        print(name, "'s HP:", player_HP)
        print(enemy_type, ":", enemyHP)

        turn = turn + 1
        
        if enemyHP <= 0:
           print ("You Win!")
           NME_death = True

        if player_HP <= 0:
            print("GAME OVER")
            retry = str(input("Try again?:"))
            if retry == "Y":
                        Ylisse_battle(Hero_Stats)

            else:
                        print("You Died, and Gaia was Destroyed...")
                        exit()

#---------------------------------------------------

def Gangrel_Boss(Hero_Stats):
    gangrel_HP = 3600
    g_att_1 = "Levin Dagger"
    g_att1_dmg = 50
    g_att_2 = "Glacies"
    g_att2_dmg = 25
    g_att_3 = "Levin Sword"
    g_att3_dmg = 75

    player_HP = 300
    attack = 60
    item1 = "Vulnary"
    Boss_death = False

    turn = 1

    print("\n""Gangrel Approches!")

    while Boss_death != True:
        print("\n""Turn", turn)
        
        action = str(input("What would you like to do?" "\n" "Fight" "\n" "Item" "\n" ))

        if action == "F":
            print(name, "used Slash")
            slash_dmg = attack * 1.25
            gangrel_HP = gangrel_HP - slash_dmg

        elif action == "I":
            print(item1)
            item = str(input("select an item: "))
            print(item)
            if item == "P":
                print(name, "used a Vulnary!")
                player_HP = player_HP + 100

        chrom_act = random.randint(0,1)

        if chrom_act == 0:
            print("Chrom Used Falchion!")
            gangrel_HP = gangrel_HP - 60

        elif chrom_act == 1:
            print("Chrom Used Aether!")
            gangrel_HP = gangrel_HP - 60

        print("Lucina Used Parallel Falchion!")
        gangrel_HP = gangrel_HP - 60

        print("Robin Used Thoron!")
        gangrel_HP = gangrel_HP - 60


        gangrel_act = random.randint(0,2)
        if gangrel_act == 0:
            print("Gangrel used", g_att_1)
            player_HP = player_HP - g_att1_dmg

        elif gangrel_act == 1:
            print("Gangrel used", g_att_2)
            player_HP = player_HP - g_att2_dmg

        elif gangrel_act == 2:
            print("Gangrel used", g_att_3)
            player_HP = player_HP - g_att3_dmg 
            

        if gangrel_HP <= 0:
            print ("You Win!")
            Boss_death = True

        if player_HP <= 0:
            print("GAME OVER")
            retry = str(input("Try again?:"))
            if retry == "Y":
                        Gangrel_Boss(Hero_Stats)

            else:
                        print("You Died, and Gaia was Destroyed...")
                        exit()
                        

        print(name, "'s HP:", player_HP)
        print("Gangrel's HP:", gangrel_HP)

        turn = turn + 1

#-----------------------------------   
def Chap2_battle(Hero_Stats):
    attack = 50
    player_HP = 250
    NME_death = False

    NME = random.randint(0, 1)
    
    if NME == 0:
        enemy_type = "Shinra Guard"
        enemyHP = 240

    elif NME == 1:
        enemy_type = "Shinra SOLIDER 2nd Class"
        enemyHP = 360


    turn = 1

    print("\n","A", enemy_type, "appeared!")

    while NME_death != True:
        print("\n""Turn", turn)
        
        action = str(input("What would you like to do?" "\n" "Fight" "\n " "Magic" "\n" "Item" "\n" ))

        if action == "F":
            print(name, "used Slash!")
            slash_dmg = attack * 1.2
            enemyHP = enemyHP - slash_dmg

        elif action == "M":
            materia = str(input("What Materia will you use?: "))
            if materia == "F":
               print(name, "used Fire" )
               fire_dmg = attack * 1.2
               Boss_HP = Boss_HP - magic_dmg

            elif materia == "Q":
               print(name, "used Quake")
               quake_dmg = (attack * 1.2) + 10
               enemyHP = enemyHP - quake_dmg

            elif materia == "I":
               print(name, "used Ice")
               quake_dmg = (attack * 1.2) 
               enemyHP = enemyHP - quake_dmg
                      
        elif action == "I":
            print(item1, item2)
            item = str(input("select an item: "))
            if item == "P":
                print(name, "used a potion!")
                player_HP = player_HP + 60


        Tifa_act = random.randint(0,1)
        if Tifa_act == 0:
            print("Tifa Used Punch!")
            enemyHP = enemyHP - 60

        elif Tifa_act == 1:
            print("Tifa Used Bolt!")
            enemyHP = enemyHP - 60


        enemy_act = random.randint(0,1)
        if enemy_act == 0:
            print(enemy_type, "used Slash!")
            player_HP = player_HP - 40

        elif enemy_act == 1:
            print(enemy_type, "used Buster!")
            player_HP = player_HP - 50
            

        print(name, "'s HP:", player_HP)
        print(enemy_type, ":", enemyHP)

        turn = turn + 1
        


        if enemyHP <= 0:
            print ("You Win!")
            NME_death = True

        if player_HP <= 0:
            print("GAME OVER")
            retry = str(input("Try again?:"))
            if retry == "Y":
                        Chap2_battle(Hero_Stats)

            else:
                        print("You Died, and Gaia was Destroyed...")
                        exit()

#-----------------------------------
def Heli_Gunner(Hero_Stats):
    Heli_HP = 3600
    attack1 = "AB Cannon"
    attack1_dmg = 75
    attack2 = "C Cannon"
    attack2_dmg = 60
    Boss_death = False


    player_HP = 300
    attack = 60
    item1 = "Potion"

    turn = 1

    print("\n""The Heli_Gunner Flies In!")

    while Boss_death != True:
        print("\n""Turn", turn)
        
        action = str(input("What would you like to do?" "\n" "Fight" "\n" "Magic" "\n" "Item" "\n" ))

        if action == "F":
            print(name, "used Slash")
            slash_dmg = attack * 1.2
            Heli_HP = Heli_HP - slash_dmg

        elif action == "M":
            materia = str(input("What Materia will you use?: "))
            if materia == "F":
               print(name, "used Fire" )
               fire_dmg = attack * 1.2
               Heli_HP = Heli_HP - magic_dmg

            elif materia == "Q":
               print(name, "used Quake")
               quake_dmg = attack * 1.2
               Heli_HP = Heli_HP - quake_dmg

            elif materia == "I":
               print(name, "used Ice")
               quake_dmg = attack * 1.2 
               Heli_HP = Heli_HP - quake_dmg
                      
        elif action == "I":
            print(item1,)
            item = str(input("select an item: "))
            if item == "P":
                print(name, "used a Poton!")
                player_HP = player_HP + 70

        Tifa_act = random.randint(0,1)

        if Tifa_act == 0:
            print("Tifa Used Punch!")
            Heli_HP = Heli_HP - 60

        elif Tifa_act == 1:
            print("Tifa Used Bolt!")
            Heli_HP = Heli_HP - 60

        Luigi_act = random.randint(0, 1)
        if Luigi_act == 0:
            print("Luigi used Hammer!")
            Heli_HP = Heli_HP - 60

        elif Luigi_act == 1:
            print("Luigi used Cyclone!")
            Heli_HP = Heli_HP - 70


        Heli_act = random.randint(0, 1)
        if Heli_act == 0:
                print("Heli Gunner used", attack1)
                player_HP = player_HP - attack1_dmg

        elif Heli_act == 1:
                print("Heli Gunner used", attack2)
                player_HP = player_HP - attack2_dmg


        print(name, "'s HP:", player_HP)
        print("HeliGunner's HP:", Heli_HP)

        turn = turn + 1

        if Heli_HP <= 0:
            print("You Win!")
            Boss_death = True

        if player_HP <= 0:
            print("GAME OVER")
            retry = str(input("Try again?:"))
            if retry == "Y":
                        Heli_Gunner(Hero_Stats)

            else:
                        print("You Died, and Gaia was Destroyed...")
                        exit()
                        

#-------------------------------------------------
def Tyranitar_battle(Hero_Stats):
    Ttar_HP = 4040
    t_att_1 = "Rock Slide"
    t_att_1dmg = 75
    t_att_2 = "Crunch"
    t_att_2dmg = 80
    t_att_3 = "Earthquake"
    t_att_3dmg = 90
    t_att_4 = "Rock Tomb"
    t_att_4dmg = 60

    player_HP = 500
    attack = 80
    item1 = "Super Potion"
    item2 = "Sitrus Berry"

    turn = 1
    Boss_death = False

    print("Tyranitar Approaches!")

    while Boss_death != True:
        print("\n""Turn", turn)
        
        action = str(input("What would you like to do?" "\n" "Fight" "\n" "Item" "\n" ))

        if action == "F":
            print(name, "used Slash")
            slash_dmg = attack * 1.3
            Ttar_HP = Ttar_HP - slash_dmg

        elif action == "I":
            print(item1)
            print(item2)
            item = str(input("Select an item: "))
            
            if item == "P":
                print(name, "used a Super Potion!")
                player_HP = player_HP + 100

            elif item == "S":
                print(name, "used a Sitrus Berry!")
                player_HP = player_HP + (player_HP // 3)

        chrom_act = random.randint(0,1)

        if chrom_act == 0:
            print("Chrom Used Falchion!")
            Ttar_HP = Ttar_HP - 70

        elif chrom_act == 1:
            print("Chrom Used Aether!")
            Ttar_HP = Ttar_HP - (60 * 1.6)


        Ttar_act = random.randint(0, 3)
        if Ttar_act == 0:
            print("Tyranitar used", t_att_1)
            player_HP = player_HP - t_att_1dmg

        elif Ttar_act == 1:
            print("Tyranitar used", t_att_2)
            player_HP = player_HP - t_att_2dmg

        elif Ttar_act == 2:
            print("Tyranitar used", t_att_3)
            player_HP = player_HP - t_att_3dmg

        elif Ttar_act == 3:
            print("Tyranitar used", t_att_4)
            player_HP = player_HP - t_att_4dmg


        print("Cloud's HP:", player_HP)
        print("Tyranitar's HP:", Ttar_HP)

        turn = turn + 1

        if Ttar_HP <= 0:
            boss_death = True
            print("You Win!")

        elif player_HP <= 0:
             print("Game Over")
             retry = str(input("Retry?: "))
             if retry == "Y":
                 Tyranitar_battle(Hero_Stats)
        


    
def Tyranitar_battleALT(Hero_Stats):
    Ttar_HP = 4040
    t_att_1 = "Rock Slide"
    t_att_1dmg = 75
    t_att_2 = "Crunch"
    t_att_2dmg = 80
    t_att_3 = "Earthquake"
    t_att_3dmg = 90
    t_att_4 = "Rock Tomb"
    t_att_4dmg = 60

    player_HP = 350
    attack = 70
    item1 = "Super Potion"
    item2 = "Sitrus Berry"

    turn = 1
    Boss_death = False

    while Boss_death != True:
        print("\n""Turn", turn)
        
        action = str(input("What would you like to do?" "\n" "Fight" "\n" "Item" "\n" ))

        if action == "F":
            print(name, "used Slash")
            slash_dmg = attack * 1.3
            Ttar_HP = Ttar_HP - slash_dmg

        elif action == "I":
            print(item1)
            print(item2)
            item = str(input("Select an item: "))
            
            if item == "P":
                print(name, "used a Super Potion!")
                player_HP = player_HP + 100

            elif item == "S":
                print(name, "used a Sitrus Berry!")
                player_HP = player_HP + (player_HP // 3)

        Luigi_act = random.randint(0, 1)
        if Luigi_act == 0:
            print("Luigi used Hammer!")
            Ttar_HP = Ttar_HP - 60

        elif Luigi_act == 1:
            print("Luigi used Cyclone!")
            Ttar_HP = Ttar_HP - 70

            Ttar_act = random.randint(0, 4)
            if Ttar_act == 0:
                print("Tyranitar used", t_att_1)
                player_HP = player_HP - t_att_1dmg

            elif Ttar_act == 1:
                print("Tyranitar used", t_att_2)
                player_HP = player_HP - t_att_2dmg

            elif Ttar_act == 2:
                print("Tyranitar used", t_att_3)
                player_HP = player_HP - t_att_3dmg

            elif Ttar_act == 3:
                print("Tyranitar used", t_att_4)
                player_HP = player_HP - t_att_4dmg

        turn = turn + 1
    
#Character Information
#-----------------------------------
def Hero_Stats(name):
    print(name)
    player_HP = 250
    print("HP = 250")
    attack = 50
    print("Attack = 50")
    weapon_class = "sword"
    print("Weapon-class = sword")
    magic = "Fire, Quake, Ice"
    print("Materia = Fire, Quake, Ice")
    
    return Hero_Stats
    

#Story Mode
#-----------------------------------
def StoryModeChap1(name):
    print("Chapter 1: A Rift and a Reactor ")
    print("\n""After a Mysterious Rift opened near the Nibelhiem Reactor...")
    print("...Creatures from other worlds began to appear out of nowhere.")
    print("It seemed like a war across universes had begun, but that may not be the case...")
    print("\n" "Sephiroth had used Jenova's power to summon warriors from other worlds...")
    print("...In order for him to fulfill his revenge against the Shinra, and Gaia.")

    print("\n" ,name, ": This is Why I'm here. To close the Rift, and defeat Sephiroth.")
    print("Tifa: The reactor is over there, good luck", name)
    time.sleep(2)

    Chap1_battle(Hero_Stats)
    time.sleep(2)

    act_1 = str(input("\n""Which way, through the Rift or to the Mako Reactor?: "))
    if act_1 == "R":
        time.sleep(2)
        print(StoryModeChap2(name))

    else:
        time.sleep(2)
        print(StoryModeChap2Alt(name))
        
#------------------------------------------------------------------------------                
def StoryModeChap2(name):
    print("\n""Chapter 2: Awakening")
    print(name,": What is this place...")
    print("???: The Halidom of Ylisse")
    print(name, ": Who Are you?")
    print("???: Chrom, Prince of Ylisse.")
    print("Chrom: You're here because of the Rift, right?")
    print(name, ": Yes.")
    print("Chrom: Allow me to join you, I'm also searching for a way to close the Rift.")
    print("-Chrom Joined the party!-")
    print("Chrom: My Soliders and Robin are headed for the Rift at Mount Prism, We'll Catch up if we're quick!")
    time.sleep(3)

    Ylisse_battle(Hero_Stats)
    time.sleep(2)

    print("\n""Chrom: We've made it to Mount Prism, the Rift should be up ahead.")
    print("Robin: Chrom, you're here, there are enemy forces up ahead, BE CAREFUL!")
    print(name, "and Chrom: We'll be Fine, don't worry.")
    time.sleep(2)

    Ylisse_battle(Hero_Stats)
    time.sleep(2)

    print("\n""Chrom: Lucina! You made it too?")
    print("Lucina: Be careful, Gangrel is in there! ")
    print("Robin: Allow us to be of assistance.")
    print(name, ":The more the merrier!")

    print("-Robin Joined The Party!-")
    print("-Lucina Joined The Party!-")
    time.sleep(2)

    print("\n""Gangrel: Prepare to die, Sheperds!")

    Gangrel_Boss(Hero_Stats)

    print("\n", name, ": We Won!")
    print("Chrom: Well fought Commrades!")
    print("Lucina: If it weren't for Robin's tactics, we would have died!")
    print("Robin: Just doing my Job.")
    print(name, ":, There's the Rift, but it doesn't lead to Gaia...")
    print("Chrom: Robin and Lucina, I need you to stay behind and lead the Sheperds while I'm away with Cloud.")
    print("Lucina and Robin: Yes Sir!")
    print("-Lucina and Robin left the Party-")
    print(name, ": Lets go, Chrom!")
    time.sleep(5)

    Chap3_StoryMode(name)
#-------------------------------------------------
def StoryModeChap2Alt(name):
    print("Chapter 2: The Visitor")

    print("\n", name, ":This place is heavily guarded...")
    print("Tifa: There you are,", name)
    print(name, ":You made it! This place is guarded by the Shinra.")
    print("Tifa: We'll go together, Like old times!")
    print("-Tifa Joined the Party!-")
    time.sleep(2)

    Chap2_battle(Hero_Stats)
    time.sleep(2)

    print(name, ":There's not far to go now.")
    print("Tifa: We'll be at the Mako Reactor Core before you know it!")
    time.sleep(2)

    Chap2_battle(Hero_Stats)
    time.sleep(2)

    print("\n""Tifa: Cloud be careful! It seems a Rift is opening!")
    print(name, ": Get Ready...")
    print("???: OH YEAH!")
    print("Tifa : What the-")
    print("???: I'm a Luigi, Number One!")
    print(name, ": Oh its just Luigi. I guess his world also got affected. I hope your ready, Luigi!")
    print("Luigi: Oh Yeah, Lets a Go!")
    print("-Luigi Joined the Party-")
    print("Tifa: Crap!")
    print(name, ": Here comes a HeliGunner!")
    time.sleep(3)

    Heli_Gunner(Hero_Stats)
    time.sleep(2)

    print("Tifa: That was TOUGH!")
    print(name, ": Well, at leats we're alive.")
    print("Luigi: Oh yeah!")
    print("Tifa: Hey look, another Rift is opening!")
    print(name, ": Tifa, go find Barret and the others and meet us in Costa Del Sol, We're going through the Rift.")
    print("-Tifa left the party-")
    print("Tifa: Good luck you two!")
    print("Luigi: Lets-a GO!")
    time.sleep(2)

    Chap3_StoryModeALT(name)


#-------------------------------------------------
    
def Chap3_StoryMode(name):
    print("\n""Chapter 3: The Raging Titan in another world")
    time.sleep(1)
    print("Chrom: We seem to have ended up in a cave.")
    print(name, ": But where?")
    print("Chrom: Judging from the nearby creatures, somewhere in Alola.")
    print("The ground around them shakes, a beast approaches...")
    print(name, ":Get ready!")
    time.sleep(1)

    Tyranitar_battle(Hero_Stats)
    time.slep(1)

    




def Chap3_StoryModeALT(name):
    print("\n""Chapter 3: The Raging Titan in another world")
    time.sleep(1)



#Main Program
#-----------------------------------
name = "Cloud"
Hero_Stats(name)
#BossFight(Hero_Stats)
StoryModeChap1(name)




        
        

  
