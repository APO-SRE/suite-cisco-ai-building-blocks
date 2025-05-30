from enum import Enum


class ModelsMatchType(str, Enum):
    MATCH_EQ = "MATCH_EQ"
    MATCH_GE = "MATCH_GE"
    MATCH_LE = "MATCH_LE"

    def __str__(self) -> str:
        return str(self.value)
