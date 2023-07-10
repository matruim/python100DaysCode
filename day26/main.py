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


with open("file1.txt") as file1:
    with open("file2.txt") as file2:
        data1 = [int(n.strip()) for n in file1]
        data2 = [int(n.strip()) for n in file2]
        result = [d for d in data1 if d in data2]
# Write your code above 👆

print(result)
