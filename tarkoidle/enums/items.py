from enum import auto, Enum
from dataclasses import dataclass

class ItemRarity(Enum):
    COMMON = auto()
    UNCOMMON = auto()
    RARE = auto()
    LEGENDARY = auto()
    MYTHIC = auto()

class ItemCategory(Enum):
    WEAPON = 'Weapon'

class ItemSlot(Enum):
    PRIMARY_WEAPON = 'On sling'
    SECONDARY_WEAPON = 'On back'
    SIDEARM = 'Holster'
    KNIFE = 'Sheath'


@dataclass
class ItemData:
    category = str
    slot = str
    name = str
    description = str
    rarity = ItemRarity
    weight = int
    sold_by = str
    base_value = int
    trader_buy_value = int
    trader_sell_value = int
    grid_size = int




   
