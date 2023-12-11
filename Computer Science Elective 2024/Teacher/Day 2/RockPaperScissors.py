# Program Name	: Rock Paper Scissors
# Programmed By	: Mark Wiedeman
# For Use of By : Naveen Bahadur and Mark Wiedeman
# Date			: December 6th 2023

from random import randint
import time

        
def slow_print(input_string, delay=0.1):
    for char in input_string:
        print(char, end='', flush=True)
        time.sleep(delay)

#======================Variables=====================
#	What are variables?
#		Variables are values stored in the program that
#	can change.  There are many types of variables, and
#	the simplest ones include strings for words and
#	ints/floats for numbers.  Constants also use these "data-types"
#
#	#===Lists===#
#	move_list = holds all of the possible hands the computer can play
#
#	#===Strings===#
#	player_move = this variable holds a string representing the player's hand
#	ai_move 	= this variable holds a string representing the ai's hand
#	
#	#===Booleans===#
#	game_active = this controls whether the game does another game
#					of rock, paper, scissors
#
#====================================================

#Lists
move_list = ["rock", "paper", "scissors"]

#Strings
player_move = None
ai_move = None

#Booleans
game_active = True


#main game loop
while game_active:
    
    #Simple Welcome Message to the Game
    slow_print("Get Ready! \n")
    time.sleep(0.5)
    print("Rock...")
    time.sleep(0.5)
    print("Paper..")
    time.sleep(0.5)
    print("Scissors!")
    time.sleep(1)
    
    #AI does its move
    ai_move = move_list[randint(0, 2)]
    
    #Ask for and receive the player's move
    player_move = input("Which do you pick? (type 'rock', 'paper', or 'scissors'): ").lower()
    time.sleep(0.5)
    
    #print the computer's move
    print("The computer played... ", ai_move, "!")
    time.sleep(1)
    
    #simple if-else to determine and print who won
    if player_move == ai_move:
        print("It's a tie!")
    elif (
        (player_move == "rock" and ai_move == "scissors") or
        (player_move == "paper" and ai_move == "rock") or
        (player_move == "scissors" and ai_move == "paper")
    ):
        print("You win!")
    else:
        print("Computer wins!")
    
    #checks if the player wants to play again
    play_again = input("Do you want to play again? (yes/no): ").lower()
    if play_again != "yes":
        game_active = False
    

