from enum import Enum


class BrSecureCopyAuthentication(str, Enum):
    PASSWORD = "password"
    PUBLICKEY = "publickey"

    def __str__(self) -> str:
        return str(self.value)
