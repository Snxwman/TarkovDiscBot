from dataclasses import dataclass
from enum import Enum

@dataclass
class Traders(Enum):
    PRAPOR = 'Prapor'
    THERAPIST = 'Therapist'
    FENCE = 'Fence'
    SKIER = 'Skier'
    PEACEKEEPER = 'Peacekeeper'
    MECHANIC = 'Mechanic'
    RAGMAN = 'Ragman'
    JAEGER = 'Jaeger'
    REF = 'Ref'