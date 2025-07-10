from enum import Enum


class ModelsRouteTag(str, Enum):
    TAG_AMBER = "TAG_AMBER"
    TAG_BLACK = "TAG_BLACK"
    TAG_BLUE = "TAG_BLUE"
    TAG_GREEN = "TAG_GREEN"
    TAG_PURPLE = "TAG_PURPLE"
    TAG_RED = "TAG_RED"
    TAG_YELLOW = "TAG_YELLOW"

    def __str__(self) -> str:
        return str(self.value)
