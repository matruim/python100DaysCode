# numbers = [1, 2, 3]
# # new_numbers = [new_item for item in list]
# new_numbers = [n + 1 for n in numbers]
# print(numbers)
# print(new_numbers)
#
# name = "Jared"
# letters = [letter for letter in name]
# print(name)
# print(letters)
#
# squares = [n*n for n in numbers]
# print(squares)
#
# doubles = [n*2 for n in range(1, 5)]
# print(doubles)
#
# # conditional list comprehension
# # new_list = [ new_item for item in list if condition ]
# names = ["Alex", "Beth", "Caroline", "Dave", "Elanor", "Freddie"]
# short_names = [name for name in names if len(name) < 5]
# print(names)
# print(short_names)
# long_names = [name.upper() for name in names if len(name) >= 5]
# print(long_names)
#
# with open("file1.txt") as file1:
#     with open("file2.txt") as file2:
#         data1 = [int(n.strip()) for n in file1]
#         data2 = [int(n.strip()) for n in file2]
#         result = [d for d in data1 if d in data2]
# # Write your code above 👆
#
# print(result)


# Dictionary Comprehensions
# new_dict = {new_key:new_value for item in list}
# new_dict = {new_key:new_value for (key, value) in dict.items()}
# new_dict = {new_key:new_value for (key, value) in dict.items() if condition}
# import random
#
# names = ["Alex", "Beth", "Caroline", "Dave", "Elanor", "Freddie"]
# student_scores = {student: random.randint(1, 100) for student in names}
# print(student_scores)
#
# passed_students = {student: score for (student, score) in student_scores.items() if score >= 70}
# print(passed_students)
#
#
# sentence = "What is the Airspeed Velocity of an Unladen Swallow?"
# # Don't change code above 👆
#
# # Write your code below:
# result = {word: len(word) for word in sentence.split()}
#
#
# print(result)
#
#
# weather_c = {
#     "Monday": 12,
#     "Tuesday": 14,
#     "Wednesday": 15,
#     "Thursday": 14,
#     "Friday": 21,
#     "Saturday": 22,
#     "Sunday": 24,
# }
# # 🚨 Don't change code above 👆
#
#
# # Write your code 👇 below:
# weather_f = {day: round(c * (9/5) + 32, 1) for (day, c) in weather_c.items()}
#
#
# print(weather_f)
#
# student_dict = {
#     "student": ["Angela", "James", "Lily"],
#     "score": [56,76,98]
# }
# for (key, value) in student_dict.items():
#     print(value)
#
# import pandas
# student_data_frame = pandas.DataFrame(student_dict)
# print(student_data_frame)
# for (key,value) in student_data_frame.items():
#     print(value)
#
# for (index, row) in student_data_frame.iterrows():
#     print(row.student, row.score)

