from random import random
# This is comment
# Game - Guess a number
# Author: Kaustubh
# Date : Nov 28, 2022
# Desription: You have to guess a number 
# That is to be calculate by python
# To win the game you have to be guess correct number

## Do not change this line
python_guessed_number = random() # return a random number as a float 0 to 0.099
##
python_guessed_number = (python_guessed_number * 100) + 1 # taking number from 1 to 100
python_guessed_number = int( python_guessed_number ) # converting number float to integer

my_guess = input('Choose or Guess A Number 1 to 100: ')
my_guess = int ( my_guess )

if my_guess > 100 :
    print ("You entered greater than 100 pls enter no less than 100")
    exit()
# cheat code
convert_to_str = str ( python_guessed_number ) # convert integer to string
print('Python guessed number is:' +  convert_to_str ) 
# Decision making
# single '=' means assign a number to variable
# double '=' (like '==') mean checking where the to variable equal or not
if my_guess == python_guessed_number:
    print("You have win the game")
else:
    print("You have lost")

# Example nested if-else
if  my_guess > ( python_guessed_number + 50 ):
    print ("The num is too high")

elif  my_guess < ( python_guessed_number - 50 ):
    print ("The num is too low")

# else if short form in python elif
elif  my_guess < python_guessed_number :
    print ("Number is near to low")

else:
    print(" Number is near to high")
