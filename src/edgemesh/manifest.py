from dataclasses import dataclass
@dataclass(frozen=True)
class Service: name:str; image:str; replicas:int=1
@dataclass(frozen=True)
class Deployment: services:list[Service]
def validate(d):
 e=[]; names=set()
 for s in d.services:
  if s.name in names:e.append(f'duplicate service: {s.name}')
  names.add(s.name)
  if s.replicas<1:e.append(f'invalid replicas: {s.name}')
  if not s.image:e.append(f'missing image: {s.name}')
 return e
