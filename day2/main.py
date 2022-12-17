#Data Types
#Strings
print("hello")
print("hello"[0])
print("hello"[4])
print(len("hello"))
print("123" + "456")
#Integers
print(1)
print(123+456)
print(123_456_789)
#Floats
print(3.14159)
#Booleans
print(True)
print(False)

#Type Checking
num_char = len(input("what is your name?"))
print(type(num_char))

#Challenge 1

# 🚨 Don't change the code below 👇
two_digit_number = input("Type a two digit number: ")
# 🚨 Don't change the code above 👆

####################################
#Write your code below this line 👇
print(int(two_digit_number[0]) + int(two_digit_number[1]))

#Challenge 2

# 🚨 Don't change the code below 👇
height = input("enter your height in m: ")
weight = input("enter your weight in kg: ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
float_height = float(height)
float_weight = float(weight)
bmi = int(float_weight/float_height ** 2)
print(bmi)

# Challenge 3
# 🚨 Don't change the code below 👇
age = input("What is your current age? ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
age = int(age)
years_left = 90-age
months = years_left * 12
weeks = years_left * 52
days = int(years_left * 365.25) # dont for get leap years
print(f"You have {days} days, {weeks} weeks, and {months} months left.")


#Project for the Day
#If the bill was $150.00, split between 5 people, with 12% tip. 

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

#Write your code below this line 👇
bill = float(input("How much was the bill? "))
people = int(input("How many people to split between? "))
percent = 1 + (float(input("What percentage of tip do you want to leave? ")) / 100)
cost_per_person = (bill / people) * percent
print("${:,.2f}".format(cost_per_person))