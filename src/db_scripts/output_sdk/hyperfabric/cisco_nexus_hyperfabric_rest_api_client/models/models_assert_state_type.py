from enum import Enum


class ModelsAssertStateType(str, Enum):
    ASSERT_STATE_FALSE = "ASSERT_STATE_FALSE"
    ASSERT_STATE_TRUE = "ASSERT_STATE_TRUE"
    ASSERT_STATE_UNKNOWN = "ASSERT_STATE_UNKNOWN"

    def __str__(self) -> str:
        return str(self.value)
