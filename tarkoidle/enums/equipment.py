from enum import Enum
from dataclasses import dataclass
from tarkoidle.enums.items import ItemRarity

class HelmetArmoredAreas(Enum):
    HEAD_TOP = 'Head top'
    NAPE = 'Nape'
    EARS = 'Ears'

class HelmetPenalties(Enum):
    MOVE_SPEED = 'Movement speed'
    TURN_SPEED = 'Turn Speed'
    ERGO = 'Ergonomics'
    SOUND_REDUCTION = 'Sound reduction'

@dataclass

class HelmetDataMixin:
    rarity: ItemRarity
    helemt_name: str
    helmet_material: str
    helmet_weight: int
    helmet_armor_class: int
    helmet_armored_areas: list[HelmetArmoredAreas]
    helmet_durability: int
    richochet_chance: str
    helmet_penalties: list[HelmetPenalties]
    blocks_headset: bool
    blocks_eyewear: bool
    blocks_facecover: bool

class Helmet(HelmetDataMixin, Enum):

    ALTYN = (ItemRarity.MYTHIC, 'Altyn bulletproof helmet', 'Armor steel', 2500, 5, 
             [HelmetArmoredAreas.HEAD_TOP, HelmetArmoredAreas.NAPE, HelmetArmoredAreas.EARS],
             81, 'High', [HelmetPenalties.MOVE_SPEED, HelmetPenalties.TURN_SPEED, HelmetPenalties.ERGO, HelmetPenalties.SOUND_REDUCTION],
             True, False, False)


