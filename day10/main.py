# # Functions with outputs
# def format_name(f_name, l_name):
#     formated_f_name = f_name.title()
#     formated_l_name = l_name.title()

#     return (f"{formated_f_name} {formated_l_name}")


# formated_string = format_name("jaRed", "GOOD")
# print(formated_string)


# # Challenge 1
# def is_leap(year):
#   if year % 4 == 0:
#     if year % 100 == 0:
#       if year % 400 == 0:
#         return True
#       else:
#         return False
#     else:
#       return True
#   else:
#     return False

# def days_in_month(year, month):
#     month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]  
#     if is_leap(year) and month - 1 == 1:
#         return 29  
#     else:
#       return month_days[month -1]
  
# #🚨 Do NOT change any of the code below 
# year = int(input("Enter a year: "))
# month = int(input("Enter a month: "))
# days = days_in_month(year, month)
# print(days)



# # Python Calc
#  # Add
# def add(n1, n2):
#     """Takes two numbers and adds them together."""
#     return n1+n2

# # Subtract
# def subtract(n1,n2):
#     """Takes two numbers and subtracts the second from the first (IE: 1 - 2)"""
#     return n1-n2

# # Multiply
# def multiply(n1,n2):
#     """Takes two numbers and multiplies them together"""
#     return n1*n2

# # Divide
# def divide(n1,n2):
#     """Takes two numbers and checks that the second number isn't 0 and then divides them"""
#     if(n2 == 0): return "Divide by Zero Error"
#     return n1/n2

# operations = {
#     '+': add,
#     '-': subtract,
#     '*': multiply,
#     '/': divide,
# }

# num1 = int(input("What is the first number?: "))
# while True:
#     for symbol in operations:
#         print(symbol)
#     operations_symbol = input("Pick an operation from the line above: ")
#     num2 = int(input("What is the second number?: "))


#     answer = operations[operations_symbol](num1, num2)

#     print(f"{num1} {operations_symbol} {num2} = {answer}")

#     keepGoing = input(f"Type y to continue calculating with {answer}, or type 'n' to exit.: ")
#     if keepGoing == 'n':
#         break



# Calculator

from art import logo

class DivideByZeroError(Exception):
    pass

def divide(n1, n2):
    """Takes two numbers and divides the first by the second."""
    if n2 == 0:
        raise DivideByZeroError("Cannot divide by zero")
    return n1 / n2

operations = {
    '+': lambda n1, n2: n1 + n2,
    '-': lambda n1, n2: n1 - n2,
    '*': lambda n1, n2: n1 * n2,
    '/': divide,
}

def calculator():
    print(logo)
    num1 = float(input("What is the first number?: "))
    should_continue = True
    while should_continue:
        print("Available operations:", ", ".join(operations.keys()))
        operation = input("Enter the operation in the format 'operator operand': ")
        operator, *operands = operation.split()
        num2 = float(operands[0]) if operands else int(input("What is the second number?: "))

        try:
            answer = operations[operator](num1, num2)
        except DivideByZeroError as e:
            print(e)
            break

        print(f"{num1} {operator} {num2} = {answer}")

        keep_going = input(f"Type 'y' to continue calculating with {answer}, or type 'n' to start over, or type e to exit: ")
        if keep_going.lower() == 'n':
            should_continue = False
            calculator()
        elif keep_going.lower() == 'e':
            should_continue = False
        elif keep_going.lower() == 'y':
            num1 = answer


calculator()