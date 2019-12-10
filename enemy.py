# CS 30
# Period 4
# Date : 12/9/2019
# Krutik Rana
# Program description : Enemies of the game and their attributes


class Enemy():
    """Parent class of Enemies determining name and health"""
    def __init__(self):
        # Creates a warning to not create raw enemies
        raise NotImplementedError("Do not create raw Enemy objects")

    def __str__(self):
        """Gets the name of the child class and makes it a string"""
        return self.name

    def is_alive(self):
        """Gets the amount of health the enemy has to see if it still lives"""
        return self.hp > 0


class Salmon(Enemy):
    """An enemy the player might face"""
    def __init__(self):
        # Name of the enemy
        self.name = "Salmon"
        # Amount of health the enemy has
        self.hp = 10
        # Damage the enemy does to player
        self.damage = 2


class GoldFish(Enemy):
    """An enemy the player might face"""
    def __init__(self):
        # Name of the enemy
        self.name = 'Goldfish'
        # Amount of health the enemy has
        self.hp = 5
        # Damage the enemy does to player
        self.damage = 1


class Guppy(Enemy):
    """An enemy the player might face"""
    def __init__(self):
        # Name of the enemy
        self.name = 'Guppy'
        # Amount of health the enemy has
        self.hp = 3
        # Damage the enemy does to player
        self.damage = 2


class Hammerhead(Enemy):
    """An enemy the player might face"""
    def __init__(self):
        # Name of the enemy
        self.name = 'Hammerhead Shark'
        # Amount of health the enemy has
        self.hp = 15
        # Damage the enemy does to player
        self.damage = 4


class GreatWhite(Enemy):
    """An enemy the player might face"""
    def __init__(self):
        # Name of the enemy
        self.name = 'Great White Shark'
        # Amount of health the enemy has
        self.hp = 20
        # Damage the enemy does to player
        self.damage = 8


class SawShark(Enemy):
    """An enemy the player might face"""
    def __init__(self):
        # Name of the enemy
        self.name = 'Saw Shark'
        # Amount of health the enemy has
        self.hp = 25
        # Damage the enemy does to player
        self.damage = 6


class Ethereal(Enemy):
    """An enemy the player will have to face to win"""
    def __init__(self):
        # Name of the enemy
        self.name = 'Ethereal Ultimatum'
        # Amount of health the enemy has
        self.hp = 1000
        # Damage the enemy does to player
        self.damage = 20
