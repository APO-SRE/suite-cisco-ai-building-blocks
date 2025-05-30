from enum import Enum


class ConfigLatchState(str, Enum):
    LATCH_STATE_LATCH = "LATCH_STATE_LATCH"
    LATCH_STATE_UNLATCH = "LATCH_STATE_UNLATCH"

    def __str__(self) -> str:
        return str(self.value)
