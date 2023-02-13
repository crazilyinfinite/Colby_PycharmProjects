import a10P2

# Welcome UI
print("#"*80)
print("Roshambo!!!")
print("#"*80)

# loop the program
while (True):
    player = input("What would you like to use? Rock (1), Paper (2), Scissors (3): ")
    a10P2.rock()
    player = input("What would you like to use? Rock (1), Paper (2), Scissors (3): ")
    a10P2.paper()
    player = input("What would you like to use? Rock (1), Paper (2), Scissors (3): ")
    a10P2.paper()
    player = input("What would you like to use? Rock (1), Paper (2), Scissors (3): ")
    a10P2.scissors()
    print("You have completed the game!")

    again = input("Play again?")
    if again != "y":
        break