import random

cash = 200
currentCash = ()

def DKroulette():
 number1 = int(input("DK: Pick a number: "))
 number2 = int(input("Diddy: Pick another number: "))
 number3 = int(input("DK: and Pick one more number: "))
 if (number1) and (number2) and (number3) in range(0, 37):
     amountBet = int(input("DK: How much will you bet?: "))
     bet = (cash - amountBet)
     resultNumber = random.randint(1, 36)
     result = print("Diddy: The result is number", resultNumber)
     if (resultNumber == number1) or (resultNumber == number2) or (resultNumber == number3):
         print("DK: A WINNER IS YOU!")
         prize = amountBet*2
         reward = cash + (amountBet*2)
         currentCash = reward
         print("Diddy: You won £",prize)
         print("DK: Your total amount of cash is £",currentCash)

     else:
         print("Diddy: TOO BAD!")
         amountLost = cash - amountBet
         currentCash = amountLost
         print("DK: You lost £",currentCash)
         print("Diddy: Your total amount of cash is £",currentCash)

     playAgain = str(input("DK: Would you like to play again?: "))
     if playAgain == 'yes':
         print("DK: Well then, lets go!")
         print(" ")
         print(DKroulette())

     else:
         print("Diddy: Well then CYA!")
         exit()
 else:
     print("DK: HEY THAT'S NOT ALLOWED!")

     return(DKroulette())


def intro():
    print("He-he-here we go!")
    print("So they're finally here,")
    print("Performing for you.")
    print("if you want to play,")
    print("You can join in too")
    print("put your hands together")
    print("if you want to clap,")
    print("as we take you through")
    print("THIS MONKEY RAP! HUH!")
    print(" ")
    print("???: Welcome to the kongo bongo island casino, ")
    print("???: I'm the oldest wisest ape you'll ever meet")
    print("???: Cranky!")
    print("Cranky: here you can play casino games,")
    print("Cranky: but only roulette can be played at the moment")
    print("Cranky: Go see Donkey Kong to play while the others set up.")
    print("Cranky: AND LEAVE ME TO SLEEP!")
    print(" ")
    
    print(DKintro())
    return(intro())


def DKintro():
    print("???: Hey there, you must be here to play!")
    print("???: I'm the future ruler of Kongo Bongo,")
    print("DK: Donkey Kong!")
    print("DK: Hey little buddy! We have our first player!")
    print("???: Heya! I'm DK's little buddy and sidekick!")
    print("Diddy: Diddy Kong!")
    print("Diddy: Now lets play!")
    print(" ")
    print(DKroulette())

print(intro())

    
