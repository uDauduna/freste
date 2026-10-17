from dataclasses import dataclass, field
import uuid

@dataclass
class Subject:

    """
    Represent a subject.
    """
    name: str
    id: str = field(default_factory=lambda: str(uuid.uuid4()))


