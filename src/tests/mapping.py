from orchestrator.domain.entities.machine import Machine
from orchestrator.domain.entities.order_command import OrderCommand

from orchestrator.domain.services.command_mapping_service import (
    CommandMappingService,
)


machines = [
    Machine(
        machine_id=2,
        station_id=1,
        station_arrange=1,
        machine_arrange=2,
        machine_name="Sauce Machine 2",
    )
]

command = OrderCommand(
    id=501,
    code="1_2",
    level=3,
)

mapper = CommandMappingService()

assignment = mapper.assign_command(
    tray_no=15,
    command=command,
    machines=machines,
)

print(assignment)