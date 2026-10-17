import uuid
from dataclasses import dataclass, field

from .subject import Subject


@dataclass
class Course:
    """
    Represent an individual course related to a subject.
    """
    name: str
    subject: Subject
    id: str = field(default_factory=lambda: str(uuid.uuid4()))

    @property
    def course_number(self) -> str:
        return split(self.name)


def split(x):
    name, number = x.split()
    ans = name[:3] + number
    return ans.upper()

