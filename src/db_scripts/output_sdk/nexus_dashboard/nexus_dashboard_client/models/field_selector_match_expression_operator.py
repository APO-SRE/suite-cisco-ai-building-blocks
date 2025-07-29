from enum import Enum


class FieldSelectorMatchExpressionOperator(str, Enum):
    AND = "AND"
    CUSTOM = "CUSTOM"
    EQ = "EQ"
    FALSE = "FALSE"
    GT = "GT"
    GTE = "GTE"
    ISSET = "ISSET"
    LT = "LT"
    LTE = "LTE"
    NE = "NE"
    NOT = "NOT"
    OR = "OR"
    REGEX = "REGEX"
    TRUE = "TRUE"

    def __str__(self) -> str:
        return str(self.value)
