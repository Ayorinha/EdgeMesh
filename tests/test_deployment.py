from edgemesh.deployment import DeploymentSpec,validate

def test_deployment_requires_resources():
    validate(DeploymentSpec("api",2,"500m","512Mi"))
