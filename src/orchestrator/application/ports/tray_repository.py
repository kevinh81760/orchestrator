"""Tray repository contract."""

from abc import ABC, abstractmethod

from orchestrator.domain.entities.machine_assignment import MachineAssignment


class TrayRepository(ABC):
    @abstractmethod
    def save_assignments(self, assignments: list[MachineAssignment]) -> None:
        pass

    @abstractmethod
    def get_assignments(self, tray_no: int) -> list[MachineAssignment]:
        pass

    @abstractmethod
    def clear_tray(self, tray_no: int) -> None:
        pass