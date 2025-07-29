from enum import Enum


class AnyPATCHItemType2Op(str, Enum):
    COPY = "copy"
    MOVE = "move"

    def __str__(self) -> str:
        return str(self.value)
