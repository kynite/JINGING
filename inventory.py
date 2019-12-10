# CS 30
# Period 4
# Date : 11/18/2019
# Krutik Rana
# Program description : Inventory in a seperate file
from characters import Player

player = Player(None, None)


def inventory():
    """Commands to access the characters inventory"""
    # While loop to continously play
    while True:
        # Print statement detailing how to go to the last menu
        print('\ntype q to go back to previous menu')
        # Aquiring user input for what they want to access of the inventory
        user = input('action: ')
        # Making the user input all lower case to match if and elif statements
        user = user.lower()
        # Checks to see if the user typed weapon
        if user == 'backpack':
            player.print_inventory()
        # Checks to see if user typed heal
        elif user == 'heal':
            player.heal()
        # Checks to see if user typed q
        elif user == 'q':
            # Quits this part of the menu
            break
        # Checks to see if the user typed anything else
        else:
            # Tells user it is an invalid option
            print('Invalid option')
