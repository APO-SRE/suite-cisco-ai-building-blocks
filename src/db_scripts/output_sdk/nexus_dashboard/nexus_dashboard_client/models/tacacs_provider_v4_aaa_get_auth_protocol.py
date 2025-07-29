from enum import Enum


class TACACSProviderV4AaaGETAuthProtocol(str, Enum):
    CHAP = "CHAP"
    MSCHAP = "MSCHAP"
    PAP = "PAP"

    def __str__(self) -> str:
        return str(self.value)
