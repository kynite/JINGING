# CS 30
# Period 4
# Date : 12/9/2019
# Krutik Rana
# Program description : Map of the game

from characters import Player


class MapTile:
    """Parent Class to child classes in terms of position and naming"""
    def __init__(self, x, y):
        # x position of map tiles
        self.x = x
        # y position of map tiles
        self.y = y

    def __str__(self):
        """Gets the name of the child class and makes it a string"""
        return self.name


class Ethereal(MapTile):
    """Final Lake Location containing hardest boss and victory for player"""
    def __init__(self, x, y):
        self.name = "Ethereal"
        # Position of Ethereal tile
        super().__init__(x, y)


class Juliot(MapTile):
    """Lake location containing Legendary fish"""
    def __init__(self, x, y):
        self.name = "Juliot"
        # Position of Juliot tile
        super().__init__(x, y)


class Kytersize(MapTile):
    """Lake location containing hard fish"""
    def __init__(self, x, y):
        self.name = "Kytersize"
        # Position of Kytersize tile
        super().__init__(x, y)


class Where(MapTile):
    """Lake location containing normal difficulty fish"""
    def __init__(self, x, y):
        self.name = "Where are we now"
        # Position of Where are we now tile
        super().__init__(x, y)


class Hooligan(MapTile):
    """Lake location containing easy difficutly fish"""
    def __init__(self, x, y):
        self.name = "Hooligan"
        # Position of Hooligan tile
        super().__init__(x, y)


class Residential(MapTile):
    """Lake containing trader to obtain items"""
    def __init__(self, x, y):
        self.name = "Residential"
        # Position of Residential tile
        super().__init__(x, y)


# The map
world_map = [[None, None, Ethereal(2, 0), None, None],
             [None, None, None, None, None],
             [Juliot(0, 2), None, None, None, Kytersize(4, 2)],
             [None, None, None, None, None],
             [None, Where(1, 4), None, Hooligan(3, 4), None],
             [None, None, Residential(2, 5), None, None],
             [None, None, None, Player(3, 6), None]]
