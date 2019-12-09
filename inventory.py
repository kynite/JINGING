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
        if user == 'weapon':
            player.print_inventory()
        # Checks to see if user typed heal
        elif user == 'heal':
            # Loop that lists out health items in inventory
            for k, v in healthitems_inventory.items():
                print(f"In your backpack you are carrying {k} that heals\
 for {v}HP")
        # Checks to see if user typed q
        elif user == 'q':
            # Quits this part of the menu
            break
        # Checks to see if the user typed anything else
        else:
            # Tells user it is an invalid option
            print('Invalid option')


weapons_inventory = {'Stick': 1, 'Bat': 3, 'Spiked Bat': 5, 'Sword': 10}
# Creates a dictionary of items that can heal you
healthitems_inventory = {'Sandwich': 20, 'Medkit': 50, 'Pills': '5',
                         'Grass': 10
                         }
