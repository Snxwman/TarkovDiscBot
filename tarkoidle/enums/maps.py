from enum import Enum, unique
from typing import final


@final
class MapVariantData:
    loot_pool = list[str]

@unique
class MapVariant(Enum):
    WOODS = (
        ['nothing']
    )
