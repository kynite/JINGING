class Enemy():
    """s"""
    def __init__(self):
        raise NotImplementedError("Do not create raw Enemy objects")

    def __str__(self):
        return self.name

    def is_alive(self):
        return self.hp > 0


class Salmon(Enemy):
    """s"""
    def __init__(self):
        self.name = "Salmon"
        self.hp = 10
        self.damage = 2


class GoldFish(Enemy):
    """s"""
    def __init__(self):
        self.name = 'Goldfish'
        self.hp = 5
        self.damage = 1


class Guppy(Enemy):
    """s"""
    def __init__(self):
        self.name = 'Guppy'
        self.hp = 3
        self.damage = 2


class Hammerhead(Enemy):
    """s"""
    def __init__(self):
        self.name = 'Hammerhead Shark'
        self.hp = 15
        self.damage = 4


class GreatWhite(Enemy):
    """s"""
    def __init__(self):
        self.name = 'Great White Shark'
        self.hp = 20
        self.damage = 8


class SawShark(Enemy):
    """s"""
    def __init__(self):
        self.name = 'Saw Shark'
        self.hp = 25
        self.damage = 6


class Ethereal(Enemy):
    """s"""
    def __init__(self):
        self.name = 'Ethereal Ultimatum'
        self.hp = 1000
        self.damage = 20
