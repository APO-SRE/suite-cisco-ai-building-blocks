from enum import Enum


class ModelsFabricType(str, Enum):
    BLUEPRINT = "BLUEPRINT"
    INVENTORY = "INVENTORY"
    PARKINGLOT = "PARKINGLOT"

    def __str__(self) -> str:
        return str(self.value)
