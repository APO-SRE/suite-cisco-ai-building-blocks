from enum import Enum


class LDAPProviderV4AaaPUTSslStrictnessLevel(str, Enum):
    PERMISSIVE = "Permissive"
    STRICT = "Strict"

    def __str__(self) -> str:
        return str(self.value)
