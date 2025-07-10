from enum import Enum


class ModelsFabricTopology(str, Enum):
    MESH = "MESH"
    SPINE_LEAF = "SPINE_LEAF"

    def __str__(self) -> str:
        return str(self.value)
