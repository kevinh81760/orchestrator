"""Fake camera adapter."""

from orchestrator.application.ports.camera_port import CameraPort


class FakeCamera(CameraPort):
    def scan_qr(self, conveyor_id: int) -> int:
        return 15