"""Start tray use case."""

from orchestrator.domain.services.command_mapping_service import (
    CommandMappingService,
)


class StartTrayUseCase:
    def __init__(
        self,
        camera,
        order_gateway,
        machine_repository,
        tray_repository,
        command_mapper: CommandMappingService,
    ):
        self.camera = camera
        self.order_gateway = order_gateway
        self.machine_repository = machine_repository
        self.tray_repository = tray_repository
        self.command_mapper = command_mapper

    def execute(self, conveyor_id: int):

        # 1. Scan tray QR from camera
        tray_no = self.camera.scan_qr(conveyor_id)

        print(f"Scanned tray: {tray_no}")

        # 2. Ask backend/KDS for order commands
        commands = self.order_gateway.get_order(tray_no)

        print(f"Commands: {commands}")

        # 3. Load available machines
        machines = self.machine_repository.list_machines()

        print(f"Machines: {machines}")

        assignments = []

        # 4. Map commands to machines
        for command in commands:

            assignment = self.command_mapper.assign_command(
                tray_no=tray_no,
                command=command,
                machines=machines,
            )

            assignments.append(assignment)

        # 5. Save assignments
        self.tray_repository.save_assignments(assignments)

        print(f"Assignments saved")

        # 6. Return final assignments
        return assignments