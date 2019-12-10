# CS 30
# Period 4
# Date : 12/9/2019
# Krutik Rana
# Program description : The Player and extra info about characters
import weapons as wp


class Player:
    """
    Player class which contains player logic and is what the user controls.
    Holds healing capability and best weapon
    """
    def __init__(self, x, y):
        self.inventory = [wp.Stick(), wp.Bread()]  # Player inventory
        self.playername = "X"  # Player name
        self.hp = 45  # Player health
        self.victory = False  # Player victory
        self.gold = 0  # Player gold

    def print_inventory(self):
        """Prints the players inventory"""
        print("Backpack:")
        # Loop for each item in the players inventory
        for item in self.inventory:
            print('* ' + str(item))
        # Assigns the best weapon
        best_weapon = self.most_powerful_weapon()
        # print statement telling the best weapon in inventory
        print("Your best weapon is your {}".format(best_weapon))

    def most_powerful_weapon(self):
        """Determines the most damaging weapon in Players inventory"""
        # sets inital damge to 0
        max_damage = 0
        # sets the best weapon to nothing
        best_weapon = None
        # Loop for each item in inventory
        for item in self.inventory:
            # Code adapted from Make Your own Python Text Based Adventure
            # tries to see if the item damage is greator than the current max
            # damage and then replaces the best weapon in inventory
            try:
                if item.damage > max_damage:
                    best_weapon = item
                    max_damage = item.damage
            except AttributeError:
                pass
        # sends the best weapon to function
        return best_weapon

    def is_alive(self):
        """Checks if player is alive"""
        return self.hp > 0

    def __str__(self):
        """Gets the name of the player and makes it a string"""
        return self.playername

    def heal(self):
        """
        Heals the player making the players HP go up, Code adapted from Make
        Your own Python Text Based Adventure
        """
        # Creates a list of consumables from the players inventory
        consumables = [item for item in self.inventory
                       if isinstance(item, wp.Consumable)]
        # If there are no consumables then tells player he has not healing item
        if not consumables:
            print("You don't have any items to heal you!")
            return
        # Shows an item that can heal you
        for i, item in enumerate(consumables, 1):
            print("Choose an item to use to heal: ")
            print("{}. {}".format(i, item))

            valid = False
            while not valid:
                print("type the number associated with the item to use otherw\
ise type q to not use")
                # Gets user input of what item they want to use to heal
                choice = input("")
                # Checks to see if user typed in q
                if choice == 'q':
                    # Deny the heal of that particular item/cancel the heal
                    break
                # Any other option
                else:
                    # Uses the item and heals the player and then removes the
                    # item from the players inventory
                    try:
                        to_eat = consumables[int(choice) - 1]
                        self.hp = min(100, self.hp + to_eat.healing_value)
                        self.inventory.remove(to_eat)
                        print("Current HP: {}".format(self.hp))
                        valid = True
                    except (ValueError, IndexError):
                        print("Invalid choice, try again.")


def all_characters():
    """
    Commands to list out characters and enemies of the game, and provide
    information about them
    """
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
                    print(f"The main character is {k} with {v} Starting HP")
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
