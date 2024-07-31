from enum import Enum


class Priority(Enum):
    HIGH = 1
    MEDIUM = 2
    LOW = 3


class Status(Enum):
    COMPLETED = 1
    NOT_COMPLETED = 2
    IN_PROGRESS = 3

