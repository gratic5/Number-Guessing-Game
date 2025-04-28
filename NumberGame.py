import random



logo =r""" 
 /$$   /$$                         /$$                            /$$$$$$                                   
| $$$ | $$                        | $$                           /$$__  $$                                  
| $$$$| $$ /$$   /$$ /$$$$$$/$$$$ | $$$$$$$   /$$$$$$   /$$$$$$ | $$  \__/  /$$$$$$  /$$$$$$/$$$$   /$$$$$$ 
| $$ $$ $$| $$  | $$| $$_  $$_  $$| $$__  $$ /$$__  $$ /$$__  $$| $$ /$$$$ |____  $$| $$_  $$_  $$ /$$__  $$
| $$  $$$$| $$  | $$| $$ \ $$ \ $$| $$  \ $$| $$$$$$$$| $$  \__/| $$|_  $$  /$$$$$$$| $$ \ $$ \ $$| $$$$$$$$
| $$\  $$$| $$  | $$| $$ | $$ | $$| $$  | $$| $$_____/| $$      | $$  \ $$ /$$__  $$| $$ | $$ | $$| $$_____/
| $$ \  $$|  $$$$$$/| $$ | $$ | $$| $$$$$$$/|  $$$$$$$| $$      |  $$$$$$/|  $$$$$$$| $$ | $$ | $$|  $$$$$$$
|__/  \__/ \______/ |__/ |__/ |__/|_______/  \_______/|__/       \______/  \_______/|__/ |__/ |__/ \_______/
"""
def start():

    while(True):
        print()
        d1 = input("Do you wish to play the number guessing game? ")
        print(logo)
        if d1.lower() in ["y","yes"]:
            print("Welcome!")
            print()
            choice1 = input("Choose a difficulty, Easy or Hard: ")
            print()

            print("I'm thinking of a number between 1 and 100.")
            number = random.choice(list(range(1,101)))
            print()

            if choice1.lower() in ["h","hard"]:
                lives = 5

            elif choice1.lower() in ["e","easy"]:
                lives = 10

            flag = False
            while(lives > 0):
                
                print(f"You have {lives} {'attempts' if lives > 1 else 'attempt'} remaining to guess the number.")
                a1 = int(input("Make a guess: "))
                print()

                if a1 == number:
                    print()
                    print("Congratulations!")
                    print(f"the number was {number}")
                    print()
                    flag = True
                    break

                elif a1 < number:
                    print("Too low")
                    print()
                    lives -= 1

                elif a1 > number:
                    print("Too high")
                    print()
                    lives -= 1
            if not flag:
                print("You lose")
                print(f"The number was {number}")
        else:
            break

start()
