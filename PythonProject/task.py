# *********DAY 1:**********
# Write your code below this line
# print('hello world\nhello world\nhello world')
# print('Hello' + ' Daniel')
# print('Hello' + ' ' + 'Angela')

# 8. the python input function
# print("hello " + input("What is your name?")+"!")

# 9. Python variables
# name = input('What is your name? ')
# numberOfChar = len(name)
# # don't forget to cast the int into string because numberOfChar is an int type.
# print("Hello " + name + " The number of chars of your name are: " + str(numberOfChar))

# 11. DAY 1: Final Project: Name Generator
# print("Welcome to the Band Generator!!")
# city = input("Which city did you grow up in?\n ")
# petName = input("What is the name of your pet?\n ")
#
# print("So, your band name could be " + city + " " + petName)

#*******DAY 2: UNDERSTANDING DATA TYPES AND HOW TO MANIPULATE STRINGS*********
# 14. Python primitive Data types
# Str = input("Type a string: ")
# print(Str[0]) #first char
# print(Str[len(Str)-1]) #last char

#15. Type error, type checking and type conversion
# print(type("Hola"))
# print(type(123))
# print(type(False))
# print(type(3.45))
#
# #conversion type (type casting)
# print(type(int("1234"))) # ---> <class 'int'>
#
# print("Number of letters in your name: " + str(len(input("Enter your name: "))))

# 16. Mathematical Operation in python
# print(123 + 456)
# print(7 - 3)
# print(3*2)
# print(6/3) # implicit type casting to float result = 2.0
# print(6//3) # to round the number into an integer result = 2
# print(2**2) # expo number 2 to the power of 2
#
# # PEMDAS = Parentheses,Exponents,Multiplication/Division,Addition/Subtraction
# # 1. () 2. ** 3. * 4. / 5. + 6. -
# print(3*3 + 3/3 -3) # ---> result 7.0

# 17. Number Manipulation and F Strings in python
# bmi = 84/1.65**2
#
# # round operator
# print(bmi)
# print(int(bmi))
# print(round(bmi)) # round it up
# print(round(bmi,2)) # round it with number of decimal digits ---> result 30.85
#
# # assignment operator
# score = 0
# score += 1
# print(score)
#
# print('Your score is ' + str(score))
#
# # f-strings
# score2 = 0
# height = 1.8
# is_winning = True
#
# print(f"Your score is = {score2}, your height is {height} "
#       f"You are winning is {is_winning}")

# 18. day 2 project : tip calculator
# print("Welcome to the tip calculator!!")
# bill = float(input("What was the total bill?  $"))
# tip = float(input("How much tip would you like to tip? 10, 12, 0r 15? "))
# split = float(input("How many people to split the bill? "))
#
# splitBill = bill/split
# billToPay = splitBill*(tip/100) + splitBill
#
# total = round(billToPay,2)
#
# print(f"Each person should pay: ${total}")


# *****DAY 3: CONDITIONAL STATEMENTS, LOGICAL OPERATORS, CODE BLOCKS AND SCOPE****

#22.Control flow with if/else and conditional operators
# print("Welcome to the rollercoaster!")
# height = int(input("What is your height in cm? "))
# bill = 0
# if height > 120:
#     print("You can ride")
#     age = int(input("how old are you? "))
#     if age >= 18:
#         print("Please pay 12$ ticket")
#         bill = 12
#     elif (age < 18) and (age < 12):
#         print("Please pay 7$ ticket")
#         bill = 7
#     else:
#         print("Please pay 5$ ticket")
#         bill = 5
#     #Multiple ifs
#     wants_photo = input("Do you want to have a photo take? Type y for Yes and n for No.")
#     if wants_photo == 'y':
#         bill += 3 #add 3$ to their bill
#     print(f"Your final bill is {bill}$ ")
# else:
#     print("You can't ride")

 # Check Odd or Even
# number = int(input("Give me a number: "))
#
# if number%2 == 0:
#     print("The number is even")
# else:
#     print("the number is odd")


# Challenge
# print("Welcome to Python Pizza Deliveries!")
# size = input("What size pizza do you want? S, M or L: ")
# pepperoni = input("Do you want pepperoni on your pizza? Y or N: ")
# extra_cheese = input("Do you want extra cheese? Y or N: ")
# bill = 0
#
# if size == 'S':
#     bill += 15
#     if pepperoni == 'Y':
#         bill+= 2
#     elif pepperoni == 'N':
#         bill+=0
#     if extra_cheese == 'Y':
#         bill += 1
#     elif extra_cheese == 'N':
#         bill += 0
#     print(f"Your bill is: {bill}$")
# elif size == 'M':
#     bill += 20
#     if pepperoni == 'Y':
#         bill += 3
#     elif pepperoni == 'N':
#         bill+=0
#     if extra_cheese == 'Y':
#         bill += 1
#     elif extra_cheese == 'N':
#         bill += 0
#     print(f"Your bill is: {bill}$")
# elif size == 'L':
#     bill += 25
#     if pepperoni == 'Y':
#         bill += 3
#     elif pepperoni == 'N':
#         bill += 0
#     if extra_cheese == 'Y':
#         bill += 1
#     elif extra_cheese == 'N':
#         bill += 0
#     print(f"Your bill is: {bill}$")
# else:
#     print("You need to chose S=small M=medium L=Large")


# 28. Project : treasure island
# print('''
#  o .,<>., o
#                                                                 |\/\/\/\/|
#                                                                 '========'
#                                                                 (_ SSSSSSs
#                                                                 )a'`SSSSSs
#                                                                /_   SSSSSS
#                                                                .=## SSSSS
#                                                                .####  SSSSs
#                                                                ###::::SSSSS
#                                                               .;:::""""SSS
#                                                              .:;:'  . .
#                                                             .::/  '     .'|
#                                                            .::( .         |
#                                                            :::)
#                                                            /\(            /
#                                                           /)            ( |
#                                                         .'  \  .       ./ /
#                                                      _-'    |\  .        |
#                                    _..--..   .  /"---\      | ` |      . |
#            -=====================,' _     \=(*#(7.#####()   |  `/_..   , (
#                        _.-''``';'-''-) ,.  \ '  '+/// |   .'/   \  ``-.)
#                      ,'  _.-  ((    `-'  `._\    `` \_/_.'  )    /`-._  ) |
#                    ,'\ ,'  _.'.`:-.    \.-'                 /   <_L   )"  |
#                  _/   `._,' ,')`;  `-'`'                    |     L  /    /
#                 / `.   ,' ,|_/ / \                          (    <_-'
#                 \ / `./  '  / /,' \                        /|`         `. |
#                 )\   /`._   ,'`._.-\                       |)
#                /  `.'    )-'.-,' )__)                      |\            `|
#               : /`. `.._(--.`':`':/ \                      ) \
#               |::::\     ,'/::;-))  /                      ( )`.            |
#               ||:::::  . .::':  :`-(                       |/    .          |
#               ||::::|  . :|  |==[]=:                       .        -
#               |||:::|  : ||  :  |  |                      /\           `     |
#   ___ ___     '|;:::|  | |'   \=[]=|                     /  \
#  |   /_  ||``|||:::::  | ;    | |  |                     \_.'\_               `-.
#  :   \_``[]--[]|::::'\_;'     )-'..`._                 .-'\``:: ` .
#   \___.>`''-.||:.__,'     SSt |_______`>              <_____:::.         . . \  _/
#                                                             `+a:f:......jrei
# ''')
# print("Welcome to the treasure Island."
#       "Your mission is to find the treasure")
#
# #level 1
# firstMove =input("Do you want to go left or right?\n")
# if firstMove.lower() == 'left':
#     secondMove = input("Ok, do you want to swim or wait?\n")
#     #level 2
#     if secondMove.lower() == 'swim':
#         print("you have been attack by trout --- game over")
#     elif secondMove.lower() == 'wait':
#         #level 3
#         thirdMove = input("Which door do you want to chose? Yellow, Blue or Red\n")
#         if thirdMove.lower() == 'red':
#             print("Ohh burned by fire --- game over")
#         elif thirdMove.lower() == 'blue':
#             print("ohh no eaten by beast --- Game over")
#         elif thirdMove.lower() == 'yellow':
#             print('''  YOU HAVE FOUND THE TREASURE YOU WIN!!
# *******************************************************************************
#           |                   |                  |                     |
#  _________|________________.=""_;=.______________|_____________________|_______
# |                   |  ,-"_,=""     `"=.|                  |
# |___________________|__"=._o`"-._        `"=.______________|___________________
#           |                `"=._o`"=._      _`"=._                     |
#  _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
# |                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
# |___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
#           |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
#  _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
# |                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
# |___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
# ____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
# /______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
# ____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
# /______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
# ____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
# /______/______/______/______/______/______/______/______/______/______/[TomekK]
# *******************************************************************************
#             ''')
#         else:
#             print("you have been capture --- game over")
# else:
#     print("you\'ve fallen into a hole --- game over")


# *******DAY 4: BEGINNER - RANDOMISATION AND PYTHON LIST*******

# 31. Random Module
import random
from wsgiref.util import shift_path_info

#************
# import myModule
# from myModule import my_favourite_number
#
# #random.randint => range between a and b including a and b
# randomNumber = random.randint(23,56)
# print(randomNumber)
#
# print(my_favourite_number) #this variable was imported from myModule(created by me)
#************

# # random.random() => return the next floating point in the range 0.0 <= X < 1.0
# randomNumber2 = round(random.random()*100)+1
# print(randomNumber2)
#
# # random.uniform(a,b) => return random numbers between a and b but including both a and b
# randomNumber3 = round(random.uniform(1,10))
# print(randomNumber3)
#
# if randomNumber3 <= 5:
#     print("Heads")
#     #print(randomNumber3)
# else:
#     print("Tails")
#     #print(randomNumber3)

# 32 UNDERSTANDING THE OFFSET AND APPENDING ITEMS TO LIST

# LIST
# fruits = ['cherry', 'apple', 'pear']
#
# #to replace 'apple' for 'coconut' old style
# fruits[1] = 'coconut'
#
# # append => to add an element at the end of the list
# fruits.append('grape')
#
# print(fruits)

# extend => to add like a small piece of list to the main list
# fruits.extend(['lemon','orange']) # don't forget to use brackets
#
# print(fruits)

# # 33. Code challenge - Who will pay the bill?
# partners = ["Alice","Bob","Charlie","David","Emanuel"]
#
# # 1 Option
# randomPartner = random.choice(partners)
#
# print(randomPartner)
#
# # 2nd Option
# random_index = random.randint(0,4)
# print(partners[random_index])


# # 34. Index errors and working with nested list
#
# fruits2 = ["Strawberries","Nectarines","Apples","Grapes"]
# vegetables = ["Spinach","Kale","Tomatoes","Celery","Potatoes"]
#
# dirty_dozen = [fruits2,vegetables] # nested list
# print(dirty_dozen)

# 35. DAY 4: PROJECT ROCK PAPER SCISSORS

# print("Welcome to the amazing world of paper scissors or rock")
# rock =  ''''
#  _______
# ---'   ____)
#       (_____)
#       (_____)
#       (____)
# ---.__(___)
# '''
#
# paper = '''
#  _______
# ---'    ____)____
#            ______)
#           _______)
#          _______)
# ---.__________)
# '''
#
# scissor = '''
#  _______
# ---'   ____)____
#           ______)
#        __________)
#       (____)
# ---.__(___)
# '''
# number = int(input("chose paper scissor or rock, so 1 for paper 2 for scissor and 3 for rock\n"))
# game = [paper,scissor,rock]
# gameStrings = ["PAPER","SCISSOR","ROCK"]
# randomNumber = random.randint(1,3)
#
# if number == 1:
#     print(f"YOU HAVE SELECTED PAPER")
#     print(paper)
#     print(f"THE PC HAS SELECTED {gameStrings[randomNumber-1]}")
#     print(game[randomNumber-1])
#     if gameStrings[randomNumber-1] == 'ROCK':
#         print("YOU WIN")
#     elif gameStrings[randomNumber-1] == 'SCISSOR':
#         print("YOU LOSE")
#     else:
#         print("YOU TIE")
# elif number == 2:
#     print(f"YOU HAVE SELECTED SCISSOR")
#     print(scissor)
#     print(f"THE PC HAS SELECTED {gameStrings[randomNumber-1]}")
#     print(game[randomNumber-1])
#     if gameStrings[randomNumber-1] == 'PAPER':
#         print("YOU WIN")
#     elif gameStrings[randomNumber-1] == 'ROCK':
#         print("YOU LOSE")
#     else:
#         print("YOU TIE")
# elif number == 3:
#     print(f"YOU HAVE SELECTED ROCK")
#     print(rock)
#     print(f"THE PC HAS SELECTED {gameStrings[randomNumber-1]}")
#     print(game[randomNumber-1])
#     if gameStrings[randomNumber-1] == 'SCISSOR':
#         print("YOU WIN")
#     elif gameStrings[randomNumber-1] == 'PAPER':
#         print("YOU LOSE")
#     else:
#         print("YOU TIE")
# else:
#     print("error....chose a number between 1 and 3")

# 37 DAY 5: PYTHON LOOPS

# 38 USING THE FOR LOOP WITH PYTHON

# fruits = ["Apple","Peach","Pear"]
#
# for fruit in fruits:
#     print(fruit)
#     print(fruit + " pie")

# student_scores = [150,142,185,120,171,184,149,24,59,68,199,78,65,89,86]
# # sum method
# total_exam_score = sum(student_scores)
# # max method
# highest_score = max(student_scores)
#
# print(total_exam_score)
# print(highest_score)
#
# sum = 0
# for score in student_scores:
#     sum += score
#
# print(sum)

# num = 0
# for score in student_scores:
#     if score > num:
#         num = score
# print(num)

# 40. FOR LOOPS AND THE RANGE FUNCTION
# Range Function

# for number in range(1,10): # ---> 10 is not included
#     print(number) # the last number is not included

# if you want to add an interval
# for number in range(1,11,3): # ---> interval of 3
#     print(number)

# for number in range(1,101):
#     print(number)

# for number in range(1, 101):
#     if number % 3 == 0:
#         if number % 3 == 0 and number % 5 == 0:
#             print("FizzBuzz")
#         elif number % 3 == 0:
#             print("Fizz")
#     elif number % 5 == 0:
#         print("Buzz")
#     else:
#         print(number)

#41. CREATE A PASSWORD GENERATOR
#

# DAY 6: PYTHON FUNCTIONS & KARNEL
# def my_function():
#     print("hello")
#     print("bye bye")
# my_function()

# Reeborg's World challenge code
# def turn_right():
#     for move in range(3):
#         turn_left()
#
# def jump(num):
#     for moIn in range(num):
#         turn_left()
#         move()
#         if moIn > 0:
#             turn_left()
#             move()
#         turn_right()
#         move()
#         turn_right()
#         move()
#
# move()
# jump(6)

# 47 AND 48 WORKING WITH WHILE LOOPS - REEBORG WORLDS CHALLENEGES

# check the documentation

# DAY 7 - HANGMAN

























