# this is the "game.py" file...

import random
import os


def determine_winner(computer, user):
    """
    Determines the winning choice between two valid choices from selectable options: "rock", "paper", or "scissors".

    Returns the winning choice (e.g. "paper"), or None if there is a tie.

    Example: determine_winner("rock", "paper")
    """

    winner = ""

    if(user == "scissors"):
        if(computer == "scissors"):
            winner = None
        if(computer == "paper"):
            winner = "scissors"
        if(computer == "rock"):
            winner = "rock"

    if(user == "rock"):
        if(computer == "rock"):
            winner= None
        if(computer == "scissors"):
            winner ="rock"
        if(computer == "paper"):
            winner ="paper"

    if(user == "paper"):
        if(computer == "paper"):
            winner = None
        if(computer == "rock"):
            winner = "paper"
        if(computer == "scissors"):
            winner = "scissors"


    return winner


#main

if __name__ == "__main__":
    # Bonus #1: Passing of player name through environment variable

    player_name = os.getenv("PLAYER_NAME", default= "Player One")

    # welcome message
    print("Rock, Paper, Scissors, Shoot!")
    print("")
    print("Welcome " + player_name + " to my Rock, Paper, Scissors Game!")
    print("")

    # Getting input from user

    user_input = input("Please choose Rock, Paper, or Scissors: ")
    user_input = user_input.lower()
    print("")

    if(user_input != "scissors" and user_input != "rock" and user_input != "paper"):
        print("Invalid Input. The game will now end. Goodbye :)")
        quit()

    # Printing what the user selected
    print ("You selected " + user_input)
    print("")

    # Computer Choice done randomly
    computer_options = ["rock", "paper", "scissors"]
    computer_choice = random.choice(computer_options)

    # Printing What the Computer Selects
    print("The computer has selected " + computer_choice)
    print("")

    ''' Determining the winner Old version for reference


    if(user_input == "scissors"):
        if(computer_choice == "scissors"):
            print("You Tied with the computer")
        if(computer_choice == "paper"):
            print("You Won against the computer :)")
        if(computer_choice == "rock"):
            print("You Lost to the computer :(")

    if(user_input == "rock"):
        if(computer_choice == "rock"):
            print("You Tied with the computer")
        if(computer_choice == "scissors"):
            print("You Won against the computer :)")
        if(computer_choice == "paper"):
            print("You Lost to the computer :(")

    if(user_input == "paper"):
        if(computer_choice == "paper"):
            print("You Tied with the computer")
        if(computer_choice == "rock"):
            print("You Won against the computer :)")
        if(computer_choice == "scissors"):
            print("You Lost to the computer :(")

'''



    #Determining winner using determine_winner function

    champion = determine_winner(computer_choice, user_input)

    if(champion == None):
        print("You Tied with the computer")
    if(champion == computer_choice):
        print("You Lost to the computer :(")
    if(champion == user_input):
        print("You Won against the computer :)")






    # Goodbye Message
    print("")
    print("Thanks for playing. Please play again!")
