from enum import Enum


class LabelSelectorMatchExpressionOperator(str, Enum):
    DOESNOTEXIST = "DoesNotExist"
    EXISTS = "Exists"
    IN = "In"
    NOTIN = "NotIn"

    def __str__(self) -> str:
        return str(self.value)
