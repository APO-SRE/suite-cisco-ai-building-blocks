from enum import Enum


class ModelsNodeRole(str, Enum):
    LEAF = "LEAF"
    SERVER = "SERVER"
    SPINE = "SPINE"

    def __str__(self) -> str:
        return str(self.value)
