from enum import Enum


class BrSecureCopyProtocol(str, Enum):
    SCP = "scp"
    SFTP = "sftp"

    def __str__(self) -> str:
        return str(self.value)
