from dataclasses import dataclass
from enum import Enum

from tarkoidle.enums.items import ItemData


class WeaponType(Enum):
    ASSAULT_CARBINE = 'Assault Carbine'
    ASSAULT_RIFLE = 'Assault Rifle'
    BOLT_ACTION = 'Bolt-Action Rifle'
    DMR = 'Designated Marksman Rifle'
    GL = 'Grenade Launcher'
    LMG = 'Light Machine Gun'
    ROCKET_LAUNCHER = 'Rocket Launcher'
    SHOTGUN = 'Shotgun'
    SMG = 'Submachine Gun'
    PISTOL = 'Pistol'


class WeaponCaliber(Enum):
    AMMO_9x19MM = '9x19mm Parabellum'
    AMMO_9x21MM = '9x21mm'
    AMMO_9x39MM = '9x39mm'
    AMMO_5_45x39MM = '5.45x39mm'
    AMMO_5_56x45MM = '5.56x45mm NATO'
    AMMO_7_62x39MM = '7.62x39mm'
    AMMO_7_62x51MM = '7.62x51mm NATO'
    AMMO_12GAUGE = '12 Gauge'
    AMMO_20GAUGE = '20 Gauge'
    AMMO_40MM = '40mm Grenade'
    AMMO_4_6x30MM = '4.6x30mm'
    AMMO_366_TKM = '366 TKM'
    AMMO_7_62x54R = '7.62x54R'
    AMMO_72_5MM = '72.5mm Rocket'
    AMMO_45_ACP = '.45 ACP'
    AMMO_20x1MM = '20x1mm'


class FireMode(Enum):
    SingleShot = 'Single Shot'
    SemiAuto = 'Semi Auto'
    Burst = 'Burst'
    FullAuto = 'Full Auto'


@dataclass
class WeaponData(ItemData):
    # category = str
    # slot = str
    # name = str
    # description = str
    # rarity = ItemRarity
    # weight = int
    # sold_by = str
    # base_value = int
    # trader_buy_value = int
    # trader_sell_value = int
    # grid_size = int
    durability: int
    ergonomics: int
    accuracy: int
    recoil: int
    muzzle_velocity: int
    fire_mode: list[FireMode]
    caliber: WeaponCaliber
    fire_rate: int
    effective_distance: int

# class Weapon(WeaponData, Enum):
#     ADAR_2_15 = (
#         constants.ADAR_2_15_CATEGORY,
        
#     )

# class Weapon(WeaponData, Enum):
#     # Assault Carbines

#     ADAR_2_15 = (
#         ItemRarity.COMMON,
#         "ADAR 2-15",
#         WeaponType.ASSAULT_CARBINE,
#         "A cheap but versatile assault carbine.",
#         100,
#         3267,
#         60.5,
#         2.2,
#         84,
#         905,
#         [FireMode.SemiAuto],
#         WeaponCaliber.AMMO_5_56x45MM,
#         800,
#         500,
#     )

#     VSK_94 = (
#         ItemRarity.UNCOMMON,
#         "VSK-94",
#         WeaponType.ASSAULT_CARBINE,
#         "A reliable and versatile assault carbine.",
#         100,
#         2992,
#         54,
#         4.37,
#         62,
#         246,
#         [FireMode.SemiAuto, FireMode.FullAuto],
#         WeaponCaliber.AMMO_9x39MM,
#         700,
#         400,
#     )

#     SR_3M = (
#         ItemRarity.RARE,
#         "SR-3M",
#         WeaponType.ASSAULT_CARBINE,
#         "A very reliable and versatile assault carbine.",
#         100,
#         2593,
#         70,
#         5.02,
#         59,
#         290,
#         [FireMode.SemiAuto, FireMode.FullAuto],
#         WeaponCaliber.AMMO_9x39MM,
#         900,
#         400,
#     )

#     LONE_STAR_TX_15_DML = (
#         ItemRarity.LEGENDARY,
#         "Lone star TX-15 DML",
#         WeaponType.ASSAULT_CARBINE,
#         "A very very reliable and versatile assault carbine.",
#         100,
#         3702,
#         34,
#         1.38,
#         56,
#         922,
#         [FireMode.SemiAuto],
#         WeaponCaliber.AMMO_5_56x45MM,
#         800,
#         500,
#     )

#     RFB = (
#         ItemRarity.MYTHIC,
#         "RFB",
#         WeaponType.ASSAULT_CARBINE,
#         "A very super reliable and versatile assault carbine.",
#         100,
#         3606,
#         50,
#         1.58,
#         136,
#         805,
#         [FireMode.SemiAuto],
#         WeaponCaliber.AMMO_7_62x51MM,
#         700,
#         900,
#     )

#     # Assualt Rifles

#     AK_74 = (
#         ItemRarity.COMMON,
#         "AK-74",
#         WeaponType.ASSAULT_RIFLE,
#         "A cheap but versatile assault rifle.",
#         100,
#         3320,
#         39,
#         1.99,
#         85,
#         906,
#         [FireMode.SemiAuto, FireMode.FullAuto],
#         WeaponCaliber.AMMO_5_45x39MM,
#         650,
#         650,
#     )

#     AKM = (
#         ItemRarity.UNCOMMON,
#         "AKM",
#         WeaponType.ASSAULT_RIFLE,
#         "Classic 7.62x39 thumper—hits harder, kicks harder.",
#         100,
#         3495,
#         36,
#         2.3,
#         109,
#         730,
#         [FireMode.SemiAuto, FireMode.FullAuto],
#         WeaponCaliber.AMMO_7_62x39MM,
#         600,
#         400,
#     )

#     RD_704 = (
#         ItemRarity.RARE,
#         "RD-704",
#         WeaponType.ASSAULT_RIFLE,
#         "High-end 7.62x39 rifle tuned for control and output.",
#         100,
#         3835,
#         62,
#         2.0,
#         104,
#         789,
#         [FireMode.SemiAuto, FireMode.FullAuto],
#         WeaponCaliber.AMMO_7_62x39MM,
#         600,
#         650,
#     )

#     M4A1 = (
#         ItemRarity.LEGENDARY,
#         "Colt M4A1",
#         WeaponType.ASSAULT_RIFLE,
#         "Modular 5.56 rifle—endless build paths.",
#         100,
#         2849,
#         51.5,
#         1.8,
#         84,
#         862,
#         [FireMode.SemiAuto, FireMode.FullAuto],
#         WeaponCaliber.AMMO_5_56x45MM,
#         800,
#         500,
#     )

#     HK_416A5 = (
#         ItemRarity.MYTHIC,
#         "HK 416A5",
#         WeaponType.ASSAULT_RIFLE,
#         "Premium 5.56 platform—fast, clean, expensive.",
#         100,
#         3819,
#         55,
#         1.9,
#         85,
#         804,
#         [FireMode.SemiAuto, FireMode.FullAuto],
#         WeaponCaliber.AMMO_5_56x45MM,
#         850,
#         500,
#     )

#     # Bolt-action rifles

#     VPO_215 = (
#         ItemRarity.COMMON,
#         "VPO-215 Gornostay",
#         WeaponType.BOLT_ACTION,
#         "Budget bolt-action in .366—starter sniper energy.",
#         100,
#         3300,
#         50,
#         1.5,
#         130,
#         865,
#         [FireMode.SingleShot],
#         WeaponCaliber.AMMO_366_TKM,
#         30,
#         1000,
#     )

#     MOSIN_SNIPER = (
#         ItemRarity.UNCOMMON,
#         "Mosin (Sniper)",
#         WeaponType.BOLT_ACTION,
#         "Old-school 7.62x54R bolt gun—cheap, deadly, everywhere.",
#         100,
#         4880,
#         13,
#         1.3,
#         202,
#         988,
#         [FireMode.SingleShot],
#         WeaponCaliber.AMMO_7_62x54R,
#         30,
#         1000,
#     )

#     M700 = (
#         ItemRarity.RARE,
#         "Remington Model 700",
#         WeaponType.BOLT_ACTION,
#         "Reliable .308 bolt-action classic.",
#         100,
#         4060,
#         37,
#         0.8,
#         149,
#         943,
#         [FireMode.SingleShot],
#         WeaponCaliber.AMMO_7_62x51MM,
#         30,
#         1000,
#     )

#     DVL_10 = (
#         ItemRarity.LEGENDARY,
#         "DVL-10",
#         WeaponType.BOLT_ACTION,
#         "Suppressed precision bolt-action built for stealth shots.",
#         100,
#         5068,
#         52,
#         0.45,
#         69,
#         977,
#         [FireMode.SingleShot],
#         WeaponCaliber.AMMO_7_62x51MM,
#         30,
#         1000,
#     )

#     T_5000M = (
#         ItemRarity.MYTHIC,
#         "ORSIS T-5000M",
#         WeaponType.BOLT_ACTION,
#         "Long-range bolt-action focused on accuracy and stability.",
#         100,
#         5900,
#         72,
#         0.7,
#         94,
#         961,
#         [FireMode.SingleShot],
#         WeaponCaliber.AMMO_7_62x51MM,
#         30,
#         1000,
#     )

#     # DMRs

#     SVDS = (
#         ItemRarity.COMMON,
#         "SVDS",
#         WeaponType.DMR,
#         "Has a foldable stock.",
#         100,
#         4386,
#         33.5,
#         1,
#         138,
#         821,
#         [FireMode.SemiAuto],
#         WeaponCaliber.AMMO_7_62x54R,
#         700,
#         900,
#     )

#     M1A = (
#         ItemRarity.UNCOMMON,
#         "M1A",
#         WeaponType.DMR,
#         "Makes loud sounds that scare you.",
#         100,
#         3923,
#         38,
#         1.3,
#         141,
#         779,
#         [FireMode.SemiAuto],
#         WeaponCaliber.AMMO_7_62x51MM,
#         700,
#         700,
#     )

#     SR_25 = (
#         ItemRarity.RARE,
#         "SR-25",
#         WeaponType.DMR,
#         "Test drive part 1 has never felt so good.",
#         100,
#         3860,
#         53,
#         1.6,
#         101,
#         786,
#         [FireMode.SemiAuto],
#         WeaponCaliber.AMMO_7_62x51MM,
#         700,
#         900,
#     )

#     RSASS = (
#         ItemRarity.LEGENDARY,
#         "RSASS",
#         WeaponType.DMR,
#         "Deadly, and fun.",
#         100,
#         4922,
#         38,
#         0.7,
#         84,
#         796,
#         [FireMode.SemiAuto],
#         WeaponCaliber.AMMO_7_62x51MM,
#         700,
#         900,
#     )

#     G28 = (
#         ItemRarity.MYTHIC,
#         "G28",
#         WeaponType.DMR,
#         "This thing claps.",
#         100,
#         5468,
#         42,
#         1.1,
#         74,
#         795,
#         [FireMode.SemiAuto],
#         WeaponCaliber.AMMO_7_62x51MM,
#         700,
#         700,
#     )

#     # Grenade Launchers

#     FN40GL = (
#         ItemRarity.LEGENDARY,
#         "FN40GL Mk2 40mm",
#         WeaponType.GL,
#         "Boom!",
#         100,
#         3000,
#         56.5,
#         24,
#         230,
#         185,
#         [FireMode.SingleShot],
#         WeaponCaliber.AMMO_40MM,
#         30,
#         50,
#     )

#     M32A1 = (
#         ItemRarity.MYTHIC,
#         "Milkor M32A1 MSGL 40mm",
#         WeaponType.GL,
#         "Big boom!",
#         100,
#         5475,
#         23.5,
#         16.5,
#         190,
#         185,
#         [FireMode.SemiAuto],
#         WeaponCaliber.AMMO_40MM,
#         30,
#         70,
#     )

#     # LMGs

#     PKM = (
#         ItemRarity.UNCOMMON,
#         "PKM",
#         WeaponType.LMG,
#         "Factory chad type equipment.",
#         100,
#         8994,
#         0,
#         1.1,
#         99,
#         976,
#         [FireMode.FullAuto, FireMode.SemiAuto],
#         WeaponCaliber.AMMO_7_62x54R,
#         650,
#         750,
#     )

#     RPK_16 = (
#         ItemRarity.RARE,
#         "RPK-16",
#         WeaponType.LMG,
#         "Dorms chad type equipment.",
#         100,
#         3697,
#         35.8,
#         1.7,
#         76,
#         835,
#         [FireMode.FullAuto, FireMode.SemiAuto],
#         WeaponCaliber.AMMO_5_45x39MM,
#         650,
#         650,
#     )

#     M60E4 = (
#         ItemRarity.LEGENDARY,
#         "PKM",
#         WeaponType.LMG,
#         "Theyre in the trees!",
#         100,
#         10073,
#         7,
#         1.2,
#         91,
#         840,
#         [FireMode.FullAuto, FireMode.SemiAuto],
#         WeaponCaliber.AMMO_7_62x51MM,
#         550,
#         800,
#     )

#     # Rocket Launcher

#     RSHG2 = (
#         ItemRarity.MYTHIC,
#         "RShG-2 Rocket Launcher",
#         WeaponType.ROCKET_LAUNCHER,
#         "Overkill?",
#         100,
#         4000,
#         39,
#         24,
#         180,
#         144,
#         [FireMode.SingleShot],
#         WeaponCaliber.AMMO_72_5MM,
#         30,
#         50,
#     )

#     # Shotguns

#     TOZ_106 = (
#         ItemRarity.COMMON,
#         "TOZ-106",
#         WeaponType.SHOTGUN,
#         "Youre better off hitting someone with it",
#         100,
#         2715,
#         73,
#         24,
#         504,
#         438,
#         [FireMode.SingleShot],
#         WeaponCaliber.AMMO_20GAUGE,
#         30,
#         70,
#     )

#     M870 = (
#         ItemRarity.UNCOMMON,
#         "Remington M870",
#         WeaponType.SHOTGUN,
#         "USA USA USA",
#         100,
#         3140,
#         49,
#         18.9,
#         278,
#         437,
#         [FireMode.SingleShot],
#         WeaponCaliber.AMMO_12GAUGE,
#         30,
#         70,
#     )

#     MP_153 = (
#         ItemRarity.RARE,
#         "MP-153",
#         WeaponType.SHOTGUN,
#         "Semi auto shotgun.",
#         100,
#         3620,
#         35,
#         10.3,
#         230,
#         489,
#         [FireMode.SemiAuto],
#         WeaponCaliber.AMMO_12GAUGE,
#         40,
#         70,
#     )

#     SAIGA_12K = (
#         ItemRarity.LEGENDARY,
#         "Saiga-12K",
#         WeaponType.SHOTGUN,
#         "Look for drum mags...",
#         100,
#         3600,
#         55.5,
#         20.6,
#         226,
#         426,
#         [FireMode.SemiAuto],
#         WeaponCaliber.AMMO_12GAUGE,
#         40,
#         70,
#     )

#     AA_12_GEN_1 = (
#         ItemRarity.MYTHIC,
#         "Auto Assault-12 Gen 1",
#         WeaponType.SHOTGUN,
#         "Hallway clearer",
#         100,
#         5090,
#         38,
#         21,
#         172,
#         446,
#         [FireMode.SemiAuto],
#         WeaponCaliber.AMMO_12GAUGE,
#         330,
#         70,
#     )

#     # Submachine Guns

#     MP5 = (
#         ItemRarity.COMMON,
#         "HK MP5",
#         WeaponType.SMG,
#         "Classic SMG",
#         100,
#         2710,
#         68,
#         6.9,
#         43,
#         435,
#         [FireMode.SemiAuto, FireMode.FullAuto],
#         WeaponCaliber.AMMO_9x19MM,
#         800,
#         200,
#     )

#     MP9 = (
#         ItemRarity.UNCOMMON,
#         "B&T MP9",
#         WeaponType.SMG,
#         "Designed and manufactured in Switzerland.",
#         100,
#         1290,
#         84,
#         7.2,
#         47,
#         435,
#         [FireMode.SemiAuto, FireMode.FullAuto],
#         WeaponCaliber.AMMO_9x19MM,
#         900,
#         200,
#     )

#     SR_2M = (
#         ItemRarity.RARE,
#         "SR-2M Veresk",
#         WeaponType.SMG,
#         "Classic SMG",
#         100,
#         1773,
#         85,
#         7.8,
#         44,
#         467,
#         [FireMode.SemiAuto, FireMode.FullAuto],
#         WeaponCaliber.AMMO_9x21MM,
#         950,
#         200,
#     )

#     VECTOR_45 = (
#         ItemRarity.LEGENDARY,
#         "KRISS Vector Gen.2 .45 ACP",
#         WeaponType.SMG,
#         "Fast pews.",
#         100,
#         2646,
#         73,
#         6.9,
#         44,
#         375,
#         [FireMode.SemiAuto, FireMode.FullAuto],
#         WeaponCaliber.AMMO_45_ACP,
#         1100,
#         200,
#     )

#     MP7 = (
#         ItemRarity.MYTHIC,
#         "HK MP7A1",
#         WeaponType.SMG,
#         "Rips people up.",
#         100,
#         2270,
#         69,
#         8.3,
#         42,
#         701,
#         [FireMode.SemiAuto, FireMode.FullAuto],
#         WeaponCaliber.AMMO_4_6x30MM,
#         950,
#         200,
#     )

#     # Sidearms

#     BLICKY = (
#         ItemRarity.COMMON,
#         "20x1mm toy gun",
#         WeaponType.PISTOL,
#         "Cap gun for fun.",
#         100,
#         90,
#         100,
#         13.4,
#         0,
#         20,
#         [FireMode.SemiAuto],
#         WeaponCaliber.AMMO_20x1MM,
#         30,
#         50,
#     )

#     GLOCK_18C = (
#         ItemRarity.RARE,
#         "Glock 18C",
#         WeaponType.PISTOL,
#         "Switched.",
#         100,
#         842,
#         87,
#         12,
#         288,
#         369,
#         [FireMode.SemiAuto, FireMode.FullAuto],
#         WeaponCaliber.AMMO_9x19MM,
#         1200,
#         50,
#     )

#     M1911A1 = (
#         ItemRarity.COMMON,
#         "Colt M1911A1",
#         WeaponType.PISTOL,
#         "Won two world wars.",
#         100,
#         1214,
#         78,
#         12,
#         437,
#         336,
#         [FireMode.SemiAuto],
#         WeaponCaliber.AMMO_45_ACP,
#         30,
#         50,
#     )
