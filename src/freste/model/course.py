from dataclasses import dataclass, field
import uuid

from .subject import Subject

@dataclass
class Course:

    """
    Represent an individual course related to a subject.
    """
    name: str
    subject: Subject
    id: str = field(default_factory=lambda: str(uuid.uuid4()))


