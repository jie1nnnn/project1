import random

def escape_game():
    position = 0
    goal = 100
    supplies = 

    Print ("Wellcome to the escape game, you need to get from position 0 to position 100. You may encouter danger along the way!")

    while position < goal:
        try:
            step = int(input("please enter the namber of steps forward(1-3): "))
            if step not in [1, 2, 3]:
                print("please enter number between 1-3! ")
                continue

            
            
            position += step
            print ("You have moved {step} steps forward, current position:{position}")
            

#fire hazard challenge
def fire_challenge():
    right_options = [水]
    other_options = [土, 木]
    options = random.sample(other_options, 2) + ['水']
    random.shuffle(options)

    print("fire ahead!")
    print("please select the Chinese character corresponding to 'water' within three seconds!")
    for idx, opt in enumerate(options):
        print(f"{idx+1}. {opt}")


    signal.signal(signal.SIGNAL, timeout_handler) 
    signal.araim(3)
    try:
        answer = input("please enter the option number (1-3):)
        



        



            

                    


