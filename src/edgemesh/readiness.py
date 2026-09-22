"""Deployment readiness gates."""
def ready(replicas: int, healthy: int, cpu_limit: str, memory_limit: str) -> bool:
    return replicas > 0 and healthy == replicas and bool(cpu_limit.strip()) and bool(memory_limit.strip())