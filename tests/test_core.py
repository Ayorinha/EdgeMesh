from edgemesh.core import Service

def test_service_validation(): Service("api", "python:3.12", 8000, 2).validate()

def test_invalid_port():
    try: Service("api", "python:3.12", 0).validate()
    except ValueError: pass
    else: raise AssertionError("invalid port accepted")
