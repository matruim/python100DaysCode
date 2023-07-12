# print("Welcome to the rollercoster!")
# height = int(input("What is your height in cm? "))
# if height >= 120:
#     print("You can ride the rollercoster!")
# else:
#     print("Sorry, you have to grow taller before you can ride.")



# # 🚨 Don't change the code below 👇
# height = float(input("enter your height in m: "))
# weight = float(input("enter your weight in kg: "))
# # 🚨 Don't change the code above 👆

# #Write your code below this line 👇
# bmi = round(weight/height**2)

# if bmi < 18.5:
#     print(f"Your BMI is {bmi}, you are underweight")
# elif bmi < 25:
#     print(f"Your BMI is {bmi}, you have a normal weight")
# elif bmi < 30:
#     print(f"Your BMI is {bmi}, you are slightly overweight")
# elif bmi < 35:
#     print(f"Your BMI is {bmi}, you are obese")
# else:
#     print(f"Your BMI is {bmi}, you are clinically obese")





# # 🚨 Don't change the code below 👇
# year = int(input("Which year do you want to check? "))
# # 🚨 Don't change the code above 👆

# #Write your code below this line 👇
# leapYearCheck = False
# if year % 4 == 0:
#     leapYearCheck = True
#     if year % 100 == 0:
#         leapYearCheck = False
#         if not leapYearCheck and year % 400 == 0:
#             leapYearCheck = True


# if leapYearCheck:
#     print("Leap year.")
# else: 
#     print("Not leap year.")



# # 🚨 Don't change the code below 👇
# print("Welcome to Python Pizza Deliveries!")
# size = input("What size pizza do you want? S, M, or L ")
# add_pepperoni = input("Do you want pepperoni? Y or N ")
# extra_cheese = input("Do you want extra cheese? Y or N ")
# # 🚨 Don't change the code above 👆

# #Write your code below this line 👇
# basePrice = 15

# if size == 'M':
#     basePrice += 5
# elif size == 'L':
#     basePrice += 10

# if add_pepperoni == 'Y' and size == 'S':
#     basePrice += 2
# elif add_pepperoni == 'Y':
#     basePrice += 3

# if extra_cheese == 'Y':
#     basePrice += 1

# print(f"Your final bill is: {basePrice}")


# # 🚨 Don't change the code below 👇
# print("Welcome to the Love Calculator!")
# name1 = input("What is your name? \n")
# name2 = input("What is their name? \n")
# # 🚨 Don't change the code above 👆

# #Write your code below this line 👇
# num1Count = 0
# for letter in "true":
#     num1Count += name1.lower().count(letter)
#     num1Count += name2.lower().count(letter)

# num2Count = 0
# for letter in "love":
#     num2Count += name1.lower().count(letter)
#     num2Count += name2.lower().count(letter)

# score = int(f"{num1Count}{num2Count}")

# if score < 10 or score > 90:
#     print(f"Your score is {score}, you go together like coke and mentos.")
# elif score > 40 and score < 50:
#     print(f"Your score is {score}, you are alright together.")
# else:
#     print(f"Your score is {score}.")

print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.") 

#https://www.draw.io/?lightbox=1&highlight=0000ff&edit=_blank&layers=1&nav=1&title=Treasure%20Island%20Conditional.drawio#Uhttps%3A%2F%2Fdrive.google.com%2Fuc%3Fid%3D1oDe4ehjWZipYRsVfeAx2HyB7LCQ8_Fvi%26export%3Ddownload

#Write your code below this line 👇
isAlive = True
print('''
    As you stand at the crossroads, you hear a rustling in the bushes. Suddenly, a small creature appears, with a shiny object in its mouth. 
    \"Follow me!\" it squeaks, before darting off down one of the roads.
                    __________________
       /\_/\      /                   |
     ( o   o )  <    Follow me!       |
      ==_Y_==     \___________________|
      /   \        
     (     )  
    /'\_   _/`\ 
    \___)=(___/ 

.     '     , 
 )   o    ( 
(           ) 
 `  -^^-  ' 


    ''')
answer = input("Do you follow this creature? 'Y'/'N' ").upper()
if answer == 'Y':
    print('''
    As you follow the creature, you begin to notice that the road is getting narrower and darker. Soon, you're surrounded by dense trees on either side, and you can barely see the creature up ahead.

Eventually, the creature leads you to a small, run-down cottage. 

                        (   )
                          (    )
                           (    )
                          (    )
                            )  )
                           (  (                  /\
                            (_)                 /  \  /\
                    ________[_]________      /\/    \/  \
           /\      /\        ______    \    /   /\/\  /\/\
          /  \    //_\       \    /\    \  /\/\/    \/    \
   /\    / /\/\  //___\       \__/  \    \/
  /  \  /\/    \//_____\       \ |[]|     \
 /\/\/\/       //_______\       \|__|      \
/      \      /XXXXXXXXXX\                  \
        \    /_I_II  I__I_\__________________\
               I_I|  I__I_____[]_|_[]_____I
               I_II  I__I_____[]_|_[]_____I
               I II__I  I     XXXXXXX     I
            ~~~~~"   "~~~~~~~~~~~~~~~~~~~~~~~~


It disappears inside, and you hesitate for a moment before cautiously approaching the door.

You knock, but there's no answer. You push the door open and step inside.

As you look around the cottage, you realize that something feels off. The air is thick with a strange, musty smell, and the furniture looks old and worn. Suddenly, you hear a noise behind you.

You spin around to see the small creature from before, but it's changed. Its eyes are glowing red, and its fur has turned black and spiky. You realize with a sinking feeling that you've been led into a trap.

GAME OVER
    ''')
    isAlive = False
elif answer == 'N':
    print('''
    
    You decide not to follow the small creature and instead take the road away from it. As you walk, you notice that the path is getting wider and brighter, and soon you emerge into a beautiful clearing.

In the center of the clearing is a sparkling stream, and there are trees and flowers all around. You feel a sense of peace and calm wash over you.

As you look around, you notice a figure sitting by the stream. It's an old woman, dressed in a long, flowing gown. She looks up as you approach.

        
           www
          //`\\
         (/a a\)
         (\_-_/) 
        .-~'='~-.
       /`~`"Y"`~`\
      / /(_ * _)\ \
     / /  )   (  \ \
     \ \_/\\_//\_/ / 
      \/_) '*' (_\/
        |       |
        |       |
        |       |
        |       |
        |       |
        |       |
        |       |
        |       |
        w*W*W*W*w

"Hello there," she says kindly. "What brings you to this lovely place?"

You explain that you were following a small creature, but it led you to a dangerous situation. The old woman nods sympathetically.

"I know the creature you speak of," she says. "It's a trickster, and it's led many a traveler astray. But you were wise not to follow it."

She invites you to sit by the stream and rest for a while.
    
    ''')

else:
    print('''
    You hesitate for a moment, then decide not to follow the small creature. Something about it just doesn't seem right.

As you stand there, wondering what to do next, you hear a noise behind you. You spin around to see a group of bandits emerging from the woods. They're armed with swords and wearing rough, tattered clothing.

"Hand over your valuables," one of them growls, brandishing his sword. "We won't hurt you if you cooperate."

You realize with a sinking feeling that you're in serious danger.

GAME OVER
    ''')
    isAlive = False

if isAlive:
    answer = input("Do you sit and rest with the old Lady or do you follow the path? type 'wait' for 'continue'").lower()
    if answer == 'wait':
        print(''' 
        As you spend time in the meadow, you feel reinvigorated and at peace. You start to feel restless, though, and you know that it's time to move on from this place.

        As you make your way down the path, you come across a strange structure that seems out of place in the natural beauty around you. It's a small building with two brightly colored doors, one blue and one red.

You approach the building with caution, wondering what could be inside. As you get closer, you see that there is a message carved above the doors:

"Choose wisely, for one door leads to treasure, and the other leads to certain doom."

You realize that this is a test, and you must choose one of the doors to continue on your journey.

        ''')
    elif answer == 'continue':
        print('''
        You thank the old woman for her kindness, but you're too anxious to rest. You feel like you need to keep moving if you want to reach your destination.

You bid the old woman farewell and hurry down the path, ignoring the peaceful surroundings. As you rush forward, you don't notice the branch on the ground until it's too late. You trip and fall, hitting your head on a rock.

When you wake up, everything is blurry and confusing. You realize with horror that you've been seriously injured, and you know you won't make it much further.

You try to crawl forward, but it's no use. You're too weak and disoriented. As you lie there, the world starts to fade away.

The last thing you hear is the sound of the small creature's laughter, and you realize with a sinking feeling that you should have been more careful.

GAME OVER
        ''')
        isAlive = False
    else:
        print('''
        You take in the beauty of the meadow and realize that this is where you want to be. You have no desire to continue on your journey - this is your destination.

You find a spot in the meadow that calls to you and decide to make it your home. You build a small cabin and tend to a garden, living off the land and the resources around you. You spend your days in peace and quiet, enjoying the simple pleasures of life.

As the years go by, you find that you have no regrets about staying in the meadow. You have found happiness and contentment in a place that many would consider insignificant. You have found a home and a purpose, and that is enough.

You pass away peacefully, surrounded by the beauty of the meadow you have called home for so long. You know that you have lived a good life, one that was true to yourself and your desires.

GAME OVER
        ''')
        isAlive = False


if isAlive:
    answer = input("Which door will you choose? 'red'/'blue'").lower()

    if answer == 'red':
        print('''
                               _             _,-----------._        ___
                      (_,.-      _,-'_,-----------._`-._    _)_)
                         |     ,'_,-'  ___________  `-._`.
                        `'   ,','  _,-'___________`-._  `.`.
                           ,','  ,'_,-'     .     `-._`.  `.`.
                          /,'  ,','        >|<        `.`.  `.\
                         //  ,','      ><  ,^.  ><      `.`.  \\
                        //  /,'      ><   / | \   ><      `.\  \\
                       //  //      ><    \/\^/\/    ><      \\  \\
                      ;;  ;;              `---'              ::  ::
                      ||  ||              (____              ||  ||
                     _||__||_            ,'----.            _||__||_
                    (o.____.o)____        `---'        ____(o.____.o)
                      |    | /,--.)                   (,--.\ |    |
                      |    |((  -`___               ___`   ))|    |
                      |    | \\,'',  `.           .'  .``.// |    |
                      |    |  // (___,'.         .'.___) \\  |    |
                     /|    | ;;))  ____) .     . (____  ((\\ |    |\
                     \|.__ | ||/ .'.--.\/       `/,--.`. \;: | __,|;
                      |`-,`;.| :/ /,'  `)-'   `-('  `.\ \: |.;',-'|
                      |   `..  ' / \__.'         `.__/ \ `  ,.'   |
                      |    |,\  /,                     ,\  /,|    |
                      |    ||: : )          .          ( : :||    |
                     /|    |:; |/  .      ./|\,      ,  \| :;|    |\
                     \|.__ |/  :  ,/-    <--:-->    ,\.  ;  \| __,|;
                      |`-.``:   `'/-.     '\|/`     ,-\`;   ;'',-'|
                      |   `..   ,' `'       '       `  `.   ,.'   |
                      |    ||  :                         :  ||    |
                      |    ||  |                         |  ||    |
                      |    ||  |                         |  ||    |
                      |    |'  |            _            |  `|    |
                      |    |   |          '|))           |   |    |
                      ;____:   `._        `'           _,'   ;____:
                     {______}     \___________________/     {______}
                     |______|_______________________________|______|
        You approach the brightly colored doors with caution. You take a deep breath and reach out to the red door, turning the handle and stepping inside.

The room is dark and foreboding, and you feel a sense of unease as you step forward. Suddenly, you hear a loud click, and the floor beneath you drops away.

You find yourself falling through a trapdoor and landing in a pit filled with spikes. You realize too late that this was a trap, and you are now trapped with no way out.

As you take your last breaths, you think back on your journey and wonder where you went wrong. You realize that you should have chosen the other door, the one that led to treasure, but it's too late now.

Your adventure has come to a sudden and tragic end.
        ''')
    elif answer == 'blue':
        print('''
                               _             _,-----------._        ___
                      (_,.-      _,-'_,-----------._`-._    _)_)
                         |     ,'_,-'  ___________  `-._`.
                        `'   ,','  _,-'___________`-._  `.`.
                           ,','  ,'_,-'     .     `-._`.  `.`.
                          /,'  ,','        >|<        `.`.  `.\
                         //  ,','      ><  ,^.  ><      `.`.  \\
                        //  /,'      ><   / | \   ><      `.\  \\
                       //  //      ><    \/\^/\/    ><      \\  \\
                      ;;  ;;              `---'              ::  ::
                      ||  ||              (____              ||  ||
                     _||__||_            ,'----.            _||__||_
                    (o.____.o)____        `---'        ____(o.____.o)
                      |    | /,--.)                   (,--.\ |    |
                      |    |((  -`___               ___`   ))|    |
                      |    | \\,'',  `.           .'  .``.// |    |
                      |    |  // (___,'.         .'.___) \\  |    |
                     /|    | ;;))  ____) .     . (____  ((\\ |    |\
                     \|.__ | ||/ .'.--.\/       `/,--.`. \;: | __,|;
                      |`-,`;.| :/ /,'  `)-'   `-('  `.\ \: |.;',-'|
                      |   `..  ' / \__.'         `.__/ \ `  ,.'   |
                      |    |,\  /,                     ,\  /,|    |
                      |    ||: : )          .          ( : :||    |
                     /|    |:; |/  .      ./|\,      ,  \| :;|    |\
                     \|.__ |/  :  ,/-    <--:-->    ,\.  ;  \| __,|;
                      |`-.``:   `'/-.     '\|/`     ,-\`;   ;'',-'|
                      |   `..   ,' `'       '       `  `.   ,.'   |
                      |    ||  :                         :  ||    |
                      |    ||  |                         |  ||    |
                      |    ||  |                         |  ||    |
                      |    |'  |            _            |  `|    |
                      |    |   |          '|))           |   |    |
                      ;____:   `._        `'           _,'   ;____:
                     {______}     \___________________/     {______}
                     |______|_______________________________|______|
        You approach the brightly colored doors with caution. You take a deep breath and reach out to the blue door, turning the handle and stepping inside.

Inside the room, you find a treasure trove of gold, jewels, and other valuable artifacts. You smile to yourself, grateful for your good fortune.

But wait - you hear a creaking noise behind you. You turn around to see the red door slowly opening, revealing a dark and ominous hallway.

You realize that you have made the right choice in choosing the blue door, and you quickly gather the treasure and make your way out of the building.
        ''')
    else:
        print('''
        You approach the brightly colored doors with caution, but you suddenly stop in your tracks. You realize that you don't have to choose either door. You take a step back and look at the structure with a critical eye.

As you examine the building, you notice a small button hidden in the wall. You press it, and a hidden door slides open, revealing a small room filled with treasures.

You smile to yourself, realizing that sometimes the answer isn't always a binary choice. You take some time to explore the hidden room, gathering as many treasures as you can carry.

You leave the building feeling satisfied and happy with your unexpected discovery. You continue on your journey, wondering what other surprises lie ahead.
        ''')