"""Fake order gateway adapter."""

from orchestrator.application.ports.order_gateway import OrderGateway
from orchestrator.domain.entities.order_command import OrderCommand


class FakeOrderGateway(OrderGateway):
    def get_order(self, tray_no: int) -> list[OrderCommand]:
        return [
            OrderCommand(id=501, code="1_1", level=2),
            OrderCommand(id=502, code="1_3", level=1),
        ]

    def complete_order(self, tray_no: int) -> None:
        print(f"Completed tray {tray_no}")

    def mark_failed_order(self, tray_no: int, failed_command_ids: list[int]) -> None:
        print(f"Failed tray {tray_no}, commands={failed_command_ids}")