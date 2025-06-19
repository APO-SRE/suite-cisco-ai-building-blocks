from enum import Enum


class ModelsCandidateType(str, Enum):
    CANDIDATE_CONFIGS = "CANDIDATE_CONFIGS"
    CANDIDATE_DOWNLOADS = "CANDIDATE_DOWNLOADS"
    CANDIDATE_REBOOTS = "CANDIDATE_REBOOTS"

    def __str__(self) -> str:
        return str(self.value)
