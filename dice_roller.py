import random


def dice_roller():
    val = None
    while val != "n":
        val = input("Press 'y' to roll die, press 'n' to quit: ")
        if val == "y":
            print(random.randint(1, 6))
        else:
            print("Adios!")

dice_roller()