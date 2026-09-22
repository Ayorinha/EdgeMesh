from edgemesh.readiness import ready
def test_readiness_rejects_impossible_replica_counts():
    assert not ready(-1, 0, "1", "1Gi")
    assert not ready(2, 3, "1", "1Gi")