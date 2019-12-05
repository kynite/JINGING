# CS 30
# Period 4
# Date : 11/18/2019
# Krutik Rana
# Program description : Locations in a seperate file
from tabulate import tabulate
from world import *
import world
from characters import Player


def location():
    global world_map
    """Commands that allow for movement on the map"""
    # While loop for continous play
    while True:
        # Prints map out in a grid style using tabulate
        print(tabulate(world.world_map, tablefmt="grid"))
        # Tells user to type q to go to the previous menu
        print('\ntype q to go back to previous menu')
        print('North')
        print('West')
        print('East')
        print('South')
        # Asks for user input of what location they would like to go to
        user = input('Select a Movement: ')
        # Makes all user inputs lower cased to match if and elif statements
        user = user.lower()
        # Checks to see if user typed in movement command
        if user == 'north':
            # characters.Player().move_north()
            # # prints out Movement
            # print('Travelling North!')
            for y, row in enumerate(world.world_map):
                for x, object in enumerate(row):
                    if isinstance(object, Player):
                        if isinstance(world.world_map[y - 1][x], Hooligan):
                            pass
                        else:
                            world.world_map[y - 1][x] = object
                            world.world_map[y][x] = None
        # Checks to see if user typed in movement command
        elif user == 'west':
            for y, row in enumerate(world.world_map):
                for x, object in enumerate(row):
                    if isinstance(object, Player):
                        if isinstance(world.world_map[y][x - 1], Hooligan):
                            pass
                        else:
                            world.world_map[y][x - 1] = object
                            world.world_map[y][x] = None
        # Checks to see if user typed in movement command
        elif user == 'east':
            for y, row in enumerate(world.world_map):
                for x, object in enumerate(row):
                    if isinstance(object, Player):
                        print(x)
                        if isinstance(world.world_map[y][x + 1], Hooligan):
                            pass
                        else:
                            world.world_map[y][x + 1] = object
                            world.world_map[y][x] = None
                        break
        # Checks to see if user typed in movement command
        elif user == 'south':
            for y, row in enumerate(world.world_map):
                for x, object in enumerate(row):
                    if isinstance(object, Player):
                        if isinstance(world.world_map[y + 1][x], Hooligan):
                            pass
                        else:
                            world.world_map[y + 1][x] = object
                            world.world_map[y][x] = None
            # Checks to see if user typed q
        elif user == 'q':
            # Quits this part of the menu
            break
        # Checks to see if user typed anything else
        else:
            # Tells user it is an invalid option
            print('invalid option')


# Creates a dictionary with a list of fishes available at each lake
locations = {'Hooligan Lake': ['Salmon', 'GoldFish', 'Guppy'],
             'Where are we now Lake': ['Hammerhead Sharks', 'The Great White',
                                       'Saw Sharks'],
             'Ethereal Lake': ['Ethereal Ultim\
atum'], 'Residential Lake': ['Shopkeeper'],
             }
