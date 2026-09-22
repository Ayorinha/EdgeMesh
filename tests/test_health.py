from edgemesh.manifest import Deployment, Service
from edgemesh.health import inspect

def test_deployment_health():
    result=inspect(Deployment([Service("api","image:v1",2)]))
    assert result.ready and result.services==1

def test_invalid_deployment():
    result=inspect(Deployment([Service("api","",1)]))
    assert not result.ready
