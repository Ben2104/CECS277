#main.py
from die import Die
from player import Player  
import check_input

def main():
    player = Player()
    choice = True
    print("-Yahtzee-")
    print()
    while choice != False:
        take_turn(player)
        choice = check_input.get_yes_no("Play Again? Y/N: ")
        
    print("Game Over")
    print("Final Score: ", player.get_points())
def take_turn(player):
    ''' Takes a yahtzee turn for the player

    Args:
        - player (Player): player class representing the user

    Returns: none
    '''
    player.roll_dice()
    print(player)
    if player.has_pair():
        print("You got a pair!")
    elif player.has_three_of_a_kind():
        print("You got 3 of a kind!")
    elif player.has_series():
        print("You got a series of 3!")
    else:
        print("Aww. Too Bad.")
    
    print("Score =", player.get_points())
main()