# CS 30
# Period 4
# Date : 11/18/2019
# Krutik Rana
# Program description : Seperate file for Characters


class Player:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.playername = "X"

    def __str__(self):
        return self.playername

    def move(self, dx, dy):
        self.x = self.x + dx
        self.y = self.y + dy

    def move_north(self):
        self.move(dx=0, dy=-1)

    def move_south(self):
        self.move(dx=0, dy=1)

    def move_east(self):
        self.move(dx=1, dy=0)

    def move_west(self):
        self.move(dx=-1, dy=0)


def all_characters():
    """Commands to list out characters and enemies of the game"""
    while True:
        # Creates a new line
        print('\n')
        # Tells user how to go back to prevous menu
        print('Type q to go back to the previous menu')
        # Asks for the user input to continue
        user = input('Type [friendly characters] or [enemies] to list characters:\
 ')
        # Lowers all user inputs to satisfy if/elif/else statements
        user = user.lower()
        # Checks to see if user typed in friendly characters
        if user == 'friendly characters':
            # Special loop that loops through all friendly characters
            for k, v in characters.items():
                # If name is Xunerophore then special print statement
                if k == "Xunerophore":
                    print(f"The main character is {k} with {v}HP")
                # If name is Shopkeeper then special print statement
                elif k == "Shopkeeper":
                    print(f"The {k} is {v}")
        # Checks to see if user typed in enemies
        elif user == 'enemies':
            # Special loop that lists the enemies in the game
            for k, v in enemies.items():
                print(f"{k} is an enemy with {v['HP']}HP and {v['Attack']} Attack\
 Damage")
        # Checks to see if user typed in q
        elif user == 'q':
            # quits this part of the menu
            break
        # If user typed in anything else
        else:
            # Tells user the input is invalid
            print('invalid input')


# Dictionary of friendly characters with values
characters = {
    "Xunerophore": "100", "Shopkeeper": "the person you can buy\
 items from."
             }

# Dictionary of Enemies with values
enemies = {'Salmon': {'HP': 10, 'Attack': 2},
           'GoldFish': {'HP': 5, 'Attack': 1},
           'Guppy': {'HP': 3, 'Attack': 2},
           'Hammerhead Shark': {'HP': 15, 'Attack': 4},
           'The Great White': {'HP': 20, 'Attack': 8},
           'Saw Shark': {'HP': 25, 'Attack': 6},
           'Ethereal Ultimatum': {'HP': 1000, 'Attack': 20}
           }
