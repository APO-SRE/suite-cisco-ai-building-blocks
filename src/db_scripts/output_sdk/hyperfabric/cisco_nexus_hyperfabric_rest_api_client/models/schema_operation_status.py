from enum import Enum


class SchemaOperationStatus(str, Enum):
    DOWN = "DOWN"
    UP = "UP"

    def __str__(self) -> str:
        return str(self.value)
