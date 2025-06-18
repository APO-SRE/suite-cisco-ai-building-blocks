from enum import Enum


class AuthGetUsersRoles(str, Enum):
    ADMIN = "ADMIN"
    READ_ONLY = "READ_ONLY"
    READ_WRITE = "READ_WRITE"

    def __str__(self) -> str:
        return str(self.value)
