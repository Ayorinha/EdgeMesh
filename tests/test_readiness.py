from edgemesh.readiness import ready
def test_readiness_requires_all_replicas():
    assert ready(2,2,"500m","512Mi")
    assert not ready(2,1,"500m","512Mi")