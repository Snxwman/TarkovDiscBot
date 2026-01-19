from dataclasses import dataclass


@dataclass
class GridSize:
    height: int
    width: int


class Inventory: ...


class ItemInventory: ...


class PlayerInventory:
    def __init__(self) -> None:
        self.headset: ItemInventory | None = None
        self.head: ItemInventory | None = None
        self.face: ItemInventory | None = None
        self.eyes: ItemInventory | None = None
        self.armor: ItemInventory | None = None
        self.primary_weapon: ItemInventory | None = None
        self.secondary_weapon: ItemInventory | None = None
        self.side_arm: ItemInventory | None = None
        self.rig: ItemInventory | None = None
        self.pockets: ItemInventory | None = None
        self.backpack: ItemInventory | None = None
        self.secure_container: ItemInventory | None = None


class ContainerInventory: ...


class Stash: ...
