import uuid
from dataclasses import dataclass, field


@dataclass
class Room:
    """
    Represent an individual room.
    """
    name: str
    capabilities: set[str] = field(default_factory=set) 
    id: str = field(default_factory=lambda: str(uuid.uuid4()))

