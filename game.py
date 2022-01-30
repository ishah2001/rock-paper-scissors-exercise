# this is the "game.py" file...

import random




print("Rock, Paper, Scissors, Shoot!")
print("")
print("Welcome Player One to my Rock, Paper, Scissors Game!")
print("")


#Getting input for user

userInput = input("Please choose Rock, Paper, or Scissors: ")
userInput = userInput.upper()
print("")

if(userInput != "SCISSORS" and userInput != "ROCK" and userInput != "PAPER"):
	print("Invalid Input. The game will now end. Goodbye :)")
	quit()


#Printing what the user selected
print ("You selected " +userInput)
print("")


#Computer Choice done randomly
computerOptions = ["ROCK", "PAPER", "SCISSORS"]
computerChoice = random.choice(computerOptions)

#Printing What the Computer Selects
print ("The computer has selected " + computerChoice)
print("")


#Determining the winner

if(userInput == "SCISSORS"):
	if(computerChoice == "SCISSORS"):
		print ("You Tied with the computer")
	if(computerChoice == "PAPER"):
		print ("You Won against the computer :)")
	if(computerChoice == "ROCK"):
		print("You Lost to the computer :(")

if(userInput == "ROCK"):
	if(computerChoice == "ROCK"):
		print("You Tied with the computer")
	if(computerChoice == "SCISSORS"):
		print ("You Won against the computer :)")
	if(computerChoice == "PAPER"):
		print("You Lost to the computer :(")

if(userInput == "PAPER"):
	if(computerChoice == "PAPER"):
		print("You Tied with the computer")
	if(computerChoice == "ROCK"):
		print ("You Won against the computer :)")
	if(computerChoice == "SCISSORS"):
		print("You Lost to the computer :(")

#Goodbye Message
print("Thanks for playing. Please play again!")
		

