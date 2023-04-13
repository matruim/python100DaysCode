
# programming_dictionary = {
#     "Bug": "An error in a program that prevents the program from running as expected.",
#     "Function": "A piece of code that you can easily call over and over again.",
# }

# print(programming_dictionary["Bug"])

# programming_dictionary["Loop"] = "The action of doing something over and over again."

# print(programming_dictionary)


# empty_dictionary = {}

# #wipe dictionary
# # programming_dictionary = empty_dictionary

# # print(programming_dictionary)

# programming_dictionary["Bug"] = "A Moth in your computer."

# print(programming_dictionary["Bug"])

# #Loop
# for key in programming_dictionary:
#     print(key)
#     print(programming_dictionary[key])


# # Challenge 1

# student_scores = {
#   "Harry": 81,
#   "Ron": 78,
#   "Hermione": 99, 
#   "Draco": 74,
#   "Neville": 62,
# }
# # 🚨 Don't change the code above 👆

# #TODO-1: Create an empty dictionary called student_grades.
# student_grades = {}


# #TODO-2: Write your code below to add the grades to student_grades.👇
# for student, score in student_scores.items():
#     if score > 90:
#         student_grades[student] = "Outstanding"
#     elif score > 80:
#         student_grades[student] = "Exceeds Expectations"
#     elif score > 70:
#         student_grades[student] = "Acceptable"
#     else:
#         student_grades[student] = "Fail"

# # 🚨 Don't change the code below 👇
# print(student_grades)


# Nesting
# travel_log = {
#     "France": ["Paris", "Lille", "Dijon"],
#     "Germany": ["Berlin", "Hamburg", "Stuttgart"]
# }

# travel_log = {
#     "France": { "cities_visited": ["Paris", "Lille", "Dijon"], "total_visits": 12},
#     "Germany": {"cities_visited":["Berlin", "Hamburg", "Stuttgart"], "total_visits": 2}
# }

# travel_log = [
#     {
#         "country":"France", 
#         "cities_visited": ["Paris", "Lille", "Dijon"],
#         "total_visits": 12,
#     },
#     {
#         "country":"Germany", 
#         "cities_visited": ["Berlin", "Hamburg", "Stuttgart"],
#         "total_visits": 5,
#     }
# ]

# #Challenge 2

# travel_log = [
# {
#   "country": "France",
#   "visits": 12,
#   "cities": ["Paris", "Lille", "Dijon"]
# },
# {
#   "country": "Germany",
#   "visits": 5,
#   "cities": ["Berlin", "Hamburg", "Stuttgart"]
# },
# ]
# #🚨 Do NOT change the code above

# #TODO: Write the function that will allow new countries
# #to be added to the travel_log. 👇
# def add_new_country(country, visits, cities):
#     travel_log.append({"country":country, "visits":visits, "cities":cities})




# #🚨 Do not change the code below
# add_new_country("Russia", 2, ["Moscow", "Saint Petersburg"])
# print(travel_log)


import os
from art import logo, fireworks

def clear(): return os.system('clear')

def get_bid():
    name = input("What is your name?: ")
    bid = float(input("What's your bid in dollars?: $"))
    bids[name] = bid

def check_winner(bidding_record):
    highest_bid = 0
    winner = None
    for bidder, bid_amount in bidding_record.items():
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder
    print(fireworks)
    print(f"Sold to {winner} for ${highest_bid}!")



clear()

print(logo)

bids = {}
print("Welcome to the secret auction program.")


while True:
    get_bid()
    isDone = input("Are there any other bidders? Type 'yes' or 'no': ")
    if isDone == 'no' or isDone == 'n':
        break;
    clear()

check_winner(bids)