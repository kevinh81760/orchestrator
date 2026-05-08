"""Order gateway contract."""

from abc import ABC, abstractmethod

from orchestrator.domain.entities.order_command import OrderCommand


class OrderGateway(ABC):
    @abstractmethod
    def get_order(self, tray_no: int) -> list[OrderCommand]:
        pass

    @abstractmethod
    def complete_order(self, tray_no: int) -> None:
        pass

    @abstractmethod
    def mark_failed_order(self, tray_no: int, failed_command_ids: list[int]) -> None:
        pass