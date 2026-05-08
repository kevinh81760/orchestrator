"""Tray entity."""

from dataclasses import dataclass


@dataclass
class Tray:
    tray_no: int
    order_id: int
    client_id: int