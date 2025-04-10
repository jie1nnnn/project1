import random

def escape_game():
    position = 0
    goal = 30
    supplies = 100
    health = 100

    print("Wellcome to the escape game, you need to get from position 0 to position 30. You may encouter danger along the way!")

    while position < goal:
        try:
            step = int(input("please enter the namber of steps forward(1-3): "))
            if step not in [1, 2, 3]:
                print("please enter number between 1-3! ")
                continue 
            
            position += step
            print ("You have moved {step} steps forward, current position:{position}")


            if random.random() < 0.2:

                event_type == random.choice(["fire", "tornado"])

                if event_type == "fire":
                    if not danger_event():
                        supplies = int(supplies * 0.75)
                        health = int(health * 0.75)
                        print(f"you failed and were returned to the starting point. Your current supplies are: {supplies}")
                        position = 0
                elif event_type == "tornado":
                    survived, health = danger_event_tornado(health)
                    if not survived:
                        position = 0

def danger_event():
    right_options = [水]
    other_options = [土, 木]
    options = random.sample(other_options, 2) + ['水']
    random.shuffle(options)

    print("fire ahead!")
    print("please select the Chinese character corresponding to 'water' within three seconds!")
    for idx, opt in enumerate(options):
        print(f"{idx+1}. {opt}")

    try:
        answer = input("please enter the option number (1-3):")
        if answer.isdigit() and int(answer) in [1, 2, 3]:
            if options[int(answer)-1] == '水':
               print("choose the right one and you move on.")
               return True
            else:
                print("wrong choice.")
                return False

        else:
            print("invalid input! ")
            return False
    except TimeoutError:
        print("\ntimeout! ")
        return False
        

def danger_event_tornado(health):
    print("\n you've encountered a dangerous event! ")
    print("The world is spining...the fate is about to be revealed! ")

    result = random.choice([1, 2])
    if result == 1:
        health = max(0, int(health * 0.9))
        print("You survived the tornado, but you are injured. -10%! ")
        return True, health
    else:
        print("You are returned to the starting point! ")
        return False































































































































































































































      
        
        



            

                    


