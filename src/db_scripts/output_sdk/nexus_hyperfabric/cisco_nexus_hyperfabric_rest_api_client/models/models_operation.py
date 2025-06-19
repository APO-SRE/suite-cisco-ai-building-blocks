from enum import Enum


class ModelsOperation(str, Enum):
    BIND = "BIND"
    COMMENT = "COMMENT"
    COMMIT = "COMMIT"
    CREATE = "CREATE"
    DELETE = "DELETE"
    DISABLE = "DISABLE"
    ENABLE = "ENABLE"
    LOGIN = "LOGIN"
    LOGOUT = "LOGOUT"
    REVERT = "REVERT"
    UNBIND = "UNBIND"
    UPDATE = "UPDATE"

    def __str__(self) -> str:
        return str(self.value)
