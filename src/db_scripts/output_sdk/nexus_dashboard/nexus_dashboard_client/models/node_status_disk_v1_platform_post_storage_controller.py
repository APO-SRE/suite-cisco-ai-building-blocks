from enum import Enum


class NodeStatusDiskV1PlatformPOSTStorageController(str, Enum):
    IDE = "IDE"
    MMC = "MMC"
    NVME = "NVMe"
    SCSI = "SCSI"
    UNKNOWN = "Unknown"
    VIRTIO = "virtio"

    def __str__(self) -> str:
        return str(self.value)
