import random
cash = 200
current_cash = int()




def Slots():
    lanes = ['bell', 'cherry', '7', 'bar', 'lemon',
             'watersmoothis', 'double bar', 'triple bar']

    lane_one = random.randint(0, 7)
    lane_two = random.randint(0, 7)
    lane_three = random.randint(0, 7)

    bet_amount = int(input("how much will you bet: "))
    current_cash = (cash - bet_amount)
    prize = (bet_amount * 1.30)

    print (lanes[lane_one],",", lanes[lane_two],",", lanes[lane_three])

    if (lane_one == lane_two) and (lane_one == lane_three):
        print("JACKPOT!!")
        print("You won", prize("%.2f"))

    else:
        print("Too Bad!")
        print("print you have: £",current_cash)


    play_again = str(input("Want to play again?: "))
    if play_again == 'y':
         print(Slots())

    elif play_again == 'n':
         print("Thanks for playing!")
         exit()

    else:
         exit()


         return(Slots())





print(Slots())
