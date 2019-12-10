# CS 30
# Period 4
# Date : 11/18/2019
# Krutik Rana
# Program description : Locations in a seperate file
from tabulate import tabulate
from world import *
import world
from characters import Player
import Hooligan as hg


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
            for y, row in enumerate(world.world_map):
                for x, object in enumerate(row):
                    if isinstance(object, Player):
                        if isinstance(world.world_map[y - 1][x], Hooligan):
                            hg.hooligan_lake()
                        elif isinstance(
                                world.world_map[y - 1][x], Residential):
                            hg.residential()
                        elif isinstance(world.world_map[y - 1][x], Where):
                            hg.where_are_we_now()
                        elif isinstance(world.world_map[y - 1][x], Kytersize):
                            hg.kytersize()
                        elif isinstance(world.world_map[y - 1][x], Juliot):
                            hg.juliot()
                        elif isinstance(world.world_map[y - 1][x], Ethereal):
                            hg.ethereal()
                        else:
                            world.world_map[y - 1][x] = object
                            world.world_map[y][x] = None
        # Checks to see if user typed in movement command
        elif user == 'west':
            for y, row in enumerate(world.world_map):
                for x, object in enumerate(row):
                    if isinstance(object, Player):
                        if isinstance(world.world_map[y][x - 1], Hooligan):
                            hg.hooligan_lake()
                        elif isinstance(
                                world.world_map[y][x - 1], Residential):
                            hg.residential()
                        elif isinstance(world.world_map[y][x - 1], Where):
                            hg.where_are_we_now()
                        elif isinstance(world.world_map[y][x - 1], Kytersize):
                            hg.kytersize()
                        elif isinstance(world.world_map[y][x - 1], Juliot):
                            hg.juliot()
                        elif isinstance(world.world_map[y][x - 1], Ethereal):
                            hg.ethereal()
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
                            hg.hooligan_lake()
                        elif isinstance(
                                world.world_map[y][x + 1], Residential):
                            hg.residential()
                        elif isinstance(world.world_map[y][x + 1], Where):
                            hg.where_are_we_now()
                        elif isinstance(world.world_map[y][x + 1], Kytersize):
                            hg.kytersize()
                        elif isinstance(world.world_map[y][x + 1], Juliot):
                            hg.juliot()
                        elif isinstance(world.world_map[y][x + 1], Ethereal):
                            hg.ethereal()
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
                            hg.hooligan_lake()
                        elif isinstance(
                                world.world_map[y + 1][x], Residential):
                            hg.residential()
                        elif isinstance(world.world_map[y + 1][x], Where):
                            hg.where_are_we_now()
                        elif isinstance(world.world_map[y + 1][x], Kytersize):
                            hg.kytersize()
                        elif isinstance(world.world_map[y + 1][x], Juliot):
                            hg.juliot()
                        elif isinstance(world.world_map[y + 1][x], Ethereal):
                            hg.ethereal()
                        else:
                            world.world_map[y + 1][x] = object
                            world.world_map[y][x] = None
                            location()
                            return
            # Checks to see if user typed q
        elif user == 'q':
            # Quits this part of the menu
            break
        # Checks to see if user typed anything else
        else:
            # Tells user it is an invalid option
            print('invalid option')
