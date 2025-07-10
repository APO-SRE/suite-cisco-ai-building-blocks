from enum import Enum


class ModelsConfigType(str, Enum):
    CONFIG_TYPE_DHCP = "CONFIG_TYPE_DHCP"
    CONFIG_TYPE_STATIC = "CONFIG_TYPE_STATIC"

    def __str__(self) -> str:
        return str(self.value)
