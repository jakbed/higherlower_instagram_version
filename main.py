import assets
from game_data import data
import random

def find_bigger(number1, number2):
    if number1>number2:
        return 'a'
    elif number2<number2:
        return 'b'
    
print(assets.logo)


def game():
    end_game = False

    score = 0

    while end_game is False:
        
        random_numbers = []

        for i in range(2):
            number = random.randint(0, len(data)-1)
            random_numbers.append(number)

        followers_a = data[random_numbers[0]]['follower_count']
        followers_b = data[random_numbers[1]]['follower_count']

        print(f" A: {data[random_numbers[0]]['name']}, a {data[random_numbers[0]]['description']} from {data[random_numbers[0]]['country']}")
        print(assets.vs)
        print(f" B: {data[random_numbers[1]]['name']}, a {data[random_numbers[1]]['description']} from {data[random_numbers[1]]['country']}")

        player_choice = input("Who has more followers? type 'a' or 'b': ").lower()
        # player_choice = 'a'
        if player_choice == find_bigger(followers_a, followers_b):
            
                score +=1
                print(f"GOOD! Your score is {score}")
        
        else:
            print(f"\nSorry, thats wrong answer.\nYour final score is: {score}\n")
            end_game = True
    


game()
