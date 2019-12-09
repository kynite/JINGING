class WeaponName:
    def __str__(self):
        return self.name


class Stick(WeaponName):
    def __init__(self):
        self.name = 'stick'
        self.damage = 1


class Bat(WeaponName):
    def __init__(self):
        self.name = 'bat'
        self.damage = 3


class SpikedBat(WeaponName):
    def __init__(self):
        self.name = 'spiked bat'
        self.damage = 5


class Sword(WeaponName):
    def __init__(self):
        self.name = 'sword'
        self.damage = 10
