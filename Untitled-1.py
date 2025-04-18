import random

def escape_game():
    position = 0
    goal = 30
    supplies = 100
    health = 100
    skip_token = 0

    print("Welcome to the escape game! You need to get from position 0 to 30. You may encounter danger along the way!")

    while position < goal:
        try:
            step = int(input("Please enter the number of steps forward (1-3): "))
            if step not in [1, 2, 3]:
                print("Please enter a number between 1 and 3!")
                continue

            position += step
            print(f"You have moved {step} steps forward. Current position: {position}")

        except ValueError:
            print("Please enter a valid number!")
            continue

        if random.random() < 0.4:
            event_type = random.choice(["fire", "tornado", "flood"])

            if event_type == "fire":
                if not danger_event():
                    supplies = int(supplies * 0.75)
                    health = int(health * 0.75)
                    print(f"You failed and were returned to the starting point. Supplies: {supplies}, Health: {health}")
                    position = 0
            elif event_type == "tornado":
                survived, health = danger_event_tornado(health)
                if not survived:
                    position = 0
            elif event_type == "flood":
                position, health = danger_event_flood(health, position, step)


        skip_token = find_random_item(skip_token)

    print("\n Congratulations! You escaped successfully!")

def find_random_item(skip_token):
    if random.random() < 0.2:
        print("You found a backpack! You get a token to skip a dangerous event.")
        skip_token += 1
    return skip_token

def danger_event():
    options = ["水", "土", "木"]
    choices = random.sample(options, 3)

    print(" Fire ahead!")
    print("Please select the Chinese character for 'water' !")
    for idx, opt in enumerate(choices):
        print(f"{idx+1}. {opt}")

    answer = input("Enter the option number (1-3): ")
    if answer.isdigit() and int(answer) in [1, 2, 3]:
        if choices[int(answer)-1] == '水':
            print("Correct choice! You move on.")
            return True
        else:
            print("Wrong choice.")
            return False
    else:
        print("Invalid input!")
        return False

def danger_event_tornado(health):
    print("\n Tornado encountered!")
    print("The world is spinning... fate will be decided!")

    result = random.choice([1, 2])
    if result == 1:
        health = max(0, int(health * 0.9))
        print("You survived the tornado, but you're injured. Health -10%.")
        return True, health
    else:
        print("You were blown back to the starting point!")
        return False, health

def danger_event_flood(health, position, step):
    print("\n Flood ahead!")
    print("1. Swim over (50% success)\n2. Take a detour (safe but one step back)")

    choice = input("Enter your choice (1 or 2): ")

    if choice == "1":
        if random.random() < 0.5:
            print("You swam through the flood successfully!")
            return position, health
        else:
            health = max(0, int(health * 0.8))
            print("You were swept back to the start. Health -20%.")
            return 0, health
    elif choice == "2":
        position = max(0, position - step)
        print(f"You chose to detour. Safe escape, but moved back to position {position}.")
        return position, health

    else:
        print("Invalid choice.")
        return position, health

escape_game()






    
    













































































































































































































      
        
        



            

                    


