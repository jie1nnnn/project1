import random

def escape_game():
    position = 0
    goal = 100

    Print ("Wellcome to the escape game, you need to get from position 0 to position 10. You may encouter danger along the way!")

    while position < goal:
        try:
            step = int(input("please enter the namber of steps forward(1-3): "))
            if step not in [1, 2, 3]:
                print("please enter number between 1-3! ")
                continue


