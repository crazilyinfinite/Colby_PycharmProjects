# Welcome UI
print("#"*80)
print("Roshambo!!!")
print("#"*80)

# rules for decisions
def rock():
    if player == "1":
        print("Tie")
    elif player == "2":
        print("You win!")
    elif player == "3":
        print("You lose")
    else:
        print("Invalid")


def paper():
    if player == "1":
        print("You lose")
    elif player == "2":
        print("Tie")
    elif player == "3":
        print("You win!")
    else:
        print("Invalid")


def scissors():
    if player == "1":
        print("You win")
    elif player == "2":
        print("You lose!")
    elif player == "3":
        print("Tie")
    else:
        print("Invalid")


# loop the program
while (True):
    player = input("What would you like to use? Rock (1), Paper (2), Scissors (3): ")
    rock()
    player = input("What would you like to use? Rock (1), Paper (2), Scissors (3): ")
    paper()
    player = input("What would you like to use? Rock (1), Paper (2), Scissors (3): ")
    paper()
    player = input("What would you like to use? Rock (1), Paper (2), Scissors (3): ")
    scissors()
    print("You have completed the game!")

    again = input("Play again?")
    if again != "y":
        break