"""Camera port contract."""

from abc import ABC, abstractmethod


class CameraPort(ABC):
    @abstractmethod
    def scan_qr(self, conveyor_id: int) -> int:
        pass