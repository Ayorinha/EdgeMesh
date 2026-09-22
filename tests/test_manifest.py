from edgemesh.manifest import *
def test_valid(): assert validate(Deployment([Service('api','python:3.12')]))==[]
def test_invalid(): assert validate(Deployment([Service('api','',0)]))==['invalid replicas: api','missing image: api']
