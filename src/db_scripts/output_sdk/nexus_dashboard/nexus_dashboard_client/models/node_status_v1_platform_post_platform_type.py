from enum import Enum


class NodeStatusV1PlatformPOSTPlatformType(str, Enum):
    AWS = "Aws"
    AZURE = "Azure"
    KVM = "Kvm"
    OVA = "Ova"
    PHYSICAL = "Physical"
    RHELBAREMETAL = "RhelBareMetal"
    RHELVIRTUAL = "RhelVirtual"
    UNKNOWN = "Unknown"

    def __str__(self) -> str:
        return str(self.value)
