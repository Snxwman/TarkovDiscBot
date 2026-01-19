from tarkoidle.enums.weapon import WeaponType, WeaponCaliber


class Weapon:
    def __init__(self, name, type: WeaponType, caliber: WeaponCaliber, weight, size):
        self.name = name
        self.type = type
        self.caliber = caliber
        self.weight = weight
        self.size = size

