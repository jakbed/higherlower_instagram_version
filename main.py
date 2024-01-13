import assets
from game_data import data
import random

def find_bigger(number1, number2):
    if number1>number2:
        return True
    elif number2<number2:
        return False
    
print(assets.logo)

score = 0
end_game = False

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

    print(f"___test_only_______{followers_a} vs {followers_b}")

    player_choice = input("Who has more followers? type 'a' or 'b': ")
    if player_choice=='a':
        if find_bigger(followers_a, followers_b):
            print("\n"*10)
            print(f"GOOD! Your score is {score}")
            score +=1
        else:
            end_game = True
    elif player_choice=='b':
        if not find_bigger(followers_a, followers_b):
            print("\n"*10)
            print(f"GOOD! Your score is {score}")
            score += 1
        else:
            end_game = True
print(f"\nYour final score is: {score}")