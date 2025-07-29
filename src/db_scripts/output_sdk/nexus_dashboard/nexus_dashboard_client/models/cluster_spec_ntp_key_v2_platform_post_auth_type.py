from enum import Enum


class ClusterSpecNTPKeyV2PlatformPOSTAuthType(str, Enum):
    AES128CMAC = "AES128CMAC"
    MD5 = "MD5"
    SHA1 = "SHA1"

    def __str__(self) -> str:
        return str(self.value)
