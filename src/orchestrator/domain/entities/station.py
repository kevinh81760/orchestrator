"""Station entity."""

from dataclasses import dataclass


@dataclass
class Station:
    station_id: int
    station_arrange: int
    station_name: str
    station_min_level: int
    station_max_level: int
    station_prefix: str | None = None
    station_suffix: str | None = None
    station_has_multi_machine: bool = False

    def allows_level(self, level: int | float) -> bool:
        return self.station_min_level <= level <= self.station_max_level