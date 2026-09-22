from dataclasses import dataclass

@dataclass(frozen=True)
class DeploymentHealth:
    ready: bool
    services: int
    errors: tuple[str,...]

def inspect(deployment) -> DeploymentHealth:
    errors=tuple(__import__("edgemesh.manifest",fromlist=["validate"]).validate(deployment))
    return DeploymentHealth(not errors, len(deployment.services), errors)
