from threading import Thread
from time import sleep

import random


_TIME_OUT = [False, False]

_TIME_LIMIT = 1

class MyThread(Thread):
    def __init__(self, time_out, player):
        Thread.__init__(self)
        self.time_out = time_out
        self.player = player

    def run(self):
        sleep(self.time_out)
        _TIME_OUT[self.player - 1] = True
        print('\a', end="") # Make a noise

def main():
    _TIME_OUT[0] = False
    _TIME_OUT[1] = False

    tread_1 = MyThread(_TIME_LIMIT, 1)

    n = random.randint(1, 99)
    chances = 5

    
    tread_1.start()
    print(f"You have {_TIME_LIMIT} sec")

    guess = int(input("Player 1 please enter an integer from 1 to 99, you have 5 chances: " ))
    while n != "guess" and not _TIME_OUT[0]:
        print(not _TIME_OUT, _TIME_OUT)
        chances -=1
        if chances == 0:
            print("out of chances, it is now player 2's turn to play. The number was", n)
            break
        if guess < n:
            print("guess is low you have",chances,"chances left")
            guess = int(input("Enter an integer from 1 to 99: "))
        elif guess > n:
            print ("guess is high you have",chances, "chances left")
            guess = int(input("Enter an integer from 1 to 99: "))
        else:
            print("you guessed it and have", chances, "chances left")
            break
            
    if _TIME_OUT:
        print("Sorry, out of time!")

    tread_2 = MyThread(_TIME_LIMIT, 2)

    n1 = random.randint(1, 99)
    chances1 = 0

    tread_2.start()
    print(f"You have {_TIME_LIMIT} sec")

    guess1 = int(input("Player 2 please enter an integer from 1 to 99, you have 5 chances: "))
    while n1 != "guess" and not _TIME_OUT[1]:
        chances1 +=1
        if chances1 ==5:
            print("out of chances, the number was", n1)
            break
        if guess1 < n1:
            print("guess is low you have",chances1,"chances left")
            guess1 = int(input("Enter an integer from 1 to 99: "))
        elif guess > n1:
            print ("guess is high you have",chances1, "chances left")
            guess1 = int(input("Enter an integer from 1 to 99: "))
        else:
            print("you guessed it and have", chances1, "chances left")
            break

    if _TIME_OUT:
        print("Sorry, out of time!")

    retry=input("would you like to play again? (please choose either 'yes' or 'no' )")
    if retry == "yes":
        main()
    elif retry == "no":
        print("Okay. have a nice day! :D ")
    else:
        print("Invalid input")


if __name__ == "__main__":
    main()