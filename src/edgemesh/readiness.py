"""Deployment readiness gates."""
def ready(replicas: int, healthy: int, cpu_limit: str, memory_limit: str) -> bool:
    if replicas < 1 or healthy < 0 or healthy > replicas: return False
    return healthy == replicas and bool(cpu_limit.strip()) and bool(memory_limit.strip())