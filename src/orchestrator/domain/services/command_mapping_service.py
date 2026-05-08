"""Maps external commands to domain commands."""


from orchestrator.domain.entities.machine import Machine
from orchestrator.domain.entities.order_command import OrderCommand
from orchestrator.domain.entities.machine_assignment import MachineAssignment


class CommandMappingService:
    def assign_command(self, tray_no: int, command: OrderCommand, machines: list[Machine]) -> MachineAssignment:
        for machine in machines:
            if machine.command_code == command.code:
                if getattr(machine, "is_disabled", False):
                    raise ValueError(f"Machine {machine.machine_id} is disabled")

                return MachineAssignment(
                    tray_no=tray_no,
                    machine_id=machine.machine_id,
                    command_id=command.id,
                    command_code=command.code,
                    assigned_level=command.level,
                )

        raise ValueError(f"No machine found for command code {command.code}")