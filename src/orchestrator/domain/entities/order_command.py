"""Order command entity."""

from dataclasses import dataclass


@dataclass(frozen=True)
class OrderCommand:
    id: int
    code: str
    level: int | float