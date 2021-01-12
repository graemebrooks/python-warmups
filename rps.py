import random


def rps():
    val = None
    outcomes = ["rock", "paper", "scissors"]
    comp_result = None
    while val != "q":
        comp_result = outcomes[random.randint(0, 2)]
        user_result = input("Type `rock`, `paper`, `scissors` to play or `q` to quit: ")
        print(f"You played {user_result}!")
        if user_result == "rock":
            if comp_result == "rock":
                print("Computer plays rock, draw!")
                continue
            elif comp_result == "scissors":
                print("Computer plays scissors, you win!")
                continue
            elif comp_result == "paper":
                print("Computer plays paper, you lose!")
                continue
        if user_result == "paper":
            if comp_result == "rock":
                print("Computer plays rock, you win!")
                continue
            elif comp_result == "scissors":
                print("Computer plays scissors, you lose!")
                continue
            elif comp_result == "paper":
                print("Computer plays paper, draw!")
                continue
        if user_result == "scissors":
            if comp_result == "scissors":
                print("Computer plays rock, you lose!")
                continue
            elif comp_result == "scissors":
                print("Computer plays scissors, draw!")
                continue
            elif comp_result == "paper":
                print("Computer plays paper, you win!")
                continue
        else:
            print("Adios!")
            break


rps()
