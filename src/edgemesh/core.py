from __future__ import annotations
from dataclasses import dataclass
@dataclass(frozen=True, slots=True)
class Service:
    name: str; image: str; port: int; replicas: int = 1
    def validate(self) -> None:
        if not self.name.strip() or not self.image.strip(): raise ValueError("name and image are required")
        if not 1 <= self.port <= 65535: raise ValueError("invalid port")
        if self.replicas < 1: raise ValueError("replicas must be positive")
