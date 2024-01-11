# Program Name: Rock Paper Scissors
# Name:
# Date: 

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

#List of strings
move_list = []			#1. What moves should we put?

#Strings
player_move = None
ai_move = None

#Booleans
game_active = True


#main game loop
while game_active:
    
    #2. Write a Simple Welcome Message for the Game
    print("Hello World")
    time.sleep(1)
    
    
    #3. This is where the ai does a move, we need to add an upper and lower bound
    #for rand_int so we can select a random move from the move list
    #HINT: Remember that indexing begins with 0!
    ai_move = move_list[randint( , )]
    
    
    #4. Type a message that will prompt the player to type out their move
    player_move = input("		").lower()
    time.sleep(0.5)
    
    
    #print the computer's move
    print("The computer played... ", ai_move, "!")
    time.sleep(1)
    
    
    #5. Determine what should be in the elif for the game logic to function
    if player_move == ai_move:
        print("It's a tie!")
    elif (
        (			 and 			) or
        (			 and 			) or
        (			 and 			)
    ):
        print("You win!")
    else:
        print("Computer wins!")
        
    
    #6. Type a message that will prompt the player and ask whether they would like to play again
    play_again = input("		").lower()
    if play_again != "yes":
        #7. Figure out what code goes here in order to make the game loop end
    


