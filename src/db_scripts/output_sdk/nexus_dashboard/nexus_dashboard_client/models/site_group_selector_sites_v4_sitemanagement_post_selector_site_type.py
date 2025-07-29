from enum import Enum


class SiteGroupSelectorSitesV4SitemanagementPOSTSelectorSiteType(str, Enum):
    ALL = "All"
    ANY = "Any"

    def __str__(self) -> str:
        return str(self.value)
