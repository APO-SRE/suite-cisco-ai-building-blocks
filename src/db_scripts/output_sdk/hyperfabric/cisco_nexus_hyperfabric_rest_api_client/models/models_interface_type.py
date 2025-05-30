from enum import Enum


class ModelsInterfaceType(str, Enum):
    LOOPBACK_INTERFACE = "LOOPBACK_INTERFACE"
    NETWORK_PORT_INTERFACE = "NETWORK_PORT_INTERFACE"
    PORT_CHANNEL_INTERFACE = "PORT_CHANNEL_INTERFACE"
    SUB_PORT_INTERFACE = "SUB_PORT_INTERFACE"
    VLAN_INTERFACE = "VLAN_INTERFACE"

    def __str__(self) -> str:
        return str(self.value)
