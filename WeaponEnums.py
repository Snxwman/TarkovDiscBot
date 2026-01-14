from enum import Enum
from dataclasses import dataclass
from items import ItemRarity

class WeaponType(Enum):
    ASSAULT_CARBINE = "Assault Carbine"
    ASSAULT_RIFLE = "Assault Rifle"
    BOLT_ACTION = "Bolt-Action Rifle"
    DMR = "Designated Marksman Rifle"
    GL = "Grenade Launcher"
    LMG = "Light Machine Gun"
    ROCKET_LAUNCHER = "Rocket Launcher"
    SHOTGUN = "Shotgun"
    SMG = "Submachine Gun"

class WeaponCaliber(Enum):
    AMMO_9x19MM = "9x19mm Parabellum"
    AMMO_5_45x39MM = "5.45x39mm"
    AMMO_5_56x45MM = "5.56x45mm NATO"
    AMMO_7_62x39MM = "7.62x39mm"
    AMMO_7_62x51MM = "7.62x51mm NATO"
    AMMO_12GAUGE = "12 Gauge"
    AMMO_40MM = "40mm Grenade"
    AMMO_4_6x30MM = "4.6x30mm"

class FireMode(Enum):
    SingleShot = "Single Shot"
    SemiAuto = "Semi Auto"
    Burst = "Burst"
    FullAuto = "Full Auto"

@dataclass
class WeaponDataMixin:
    rarity: ItemRarity
    weapon_name: str
    weapon_type: WeaponType
    description: str
    durability: int
    weight: int
    ergonomics: int
    accuracy: int
    recoil: int
    muzzle_velocity: int
    fire_mode: list[FireMode]
    caliber: WeaponCaliber
    fire_rate: int
    effective_distance: int

class Weapon(WeaponDataMixin, Enum):
    #Assault Carbines
    ADAR_2_15 = (ItemRarity.COMMON,"ADAR 2-15",WeaponType.ASSAULT_CARBINE, 
    "A reliable and versatile assault carbine.",
    100, 3267, 60.5, 2.2, 84, 905, [FireMode.SemiAuto], WeaponCaliber.AMMO_5_56x45MM, 800, 500)



#MOVE ALL THIS INTO THE DATA CLASS
class WeaponName(Enum):

    #ASSAULT CARBINES

    OP_SKS = "OP-SKS"
    RFB = "RFB"
    SR_3M = "SR-3M"
    VPO_101 = "VPO-101"
    VSK_94 = "VSK-94"

    #ASSAULT RIFLES

    AK_74 = "AK-74"
    AKM = "AKM"
    AS_VAL = "AS VAL"
    M4A1 = "M4A1"
    SA_58 = "SA-58"

    #BOLT-ACTION RIFLES

    AXMC = "AXMC"
    DVL_10 = "DVL-10"
    MARLIN_MXLR = "Marlin MXLR"
    T_5000M = "T-5000M"
    VPO_215 = "VPO-215"

    #DESIGNATED MARKSMAN RIFLES

    SR_25 = "SR-25"
    SVDS = "SVDS"
    G28 = "G28"
    M1A = "M1A"

    #GRENADES LAUNCHERS

    FN40GL = "FN40GL"
    M32A1 = "M32A1"

    #LIGHT MACHINE GUNS

    M60E4 = "M60E4"
    RPK_16 = "RPK-16"
    PKM = "PKM"

    #ROCKET LAUNCHERS

    RSHG2 = "RShG-2"

    #SHOTGUNS

    AA_12_GEN_1 = "AA-12 Gen1"
    M870 = "M870"
    MP_153 = "MP-153"
    TOZ_106 = "TOZ-106"
    SAIGA_12K = "Saiga-12K"

    #SUBMACHINE GUNS

    MP5 = "MP5"
    MP7A1 = "MP7A1"
    MP9 = "MP9"
    VECTOR_45 = "Vector .45"
    SR_2M = "SR-2M"

    #SECONDARY WEAPONS

    BLICKY = "Blicky"
    GLOCK_18C = "Glock 18C" 
    M1911A1 = "M1911A1"



    





