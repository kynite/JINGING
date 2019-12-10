# CS 30
# Period 4
# Date : 12/9/2019
# Krutik Rana
# Program description : Main game file to run all code
import inventory as inv
import locations as loc
import characters as ch


def ingame_menu():
    """The menu that appears after the main menu/the first menu"""
    # While loop for continous play
    while True:
        # Tells user that typing q goes to the main menu
        print('type q to go back to the main menu')
        # Asks for user input
        menu = input('type map/inventory/characters: ')
        # Makes all the user input into lower case
        menu = menu.lower()
        # Checks to see if user typed inventory
        if menu == 'inventory':
            # Tells user to type in certain commands to access further menus
            print('type [backpack], [heal]')
            # Runs the inventory function
            inv.inventory()
        # Checks to see if user typed location
        elif menu == 'map':
            # Runs the location function
            loc.location()
        elif menu == 'characters':
            ch.all_characters()
        # Checks to see if user typed in q
        elif menu == 'q':
            # Goes to main menu
            break
        # Checks to see if anything else was typed in
        else:
            # Tells user that was an invalid selection
            print('invalid select again')


def main_menu():
    """The main menu of the game, the first one you see"""
    # While loop for continous play
    while True:
        # Prints out name of the game
        print('Ethereal Ultimatum')
        # Just something to seperate the title
        print('----------------')
        # Informs user to type y to play the game
        print('type y to play the game')
        # Informs user to type q to quit the game
        print('type q to quit the game')
        # Gets user input
        selection = input('Make your selection: ')
        # Converts user input into all lower case
        selection = selection.lower()
        # Checks to see if y is typed
        if selection == 'y':
            # Runs the ingame menu function
            ingame_menu()
        # Checks to see if q is typed
        elif selection == 'q':
            # Ends the game
            break
        # Checks to see if anything else is typed
        else:
            # Tells user it is an invalid option
            print('Invalid option')


# Calls main menu function
main_menu()
