from enum import Enum


class HTTPServerOptionsV4AaaPUTMinVersion(str, Enum):
    TLS12 = "TLS12"
    TLS13 = "TLS13"

    def __str__(self) -> str:
        return str(self.value)
