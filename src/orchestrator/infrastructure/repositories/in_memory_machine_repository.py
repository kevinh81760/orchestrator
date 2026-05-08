"""In-memory machine repository."""

from orchestrator.application.ports.machine_repository import MachineRepository
from orchestrator.domain.entities.machine import Machine


class InMemoryMachineRepository(MachineRepository):
    def list_machines(self) -> list[Machine]:
        return [
            Machine(1, 1, 1, 1, "Machine 1"),
            Machine(2, 1, 1, 2, "Machine 2"),
            Machine(3, 1, 1, 3, "Machine 3"),
        ]