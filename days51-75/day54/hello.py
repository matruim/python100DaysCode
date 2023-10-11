# import time
#
#
# from flask import Flask
#
# app = Flask(__name__)
#
#
# @app.route('/')
# def hello_world():
#     return "Hello, World"
#
# @app.route('/bye')
# def bye():
#     return "Bye"
#
#
# if __name__ == "__main__":
#     app.run()

#
# def delay_decorator(function):
#     def wrapper_function():
#         time.sleep(2)
#         function()
#
#     return wrapper_function
#
#
# @delay_decorator
# def say_hello():
#     print("hello")
#
#
# @delay_decorator
# def say_bye():
#     print("bye")
#
#
# def say_greeting():
#     print("how are you?")
#
#
# say_hello()
# say_bye()
# say_greeting()


# Challenge 1
import time

current_time = time.time()
print(current_time)  # seconds since Jan 1st, 1970


# Write your code below 👇

def speed_calc_decorator(function):
    def wrapper_function():
        function()
        end_time = time.time()
        print(f"{function.__name__} run speed: {end_time - current_time}")

    return wrapper_function


@speed_calc_decorator
def fast_function():
    for i in range(1000000):
        i * i


@speed_calc_decorator
def slow_function():
    for i in range(1000000):
        i * i


fast_function()
slow_function()
