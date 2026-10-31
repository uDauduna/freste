from enum import Enum
from dataclasses import dataclass, field
from datetime import time, datetime
import uuid

class Day(Enum):
    MONDAY = "Monday"
    TUESDAY = "Tuesday"
    WEDNESDAY = "Wednesday"
    THURSDAY = "Thursday"
    FRIDAY = "Friday"

@dataclass
class Period:
    day: Day
    start_time: time
    end_time: time
    id: str = field(default_factory=lambda: str(uuid.uuid4()))

    @property
    def duration(self):
        diff = datetime.combine(datetime.today(), self.end_time) - datetime.combine(datetime.today(), self.end_time)
        return diff

    def __post__init__(self):
        if self.end_time <= self.start_time:
            raise ValueError("End time must be later than start time")