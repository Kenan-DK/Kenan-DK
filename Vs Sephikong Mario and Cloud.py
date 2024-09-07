import random


def sephikong():

    bossHP = 5000
    bossAttack = 80
    bossDeath = False

    marioHP = 500
    marioAttack = 60
    marioDeath = False

    cloudHP = 800
    cloudAttack = 70
    cloudDeath = False

    turn = 1
    magic = 50
    limit = 0
    itemNum = 5

    while bossDeath != True:
        print("\n""Turn:", turn)
        print("Limit:", limit)
        print("Items:", itemNum)
        print("Magic:", magic)
        
        if marioDeath != True:
            mAct = input("\n""What will Mario Do?""\n""Attack (a)""\n""Special (s)""\n""item (i)""\n""Limit Break (l)""\n")
            if mAct == "a":
                print("Mario Used Jump!")
                bossHP = bossHP - (marioAttack * 1.2)

            elif mAct == "s":
                special = input("Which Special will Mario use?""\n""Fire Flower (f)""\n""Green Shell (g)""\n")
                if special == "f":
                    print("Mario used a Fire Flower!""\n""Mario became Fire Mario!")
                    print("Mario used Fireball!")
                    bossHP = bossHP - (marioAttack * 1.35)

                elif special == "g":
                    print("Mario threw a Green Shell!")
                    bossHP = bossHP - (marioAttack * 1.45)

            elif mAct == "i":
                if itemNum == 0:
                    print("You have no items!")
                    
                else:
                    Mitem = input("Which item will Mario use""\n""Super Mushroom (s)""\n""Ether (e)""\n")
                    if Mitem == "s":
                       print("Mario used a Super Mushroom!")
                       marioHP = marioHP + 70
                       itemNum = itemNum - 1

                    elif Mitem == "e":
                       print("Mario used an Ether!")
                       magic = magic + 10
                       itemNum = itemNum - 1

            elif mAct == "l":
                if limit == 5:
                    print("Mario Used SuperStar Rush!")
                    bossHP = bossHP - (marioAttack * 2.5)
                    limit = limit - 5

                else:
                    print("You can't use that yet!")


        if cloudDeath != True:
            cAct = input("\n""What will Cloud Do?""\n""Attack (a)""\n""Materia (m)""\n""item (i)""\n""Limit Break (l)""\n")
            if cAct == "a":
                print("Cloud Used Slash!")
                bossHP = bossHP - (cloudAttack * 1.2)

            elif cAct == "m":
                if magic >= 0:
                     special = input("Which Materia will Cloud use?""\n""Ice (i)(15)""\n""Bolt2 (b)(25)""\n")
                     if special == "i":
                        print("Cloud used Ice!")
                        bossHP = bossHP - (cloudAttack * 1.3)
                        magic = magic - 15

                     elif special == "g":
                         print("Cloud used Bolt2!")
                         bossHP = bossHP - (cloudAttack * 1.45)
                         magic = magic - 25

            elif cAct == "i":
                if itemNum == 0:
                    print("You have no items!")
                    
                else:
                    citem = input("Which item will Mario use""\n""Super Mushroom (s)""\n""Ether (e)""\n")
                    if citem == "s":
                       print("Cloud used a Super Mushroom!")
                       cloudHP = cloudHP + 70
                       itemNum = itemNum - 1

                    elif citem == "e":
                       print("Cloud used an Ether!")
                       magic = magic + 10
                       itemNum = itemNum - 1

            elif cAct == "l":
                if limit >= 5:
                    limitbreak = input("What Limit Break Will Cloud Use?""\n""OmniSlash (o)""\n""Legacy Cross Slash (c)""\n")
                    if limitbreak == "o":
                        print("Cloud used Omnislash!")
                        for x in range(15):
                            bossHP = bossHP - (cloudAttack * 1.10)

                        limit = limit - 5

                    elif limitbreak == "c":
                        print("Cloud used Legacy Cross Slash!")
                        print("Zack's Spirit Appeared to lend a Hand!")
                        for x in range(3):
                            bossHP = bossHP - (cloudAttack * 1.25)
                        limit = limit - 5

            mikuAct = random.randint(1,3)
            if mikuAct == 1:
                print("\n""Hatsune Miku used Healing Song")
                marioHP = marioHP + 110
                cloudHP = cloudHP + 110

            elif mikuAct == 2:
                print("\n""Hatsune Miku used Jab-Cross")
                bossHP = bossHP - 85

            elif mikuAct == 3:
                print("\n""Hatsune Miku sent out Meloetta""\n""Meloetta and Miku used Harmonic Relic Song")
                for x in range(2):
                    bossHP = bossHP - 75
                    marioHP = marioHP + 40
                    cloudHP = cloudHP + 40



            sephikongAct = random.randint(1,4)

            if sephikongAct == 1:
                print("\n""Sephikong used Coconut Gun!")
                marioHP = marioHP - (bossAttack * 1.35)
                cloudHP = cloudHP - (bossAttack * 1.35)

            elif sephikongAct == 2:
                print("\n""Sephikong used THE CLAP!")
                marioHP = marioHP - (bossAttack * 1.55)
                cloudHP = cloudHP - (bossAttack * 1.55)

            elif sephikongAct == 3:
                print("\n""Sephikong used OctaSlash!")
                for x in range(8):
                    DKtarget = random.randint(1,2)
                    if DKtarget == 1:
                       marioHP = marioHP - (bossAttack * 1.25)

                    elif DKtarget == 2:
                       cloudHP = cloudHP - (bossAttack * 1.25)


            elif sephikongAct == 4:
                print("Sephikong used Firaga!")
                marioHP = marioHP - (bossAttack * 1.45)
                cloudHP = cloudHP - (bossAttack * 1.45)

            DKspecial = random.randint(1,3)

            if DKspecial == "1":
                print("Sephikong used BANANA SLAMMA SUPERNOVA!")
                marioHP = marioHP - (bossAttack * 1.75)
                cloudHP = cloudHP - (bossAttack * 1.75)


            print("\n""Mario's HP:", marioHP)
            print("Cloud's HP:", cloudHP)
            print("Sephikong's HP:", bossHP)

            if marioHP <= 0:
                marioDeath = True
                print("Mario has fallen!")

            if cloudHP <= 0:
                cloudDeath = True
                print("Cloud has fallen!")

            if marioDeath == True and cloudDeath == True:
                print("GAME OVER")

            if bossHP <= 0:
                print("Sephikong was defeated!""\n""You Win!")
                bossDeath = True

            limit = limit + 1
            turn = turn + 1
            magic = magic + 10




            
                    

sephikong()    

           
                
                    

                
