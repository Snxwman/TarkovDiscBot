from enum import auto, Enum
from dataclasses import dataclass

class ItemRarity(Enum):
    COMMON = auto()
    UNCOMMON = auto()
    RARE = auto()
    LEGENDARY = auto()
    MYTHIC = auto()

@dataclass
class ItemDataMixin:
    category = str
    slot = str
    name = str
    rarity = ItemRarity
    weight = int
    sold_by = str
    description = str
    grid_size = int