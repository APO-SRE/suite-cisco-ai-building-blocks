from enum import Enum


class AnyPATCHItemType1Op(str, Enum):
    REMOVE = "remove"

    def __str__(self) -> str:
        return str(self.value)
