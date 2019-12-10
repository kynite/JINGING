# CS 30
# Period 4
# Date : 11/18/2019
# Krutik Rana
# Program description : Seperate file for Characters
import weapons as wp


class Player:
    def __init__(self, x, y):
        self.inventory = [wp.Stick(), wp.Bread()]
        self.x = x
        self.y = y
        self.playername = "X"
        self.hp = 45
        self.victory = False
        self.gold = 0

    def print_inventory(self):
        print("Backpack:")
        for item in self.inventory:
            print('* ' + str(item))
        best_weapon = self.most_powerful_weapon()
        print("Your best weapon is your {}".format(best_weapon))

    def most_powerful_weapon(self):
        max_damage = 0
        best_weapon = None
        for item in self.inventory:
            try:
                if item.damage > max_damage:
                    best_weapon = item
                    max_damage = item.damage
            except AttributeError:
                pass

        return best_weapon

    def is_alive(self):
        return self.hp > 0

    def __str__(self):
        return self.playername

    def heal(self):
        consumables = [item for item in self.inventory
                       if isinstance(item, wp.Consumable)]
        if not consumables:
            print("You don't have any items to heal you!")
            return

        for i, item in enumerate(consumables, 1):
            print("Choose an item to use to heal: ")
            print("{}. {}".format(i, item))

            valid = False
            while not valid:
                print("type the number associated with the item to use otherw\
ise type q to not use")
                choice = input("")
                if choice == 'q':
                    break
                else:
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
