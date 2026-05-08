"""Machine repository contract."""

from abc import ABC, abstractmethod

from orchestrator.domain.entities.machine import Machine


class MachineRepository(ABC):
    @abstractmethod
    def list_machines(self) -> list[Machine]:
        pass