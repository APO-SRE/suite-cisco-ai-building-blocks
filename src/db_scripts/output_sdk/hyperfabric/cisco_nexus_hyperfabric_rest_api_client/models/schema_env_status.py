from enum import Enum


class SchemaEnvStatus(str, Enum):
    NOT_OK = "NOT_OK"
    NOT_PRESENT = "NOT_PRESENT"
    OK = "OK"
    WARNING = "WARNING"

    def __str__(self) -> str:
        return str(self.value)
