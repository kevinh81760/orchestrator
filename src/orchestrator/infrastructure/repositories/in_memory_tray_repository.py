"""In-memory tray repository."""

from orchestrator.application.ports.tray_repository import TrayRepository
from orchestrator.domain.entities.machine_assignment import MachineAssignment


class InMemoryTrayRepository(TrayRepository):
    def __init__(self):
        self.assignments: dict[int, list[MachineAssignment]] = {}

    def save_assignments(self, assignments: list[MachineAssignment]) -> None:
        if not assignments:
            return

        tray_no = assignments[0].tray_no
        self.assignments[tray_no] = assignments

    def get_assignments(self, tray_no: int) -> list[MachineAssignment]:
        return self.assignments.get(tray_no, [])

    def clear_tray(self, tray_no: int) -> None:
        self.assignments.pop(tray_no, None)