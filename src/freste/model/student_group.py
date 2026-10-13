from dataclasses import dataclass, field
import uuid

@dataclass
class StudentGroup:

    """
    Represent a group of students scheduled together.
    """
    level: str 
    section: str
    id: str = field(default_factory=lambda: str(uuid.uuid4()))



