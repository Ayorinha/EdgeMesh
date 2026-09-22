from edgemesh.core import Service

def test_service():
 Service("api","python:3.12",8000).validate()
