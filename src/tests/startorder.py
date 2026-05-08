"""Demo script for starting a tray."""

from orchestrator.application.use_cases.start_tray_use_case import StartTrayUseCase
from orchestrator.domain.services.command_mapping_service import CommandMappingService
from orchestrator.infrastructure.camera.fake_camera import FakeCamera
from orchestrator.infrastructure.order_gateway.fake_order_gateway import FakeOrderGateway
from orchestrator.infrastructure.repositories.in_memory_machine_repository import (
    InMemoryMachineRepository,
)
from orchestrator.infrastructure.repositories.in_memory_tray_repository import (
    InMemoryTrayRepository,
)


def main() -> None:
    camera = FakeCamera()
    gateway = FakeOrderGateway()
    machine_repo = InMemoryMachineRepository()
    tray_repo = InMemoryTrayRepository()
    mapper = CommandMappingService()

    use_case = StartTrayUseCase(
        camera=camera,
        order_gateway=gateway,
        machine_repository=machine_repo,
        tray_repository=tray_repo,
        command_mapper=mapper,
    )

    result = use_case.execute(conveyor_id=1)
    print(result)


if __name__ == "__main__":
    main()