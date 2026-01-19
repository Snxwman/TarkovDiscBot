from dataclasses import dataclass
from enum import Enum, auto


class ItemRarity(Enum):
    COMMON = auto()
    UNCOMMON = auto()
    RARE = auto()
    LEGENDARY = auto()
    MYTHIC = auto()

@dataclass
class ItemData:
    category: str
    slot: str
    name: str
    rarity: ItemRarity
    weight: int
    sold_by: str
    description: str
    grid_size: int
