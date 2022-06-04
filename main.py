"""
    App for Rock ,Paper, Scissors game. using the CLI

    Implemented by: Anyanwu Amanze Arthur
    Student ID: I4G002855YAG

    version is currently for computer to play against player
    after task submission would include a player vs player mode :)

"""

#------------------------------------------------------------------------------#
#                               IMPORT STATEMENTS                              #
#------------------------------------------------------------------------------#
import random
from random import choice
"""
    accepted inputs of values ignoring case (accepted_inputs)
    choices of values (accepted_inputs)
    map of values (accepted_inputs) mapping to values (accepted_inputs)
"""


accepted_inputs=['R','P','S','ROCK', 'PAPER', 'SCISSORS'] # list of accepted inputs => Rock, Paper, Scissors
choices = ['ROCK', 'PAPER', 'SCISSORS']

mapped_values = {'ROCK': 'R', 'PAPER': 'P', 'SCISSORS': 'S', 'R': 'ROCK', 'P': 'PAPER', 'S': 'SCISSORS'}


def brain_box(first,second):
    """
        Determines the outcome of the game box
        :returns a dict of winner and result TIE if first == second
        :returns a dict of winner and result BEAT if first beats second and vice 

        RULES:
        ROCK beats SCISSORS
        PAPER beats ROCK
        SCISSORS beats PAPER
        
    """
    # if first == second: Here player is first and second is computer
    if first == second:
        return {'winner':"None",'result':'TIE'}
    elif (first == 'ROCK' and second == 'SCISSORS') or (first == 'SCISSORS' and second == 'ROCK') :
        winner= "Player" if first == 'ROCK' else "Computer"
        return {'winner':winner,'result':'BEAT'}
    elif (first == 'PAPER' and second == 'ROCK') or (first == 'ROCK' and second == 'PAPER') :
        winner= "Player" if first == 'PAPER' else "Computer"
        return {'winner':winner,'result':'BEAT'}
    elif (first == 'SCISSORS' and second == 'PAPER') or (first == 'PAPER' and second == 'SCISSORS') :
        winner= "Player" if first == 'SCISSORS' else "Computer"
        return {'winner':winner,'result':'BEAT'}
    
def validate_input(input_value):
    """
        Validates the input value
        :returns True if input_value is in accepted_inputs
        :returns False if input_value is not in accepted_inputs
    """
    try:
        return mapped_values[f"{input_value}"]  in accepted_inputs 
    except KeyError:
        return False


def game_engine():
    # game status
    game_on = True

    # player name
    player_name = input("Enter Your Name: ")
    print(f"Welcome {player_name} to Rock, Paper, Scissors game")

    while game_on:
        print("`````````````````````````````````````````````````````````````````````")
        print("`````````````````````````````````````````````````````````````````````")
        print("         Enter R , P , S or ROCK , PAPER , SCISSORS to play")
        print("`````````````````````````````````````````````````````````````````````")
        print("`````````````````````````````````````````````````````````````````````")
        player_choice = input("Enter your choice: ").upper()

        if validate_input(player_choice):
            computer_choice = choice(choices)
            # Players Moves
            print(f"Player ({mapped_values[player_choice]}) : Computer ({computer_choice})")
            
            result = brain_box(mapped_values[f"{player_choice}"] ,computer_choice)
            if result['winner'] == "None":
                print(f"{result['result']} between Player and Computer")
            else:
                print("##########-----------------------------------------------------##########")
                print("                          RESULT                                         ")
                print("##########-----------------------------------------------------##########")
                if result['winner'] == "None":
                    print(f"           {result['result']} between Player and Computer")
                else:
                    print(f"""    
                            WINNER: {result['winner']} by playing {mapped_values[f'{player_choice}']  if result['winner'] == 'Player' else computer_choice} and {result['result']} {computer_choice if result['winner'] == 'Player' else mapped_values[f'{player_choice}'] }
                        """)
                game_continue=input("Do you wish to play again? (y/n): ").lower()=='n'
                
                if  game_continue:
                    game_on=False
                    print(f"Thanks you for playing... Come back soon! {player_name}.")

        else:
            print(f"{player_choice} is an Invalid input. Please try again")

# start game
game_engine()