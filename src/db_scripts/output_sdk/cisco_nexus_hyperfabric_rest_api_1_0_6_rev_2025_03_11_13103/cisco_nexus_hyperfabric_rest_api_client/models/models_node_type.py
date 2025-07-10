from enum import Enum


class ModelsNodeType(str, Enum):
    NODE_BLUEPRINT = "NODE_BLUEPRINT"
    NODE_SWITCH = "NODE_SWITCH"

    def __str__(self) -> str:
        return str(self.value)
