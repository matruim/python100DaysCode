# import random

# random_integer = random.randint(1,6)
# print(random_integer)

# random_float = random.random()
# print(random_float)


# # Challenge 1

# #Remember to use the random module
# #Hint: Remember to import the random module here at the top of the file. 🎲
# import random
# #Write the rest of your code below this line 👇
# if random.randint(0,1) == 1:
#     print("Heads")
# else:
#     print("Tails")

# # Challenge 2
# # Import the random module here
# import random
# # Split string method
# names_string = input("Give me everybody's Names, separated by a comma. ")
# Names = names_string.split(", ")
# # 🚨 Don't change the code above 👆

# #Write your code below this line 👇

# print(f"{random.choice(Names)} is going to buy the meal today!")


# # Challenge 3
# import random

# # 🚨 Don't change the code below 👇
# row1 = ["⬜️","️⬜️","️⬜️"]
# row2 = ["⬜️","⬜️","️⬜️"]
# row3 = ["⬜️️","⬜️️","⬜️️"]
# map = [row1, row2, row3]
# print(f"{row1}\n{row2}\n{row3}")
# position = input("Where do you want to put the treasure? ")
# # 🚨 Don't change the code above 👆

# #Write your code below this row 👇
# map[int(list(position)[1]) -1][int(list(position)[0]) -1] = "X"

# #Write your code above this row 👆

# # 🚨 Don't change the code below 👇
# print(f"{row1}\n{row2}\n{row3}")


# Challenge 4
# Go to https://replit.com/@appbrewery/rock-paper-scissors-start?v=1
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇
import random

game_images = [rock,paper,scissors]

choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper, or 2 for Scissors.\n"))
if choice <=2 and choice >= 0:
    game_images[choice]
    print("Computer Chose:")
    compChoice = random.randint(0,2)
    game_images[compChoice]

    outcomes = [
        ["It's a Draw","You Loose"," You Win"],
        ["You Win","It's a Draw","You Loose"],
        ["You Loose","You Win","It's a Draw"]
    ]

    print(outcomes[choice][compChoice])
else:
    print('You loose please select a valid number!')
