import random
cash = 200
current_cash = int()




def DKroulette():
 number1 = int(input("Pick a number: "))
 number2 = int(input("Pick another number: "))
 number3 = int(input("Pick one more number: "))
 
 if (number1) and (number2) and (number3) in range(0, 37):
     bet_amount = int(input("How much will you bet?: "))
     bet = (cash - bet_amount)
     current_cash = (cash - bet_amount)
     resultNumber = random.randint(1, 36)
     result = print("The result is", resultNumber)

     if (resultNumber == number1) or (resultNumber == number2) or (resultNumber == number3):
         print("A WINNER IS YOU!")
         prize = bet_amount*2
         reward = cash + (bet_amount*1.82)
         current_cash = reward
         print("You won £",prize(".2f"))
         print("Your total amount of cash is £",current_cash)

     else:
         print("TOO BAD!")
         amountLost = cash - bet_amount
         currentCash = amountLost
         print("You lost £",bet_amount)
         print("Your total amount of cash is £",current_cash)

     playAgain = str(input("Would you like to play again?: "))
     if playAgain == 'y':
         print(DKroulette())

     elif playAgain == 'n':
         print("Thanks for playing!")
         exit()
         

    
 else:
     print("THAT'S NOT ALLOWED!")

     return(DKroulette())





print(DKroulette())
