from dataclasses import dataclass, field
import uuid

@dataclass
class Teacher:
    """
    Represent a group of students scheduled together.
    """
    name: str 
    qualified_course_ids: set[str]=field(default_factory=set)
    id: str = field(default_factory=lambda: str(uuid.uuid4()))

