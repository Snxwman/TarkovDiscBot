from tarkoidle.models.inventory import GridSize
from tarkoidle.enums.items import ItemCategory, ItemSlot, ItemRarity
from tarkoidle.enums.traders import Traders
from tarkoidle.enums.weapon import FireMode, WeaponCaliber
# category = enum
# slot = enum
# name = str
# description = str
# rarity = ItemRarity
# weight = int
# sold_by = enum
# base_value = int
# grid_size = enum
# durability: int
# ergonomics: int
# accuracy: int
# recoil: int
# muzzle_velocity: int
# fire_mode: list[FireMode]
# caliber: WeaponCaliber
# fire_rate: int
# effective_distance: int

#Adar 215 Constant
ADAR_2_15_CATEGORY = ItemCategory.WEAPON
ADAR_2_15_SLOT = [ItemSlot.PRIMARY_WEAPON, ItemSlot.SECONDARY_WEAPON]
ADAR_2_15_NAME = 'ADAR 2-15'
ADAR_2_15_DESCRIPTION = 'A cheap but versitile carbine.'
ADAR_2_15_RARITY = ItemRarity.COMMON
ADAR_2_15_WEIGHT = 3267
ADAR_2_15_SOLD_BY = Traders.SKIER
ADAR_2_15_BASE_VALUE = 45333
ADAR_2_15_GRID_SIZE = GridSize(height = 6, width = 2)
ADAR_2_15_DURABILITY = 100000
ADAR_2_15_ERGONOMICS = 60500
ADAR_2_15_ACCURACY = 2200
ADAR_2_15_VERTICAL_RECOIL = 84000
ADAR_2_15_HORIZONTAL_RECOIL = 241000
ADAR_2_15_FIRE_MODE = [FireMode.SemiAuto]
ADAR_2_15_CALIBER = WeaponCaliber.AMMO_5_56x45MM
ADAR_2_15_FIRERATE = 800000
ADAR_2_15_EFFECTIVE_DISTANCE = 500000
