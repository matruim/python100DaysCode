# fruits = ["Apple", "Peach", "Pear"]
# for fruit in fruits:
#     print(fruit)


# # Challenge 1
# # 🚨 Don't change the code below 👇
# student_heights = input("Input a list of student heights ").split()
# for n in range(0, len(student_heights)):
#   student_heights[n] = int(student_heights[n])
# # 🚨 Don't change the code above 👆


# #Write your code below this row 👇
# height = 0
# length = 0
# for student in student_heights:
#   height += student
#   length += 1

# print(f"{round(height/length)}")


# # Challenge 2
# # 🚨 Don't change the code below 👇
# student_scores = input("Input a list of student scores ").split()
# for n in range(0, len(student_scores)):
#   student_scores[n] = int(student_scores[n])
# print(student_scores)
# # 🚨 Don't change the code above 👆

# #Write your code below this row 👇
# highscore = 0
# for score in student_scores:
#   if highscore < score:
#     highscore = score

# print(f"The highest score in the class is: {highscore}")


# # Challenge 3
# #Write your code below this row 👇
# sum = 0
# for n in range(2, 101, 2):
#     sum += n

# print(f"{sum}")


# # Challenge 4
# # Write your code below this row 👇
# for n in range(1, 101):
#     if n % 3 == 0 and n % 5 == 0:
#         print("FizzBuzz")
#     elif n % 3 == 0:
#         print("Fizz")
#     elif n % 5 == 0:
#         print("Buzz")
#     else:
#         print(n)


# Challenge 5
# Go to: https://replit.com/@appbrewery/password-generator-start?v=1
# import random
# letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
# numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
# symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

# print("Welcome to the PyPassword Generator!")
# nr_letters = int(input("How many letters would you like in your password?\n")) 
# nr_symbols = int(input(f"How many symbols would you like?\n"))
# nr_numbers = int(input(f"How many numbers would you like?\n"))

# #Eazy Level
# # password = ""

# # for char in range(1, nr_letters + 1):
# #   password += random.choice(letters)

# # for char in range(1, nr_symbols + 1):
# #   password += random.choice(symbols)

# # for char in range(1, nr_numbers + 1):
# #   password += random.choice(numbers)

# # print(password)

# #Hard Level
# password_list = []

# for char in range(1, nr_letters + 1):
#   password_list.append(random.choice(letters))

# for char in range(1, nr_symbols + 1):
#   password_list += random.choice(symbols)

# for char in range(1, nr_numbers + 1):
#   password_list += random.choice(numbers)

# print(password_list)
# random.shuffle(password_list)
# print(password_list)

# password = ""
# for char in password_list:
#   password += char

# print(f"Your password is: {password}")

import random
alphas = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
nums = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
special = ['!', '#', '$', '%', '&', '(', ')', '*', '+','@']

def random_password(length: int, useNums: bool, useSpecial: bool):
    password_chars = []
    if useNums:
        i = 0
        while i < random.randint(1, password_length):
            password_chars.append(random.choice(nums))
            i += 1

    if useSpecial:
        i = 0
        while i < random.randint(1, password_length - len(password_chars)):
            password_chars.append(random.choice(special))
            i += 1

    for n in range(1, password_length - len(password_chars) +1):
        password_chars.append(random.choice(alphas))

    i = 0
    while i < 5: 
        random.shuffle(password_chars)
        i += 1


    password = ""
    for c in password_chars:
        password += c
    return password

print("Welcome to the PyPassword Generator!")
password_length = int(input("How many characters do you need your password to be?"))
useNums = input("Do you need to use numbers? (y/n): ").lower().strip() == 'y'
useSpecial = input("Do you need to use special characters? (y/n): ").lower().strip() == 'y'
for n in range (1, random.randint(1,6)):
    print(random_password(password_length, useNums, useSpecial))