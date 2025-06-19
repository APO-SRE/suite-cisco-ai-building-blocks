from enum import Enum


class ModelsConfigOrigin(str, Enum):
    CONFIG_ORIGIN_CLOUD = "CONFIG_ORIGIN_CLOUD"
    CONFIG_ORIGIN_DEVICE = "CONFIG_ORIGIN_DEVICE"

    def __str__(self) -> str:
        return str(self.value)
