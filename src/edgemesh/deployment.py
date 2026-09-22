"""Deployment invariants for AI workloads."""
from dataclasses import dataclass

@dataclass(frozen=True)
class DeploymentSpec:
    name: str
    replicas: int
    cpu_limit: str
    memory_limit: str

def validate(spec: DeploymentSpec) -> None:
    if not spec.name.strip() or spec.replicas < 1:
        raise ValueError("name is required and replicas must be positive")
    if not spec.cpu_limit.strip() or not spec.memory_limit.strip():
        raise ValueError("resource limits are required")
