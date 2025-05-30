from enum import Enum


class ModelsRouteOriginType(str, Enum):
    ROUTE_ORIGIN_EBGP = "ROUTE_ORIGIN_EBGP"
    ROUTE_ORIGIN_IBGP = "ROUTE_ORIGIN_IBGP"

    def __str__(self) -> str:
        return str(self.value)
