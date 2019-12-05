# CS 30
# Period 4
# Date : 11/18/2019
# Krutik Rana
# Program description : Inventory in a seperate file


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
            # Loop that lists out weapons and their stats
            for k, v in weapons_inventory.items():
                print(f"In your weapon stash you have a {k} that deals {v} Dam\
age")
        # Checks to see if user typed fishing rod
        elif user == 'fishing rod':
            # Loop that lists out fishing rods in inventory and their stats
            for k in fishingrod_inventory:
                print(f"\nIn your fishing rod stash you have a {k}:")
                for v in fishingrod_inventory[k]:
                    print(f"This fishing rod can capture {v}")
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
# Creates a dictionary with a list of uses for the fishing rods
fishingrod_inventory = {'Basic rod': ['Salmon', 'GoldFish', 'Guppy'],
                        'Better rod': ['Hammerhead Sharks', 'The Great White',
                                       'Saw Sharks'],
                        'Ethereal Rod': ['Ethereal Ultimatum']
                        }
# Creates a dictionary of items that can heal you
healthitems_inventory = {'Sandwich': 20, 'Medkit': 50, 'Pills': '5',
                         'Grass': 10
                         }
