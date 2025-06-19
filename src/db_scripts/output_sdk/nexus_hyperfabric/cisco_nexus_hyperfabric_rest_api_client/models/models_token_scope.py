from enum import Enum


class ModelsTokenScope(str, Enum):
    TOKEN_SCOPE_ADMIN = "TOKEN_SCOPE_ADMIN"
    TOKEN_SCOPE_READ_ONLY = "TOKEN_SCOPE_READ_ONLY"
    TOKEN_SCOPE_READ_WRITE = "TOKEN_SCOPE_READ_WRITE"

    def __str__(self) -> str:
        return str(self.value)
