# this is the "game.py" file...

import random
import os


#Bonus #1: Passing of player name through environment variable

player_name = os.getenv("PLAYER_NAME", default = "Player One")

print("Rock, Paper, Scissors, Shoot!")
print("")
print("Welcome " + player_name + " to my Rock, Paper, Scissors Game!")
print("")


#Getting input for user

user_input = input("Please choose Rock, Paper, or Scissors: ")
user_input = user_input.upper()
print("")

if(user_input != "SCISSORS" and user_input != "ROCK" and user_input != "PAPER"):
	print("Invalid Input. The game will now end. Goodbye :)")
	quit()


#Printing what the user selected
print ("You selected " +user_input)
print("")


#Computer Choice done randomly
computer_options = ["ROCK", "PAPER", "SCISSORS"]
computer_choice = random.choice(computer_options)

#Printing What the Computer Selects
print ("The computer has selected " + computer_choice)
print("")


#Determining the winner

if(user_input == "SCISSORS"):
	if(computer_choice == "SCISSORS"):
		print ("You Tied with the computer")
	if(computer_choice == "PAPER"):
		print ("You Won against the computer :)")
	if(computer_choice == "ROCK"):
		print("You Lost to the computer :(")

if(user_input == "ROCK"):
	if(computer_choice == "ROCK"):
		print("You Tied with the computer")
	if(computer_choice == "SCISSORS"):
		print ("You Won against the computer :)")
	if(computer_choice == "PAPER"):
		print("You Lost to the computer :(")

if(user_input == "PAPER"):
	if(computer_choice == "PAPER"):
		print("You Tied with the computer")
	if(computer_choice == "ROCK"):
		print ("You Won against the computer :)")
	if(computer_choice == "SCISSORS"):
		print("You Lost to the computer :(")

#Goodbye Message
print("")
print("Thanks for playing. Please play again!")
		

