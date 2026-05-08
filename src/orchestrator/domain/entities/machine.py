"""Machine entity."""

from dataclasses import dataclass


@dataclass
class Machine:
    machine_id: int
    station_id: int
    station_arrange: int
    machine_arrange: int
    machine_name: str

    @property
    def command_code(self) -> str:
        return f"{self.station_arrange}_{self.machine_arrange}"