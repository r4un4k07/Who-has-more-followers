from data import data
import random
import os

os.system('cls')

def user_input():
    test = input("Who has more followers on instagram? A or B: ")
    if test == 'A' or test == "B":
        return test
    else:
        print("Please enter valid choice!")
        return user_input()

score = 0
game = True

print("Welcome to the game of Higher and Lower!!\n")

while game:
    option_a = random.choice(data)
    option_b = random.choice(data)
    while option_a == option_b:
        option_b = random.choice(data)
    print(f"Choice A: {option_a['name']}, {option_a['description']}, from {option_a['country']}.\n")
    print('VS\n')
    print(f"Choice B: {option_b['name']}, {option_b['description']}, from {option_b['country']}.\n")
    
    # print("A: " + str(option_a['follower_count']))
    # print("B: " + str(option_b['follower_count']))
    
    test = user_input()
    
    if test == 'A':
        if option_a['follower_count'] < option_b['follower_count']:
            game = False
            continue
    elif test == 'B':
        if option_a['follower_count'] > option_b['follower_count']:
            game = False
            continue
    
    score += 1
    print("\nNext turn:\n")
    
    
print(f"\nGame Over! Score {score}")