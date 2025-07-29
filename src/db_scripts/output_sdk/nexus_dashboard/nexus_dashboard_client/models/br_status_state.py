from enum import Enum


class BrStatusState(str, Enum):
    COMPLETE = "complete"
    DOWNLOADING = "downloading"
    ERROR = "error"
    IDLE = "idle"
    PROCESSING = "processing"
    READY = "ready"
    VALIDATIONERROR = "validationError"

    def __str__(self) -> str:
        return str(self.value)
