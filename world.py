from characters import Player
import enemy
import weapons as wea


class MapTile:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return self.name

    def intro_text(self):
        raise NotImplementedError("create a subclass instead")


class Ethereal(MapTile):
    def __init__(self, x, y):
        self.name = "Ethereal"
        self.enemy = enemy.Ethereal()

        super().__init__(x, y)

    def attack_player(self):
        pass

    def intro_text(self):
        pass


class Juliot(MapTile):
    def __init__(self, x, y):
        self.name = "Juliot"

        super().__init__(x, y)

    def intro_text(self):
        pass


class Kytersize(MapTile):
    def __init__(self, x, y):
        self.name = "Kytersize"

        super().__init__(x, y)

    def intro_text(self):
        pass


class Where(MapTile):
    def __init__(self, x, y):
        self.name = "Where are we now"

        super().__init__(x, y)

    def intro_text(self):
        pass


class Hooligan(MapTile):
    def __init__(self, x, y):
        self.name = "Hooligan"

        super().__init__(x, y)

    def intro_text(self):
        pass


class Residential(MapTile):
    def __init__(self, x, y):
        self.name = "Residential"

        super().__init__(x, y)

    def intro_text(self):
        pass


class Loot(MapTile):
    def __init__(self, x, y):
        self.name = '*'
        self.lootinventory = [wea.Maggot(), wea.Bread(), wea.Sandwich()]
        self.index = 0

        super().__init__(x, y)


world_map = [[None, None, Ethereal(2, 0), None, None],
             [None, None, None, None, None],
             [Juliot(0, 2), None, None, None, Kytersize(4, 2)],
             [None, None, None, None, None],
             [None, Where(1, 4), None, Hooligan(3, 4), None],
             [None, None, Residential(2, 5), None, None],
             [None, None, None, Player(3, 6), None]]


def tile_at(x, y):
    if x < 0 or y < 0:
        return None
    try:
        return world_map[y][x]
    except IndexError:
        return None
