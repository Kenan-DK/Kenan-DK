import random


def boss():
    playerHP = 450
    playerAttack = 60
    playerDeath = False
    personaV = False
    pTurn = 0

    allyHP = 760
    allyAttack = 20
    allyPersona = False
    allyDeath = False

    bossHP = 6250
    bossAttack = 85
    bossDeath = False

    turn = 1
    arcana = 0

    while bossDeath != True:
        print("\n""Turn:", turn)
        if playerDeath != True:
            pAct = input("What will you do""\n""Attack (a)""\n""Skill (s)""\n""Persona (p)""\n""Item (i)""\n")
            if pAct == "a":
                print("Jeremy used Slash!")
                bossHP = bossHP - (playerAttack * 1.15)

            elif pAct == "s":
                pSkill = input("Mabufudyne (m)""\n""Miracle Punch (p)""\n""Ice Amp (i)""\n")
                if pSkill == "m":
                    print("Jeremy used Mabufudyne!")
                    print("Jeremy: Take this")
                    bossHP = bossHP - (playerAttack * 1.25)

                elif pSkill == "p":
                    print("Jeremy used Miracle Punch!")
                    print("Jeremy: Get a load of this!")
                    bossHP = bossHP - (playerAttack * 1.35)

                elif pSkill == "m":
                    print("Jeremy used Ice Amp!")
                    playerAttack = playerAttack + 5
                    allyAttack = allyAttack + 5
                    response = random.randint(1,3)
                    if response == 1:
                        print("Hilda: Aww Thank you")

                    elif response == 2:
                        print("Hilda: You're so sweet Jeremy")

                    elif response == 3:
                        print("Hilda: Thank you")

            elif pAct == "p":
                if arcana >= 5:
                    personaV = True
                    print("Jeremy: Persona!")
                    print("You summoned Black Frost!""\n""Black Frost: Hee-Ho!")
                    if personaV == True:
                        playerAttack = 90
                        BFact = random.randint(1,2)
                        if BFact == 1:
                            print("Jeremy used Mabufudyne EX!")
                            print("Jeremy: Can't Dodge this!")
                            bossHP = bossHP - (playerAttack * 1.4)

                        elif BFact == 2:
                            print("Jeremy used Diamond Dust!")
                            print("Jeremy: Get a load of this!")
                            bossHP = bossHP - (playerAttack * 1.5)

                        pTurn = pTurn + 1

                        if pTurn == 3:
                            personaV = False
                            arcana = 0
                            
                    else:
                        print("Jeremy used Slash!")
                        bossHP = bossHP - (playerAttack * 1.15)

           

            elif pAct == "i":
                pItem = input("Which item will you use""\n""Devil Fruit (d)""\n""Moon Dango (m)""\n")
                if pItem == "d":
                    print("Jeremy used a Devil Fruit!")
                    playerHP = playerHP + 65

                elif pItem == "m":
                    print("Jeremy shared a Moon Dango!")
                    playerHP = playerHP + 100
                    allyHP = allyHP + 100
                    response = random.randint(1,3)
                    if response == 1:
                        print("Hilda: Aww Thank you")

                    elif response == 2:
                        print("Hilda: You're so sweet Jeremy")

                    elif response == 3:
                        print("Hilda: Thank you")

            oneMore = random.randint(1,6)

            if oneMore == 2:
                print("One more time!""\n""Jeremy used Slash!")
                bossHP = bossHP - (playerAttack * 1.15)

            elif oneMore == 5:
                print("Jeremy: Time for an All-Out-Attack!")
                for x in range(6):
                    bossHP = bossHP - ((playerAttack + allyAttack) * 1.25)

                    

            
            if allyDeath != True:
                allyAct = random.randint(1,4)
                if allyAct == 1:
                   print("Hilda used slam")
                   bossHP = bossHP - (allyAttack * 1.15)

                elif allyAct == 2:
                   print("Hilda used Maziodyne!")
                   print("Hilda: Gotcha!")
                   bossHP = bossHP - (allyAttack * 1.3)

                elif allyAct == 3:
                   print("Hilda used Salvation!")
                   print("Hilda: Here you go!")
                   playerHP = playerHP + 125
                   pResponse = random.randint(1,3)
                   if pResponse == 1:
                      print("Jeremy: You're too Kind")

                   elif pResponse == 2:
                      print("Jeremy: Thanks pal")

                   elif pResponse == 3:
                      print("Jeremy: You're the best Hilda")

                elif allyAct == 4:
                   print("Hilda used Mediarahan!")
                   playerHP = playerHP + 75
                   allyHP = allyHP + 75
                   pResponse = random.randint(1,3)
                   if pResponse == 1:
                       print("Jeremy: You're too Kind")

                   elif pResponse == 2:
                       print("Jeremy: Thanks pal")

                   elif pResponse == 3:
                       print("Jeremy: You're the best Hilda")

                elif allyAct == 5:
                   if arcana != 0:
                       allyPersona = True
                       print("Hilda summoned Ishtar")
                       print("Hilda: Persona!""\n""Ishtar: I love all")
                       allyAttack = 40
                       apAct = random.randint(1,2)

                       if apAct == 1:
                           print("Hilda used Maziodyne EX!")
                           print("Hilda: Take this!")
                           bossHP = bossHP - (allyAttack * 1.4)

                       else:
                           print("Hilda used Mediarahan EX!")
                           print("Hilda: For You my Friend!")
                           playerHP = playerHP + 175
                           allyHP= alyHP + 175
                           pResponse = random.randint(1,3)
                           if pResponse == 1:
                              print("Jeremy: You're too Kind!")

                           elif pResponse == 2:
                              print("Jeremy: Thanks pal!")

                           elif pResponse == 3:
                              print("Jeremy: You're the best Amelia")
                        
                else:
                        print("Amelia used Slam")
                        bossHP = bossHP - (allyAttack * 1.15)



        bact = random.randint(1,4)

        if bact == 1:
            print("Donkey used the Coconut Gun")
            playerHP = playerHP - (bossAttack * 1.10)
            allyHP = allyHP - (bossAttack * 1.10)

        elif bact == 2:
            print("Donkey Kong summoned Sephiroth")
            bskill = random.randint(1,3)

            if bskill == 1:
                print("Donkey Kong Used Giga Flare")
                target = random.randint(1,2)
                if target == 1:
                    playerHP = playerHP - (bossAttack * 1.15)

                else:
                    allyHP = allyHP - (bossAttack * 1.15)

            elif bskill == 2:
                print("Donkey Kong Used Masamune")
                target = random.randint(1,2)
                if target == 1:
                    playerHP = playerHP - (bossAttack * 1.25)

                else:
                    allyHP = allyHP - (bossAttack * 1.25)
                


            elif bskill == 3:
                print("Donkey Kong Used Meteor")
                playerHP = playerHP - (bossAttack * 1.50)
                allyHP = allyHP - (bossAttack * 1.50)


        elif bact == 3:
            print("Donkey Kong summoned Bowser!")
            bskill = random.randint(1,3)

            if bskill == 1:
                print("Donkey Kong Used Fire Breath")
                playerHP = playerHP - (bossAttack * 1.15)
                allyHP = allyHP - (bossAttack * 1.15)

            elif bskill == 2:
                print("Donkey Kong Used Shell Smash!")
                bossAttack = bossAttack + 10


            elif bskill == 3:
                print("Donkey Kong Used Shell Spinner")
                for x in range (1, 4):
                    target = random.randint(1,2)
                    if target == 1:
                        playerHP = playerHP - (bossAttack * 1.20)

                    else:
                        allyHP = allyHP - (bossAttack * 1.20)


        elif bact == 4:
            print("Donkey Kong summoned Eggman!")
            bskill = random.randint(1,3)

            if bskill == 1:
                print("Donkey Kong Used Eclipse Cannon!")
                playerHP = playerHP - (bossAttack * 1.40)
                allyHP = allyHP - (bossAttack * 1.40)

            elif bskill == 2:
                print("Donkey Kong Used Hyper Bomber!")
                bossAttack = bossAttack + 5
                bossHP = bossHP + 100


            elif bskill == 3:
                print("Donkey Kong Used Nega Wisp Cannon!")
                target = random.randint(1,2)
                if target == 1:
                    playerHP = playerHP - (bossAttack * 1.35)

                else:
                    allyHP = allyHP - (bossAttack * 1.35)


        print("\n""Jeremy's HP:",playerHP)
        print("Hilda's HP:",allyHP)
        print("Donkey Kong's HP:",bossHP)
        arcana = arcana + 1
        turn = turn + 1


        if playerHP <= 0:
            playerDeath = True
            print("Jeremy has fallen""\n")

        if allyHP <= 0:
            allyDeath = True
            print("Hilda has fallen""\n")


        if bossHP <= 0:
            bossDeath = True
            print("You Win!")
                



            
boss()
               
                    
                    
            
