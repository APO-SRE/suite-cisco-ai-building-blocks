from enum import Enum


class AnyPATCHItemType0Op(str, Enum):
    ADD = "add"
    REPLACE = "replace"
    TEST = "test"

    def __str__(self) -> str:
        return str(self.value)
