"""Machine assignment entity."""

from dataclasses import dataclass


@dataclass
class MachineAssignment:
    tray_no: int
    machine_id: int
    command_id: int
    command_code: str
    assigned_level: int | float