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


class Consumable:
    def __init__(self):
        raise NotImplementedError("dont create raw objects")

    def __str__(self):
        return "{} (+{} HP)".format(self.name, self.healing_value)


class Sandwich(Consumable):
    def __init__(self):
        self.name = 'Sandwich'
        self.healing_value = 10


class Bread(Consumable):
    def __init__(self):
        self.name = 'Bread'
        self.healing_value = 5
