from enum import Enum


class SiteGroupSelectorSitesV4SitemanagementPUTSelectorSiteType(str, Enum):
    ALL = "All"
    ANY = "Any"

    def __str__(self) -> str:
        return str(self.value)
