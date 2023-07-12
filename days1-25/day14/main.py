from art import logo, vs
import random
from game_data import data

def get_random_person():
    """
    Randomly selects and returns a person from the data list.
    
    The function shuffles the data list to ensure randomness, and then pops and returns the last element.
    """
    random.shuffle(data)
    return data.pop()


def get_user_choice(a: dict, b: dict):
    """
    Prints the information about two people and prompts the user for a choice.
    
    Args:
        a (dict): A dictionary representing person A with name, description, and country information.
        b (dict): A dictionary representing person B with name, description, and country information.
    
    Returns:
        str: The user's choice, either 'a' or 'b', representing their selection.
    """
    print(f"Compare A: {a['name']}, {a['description']}, from {a['country']}.")
    print(vs)
    print(f"Against B: {b['name']}, {b['description']}, from {b['country']}.")
    return input("Who has more followers? Type 'A' or 'B': ").lower()


print(logo)

score = 0
a = get_random_person()
while True:
    b = get_random_person()

    choice = get_user_choice(a, b)

    if (choice == 'a') == (a['follower_count'] < b['follower_count']):
        print("Good job!")
        score += 1
        a = b
    else:
        print("Too bad!")
        break

print(f"Score: {score}\n")
