# def greet():
#     print("Hello")
#     print("How do you do?")
#     print("Isn't the weather nice today?")

# greet()

# def greet_with_name(name):
#     print(f"Hello {name}")
#     print(f"How do you do {name}?")


# greet_with_name("Jared")

# def greet_with(name, location):
#     print(f"Hello {name}")
#     print(f"Isn't the weather nice today in {location}?")

# greet_with("Jared", "Exeter")
# greet_with(location="Visalia", name="Jon")


# #Write your code below this line 👇
# def paint_calc(height, width, cover):
#     print(f"You'll need {round((height * width) / cover)} cans of paint.")






# # #Write your code above this line 👆
# # # Define a function called paint_calc() so that the code below works.   

# # # 🚨 Don't change the code below 👇
# # test_h = int(input("Height of wall: "))
# # test_w = int(input("Width of wall: "))
# # coverage = 5
# # paint_calc(height=test_h, width=test_w, cover=coverage)


# #Write your code below this line 👇
# def prime_checker(number):
#     ifPrime = True
#     if number == 1: 
#         print("It's not a prime number.")
#     elif number > 1:
#         for i in range(2, number):
#             if number % i == 0:
#                 isPrime = False
#                 break 
    
#     if isPrime:
#         print("It's a prime number.")
#     else:
#         print("It's not a prime number.")


# #Write your code above this line 👆
    
# #Do NOT change any of the code below👇
# n = int(input("Check this number: "))
# prime_checker(number=n)


# # Casear Cipher 1
# alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

# direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
# text = input("Type your message:\n").lower()
# shift = int(input("Type the shift number:\n"))

# #TODO-1: Create a function called 'encrypt' that takes the 'text' and 'shift' as inputs.
# def encrypt(text, shift):
#     #TODO-2: Inside the 'encrypt' function, shift each letter of the 'text' forwards in the alphabet by the shift amount and print the encrypted text.  
#     #e.g. 
#     #plain_text = "hello"
#     #shift = 5
#     #cipher_text = "mjqqt"
#     #print Output: "The encoded text is mjqqt"

#     ##HINT: How do you get the index of an item in a list:
#     #https://stackoverflow.com/questions/176918/finding-the-index-of-an-item-in-a-list

#     ##🐛Bug alert: What happens if you try to encode the word 'civilization'?🐛
#     max_value = len(alphabet)
#     new_chars = ""
#     for letter in text:
#         new_index = alphabet.index(letter) + shift
#         if new_index > max_value:
#             new_index -= max_value
#             new_chars += alphabet[new_index]
#         else:
#             new_chars += alphabet[new_index]
#     return new_chars
# #TODO-3: Call the encrypt function and pass in the user inputs. You should be able to test the code and encrypt a message.
# print(encrypt(text, shift))



# # Casear Cipher 2
# alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

# direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
# text = input("Type your message:\n").lower()
# shift = int(input("Type the shift number:\n"))

# def encrypt(plain_text, shift_amount):
#   max_index = len(alphabet) - 1
#   cipher_text = ""
#   for letter in plain_text:
#     new_position = alphabet.index(letter) + shift_amount
#     if new_position > max_index:
#        new_position -= max_index
#     cipher_text += alphabet[new_position]
#   print(f"The encoded text is {cipher_text}")

# #TODO-1: Create a different function called 'decrypt' that takes the 'text' and 'shift' as inputs.
# def decrypt(cipher_text, shift_amount):

#   #TODO-2: Inside the 'decrypt' function, shift each letter of the 'text' *backwards* in the alphabet by the shift amount and print the decrypted text.  
#   #e.g. 
#   #cipher_text = "mjqqt"
#   #shift = 5
#   #plain_text = "hello"
#   #print Output: "The decoded text is hello"
#   max_index = len(alphabet) - 1
#   plain_text = ""
#   for letter in cipher_text:
#     new_position = alphabet.index(letter) - shift_amount
#     if new_position < 0:
#       new_position += max_index
#     plain_text += alphabet[new_position]
#   print(f"The decoded text is {plain_text}")


# #TODO-3: Check if the user wanted to encrypt or decrypt the message by checking the 'direction' variable. 
# # Then call the correct function based on that 'drection' variable. You should be able to test the code to encrypt *AND* decrypt a message.
# if direction == "encode":
#   encrypt(plain_text=text, shift_amount=shift)
# elif direction == "decode":
#   decrypt(cipher_text=text, shift_amount=shift)



# # Casear Cipher 3
# alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

# direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
# text = input("Type your message:\n").lower()
# shift = int(input("Type the shift number:\n"))

# #TODO-1: Combine the encrypt() and decrypt() functions into a single function called caesar(). 

# def casear(passed_text, shift_amount, direction):
#     if direction == "decode":
#         shift_amount *= -1
#     max_index = len(alphabet) - 1
#     end_text = ""
#     for letter in passed_text:
#         new_position = alphabet.index(letter) + shift_amount
#         if new_position > max_index:
#             new_position -= max_index
#         elif new_position < 0:
#             new_position += max_index
#         end_text += alphabet[new_position]
#     print(f"The {direction}d text is {end_text}")

# #TODO-2: Call the caesar() function, passing over the 'text', 'shift' and 'direction' values.
# casear(passed_text=text, shift_amount=shift, direction=direction)


# Casear Cipher 4
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

max_index = len(alphabet) - 1
print(max_index)

def caesar(start_text, shift_amount, cipher_direction):
    end_text = ""
    if cipher_direction == "decode":
        shift_amount *= -1
    max_index = len(alphabet) - 1

    for char in start_text:
        #TODO-3: What happens if the user enters a number/symbol/space?
        #Can you fix the code to keep the number/symbol/space when the text is encoded/decoded?
        #e.g. start_text = "meet me at 3"
        #end_text = "•••• •• •• 3"
        try:
            if alphabet.index(char) != -1:
                new_position = alphabet.index(char) + shift_amount
                if new_position > max_index or new_position < 0:
                    new_position %= max_index
                end_text += alphabet[new_position]
        except ValueError:
            end_text += char

    print(f"The {cipher_direction}d text is {end_text}")


#TODO-1: Import and print the logo from art.py when the program starts.
from art import logo
print(logo)

#TODO-4: Can you figure out a way to ask the user if they want to restart the cipher program?
#e.g. Type 'yes' if you want to go again. Otherwise type 'no'.
#If they type 'yes' then ask them for the direction/text/shift again and call the caesar() function again?
#Hint: Try creating a while loop that continues to execute the program if the user types 'yes'. 

while True:

    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    #TODO-2: What if the user enters a shift that is greater than the number of Letters in the alphabet?
    #Try running the program and entering a shift number of 45.
    #Add some code so that the program continues to work even if the user enters a shift number greater than 26. 
    #Hint: Think about how you can use the modulus (%).

    caesar(start_text=text, shift_amount=shift, cipher_direction=direction)

    run_again = input("Would you like to run again? 'Yes'/'No'").lower()

    if run_again == "no" or run_again == "n":
        break