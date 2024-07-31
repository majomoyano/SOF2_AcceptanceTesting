from datetime import datetime
from utils.custom_ex import InvalidPriority, InvalidStatus
from utils.enums import Status, Priority
from utils.validator import Validator

class Task():
    def __init__(self, description, due_date ,priority="LOW"):
        self.description = description
        self.due_date = datetime.strptime(due_date, "%d-%m-%Y").date().strftime("%d-%m-%Y")
        self.status = Status.NOT_COMPLETED
        try:
            self.priority = Priority[priority]
        except KeyError:
            raise InvalidPriority

    @property
    def description(self):
        return self._description
    
    @description.setter
    def description(self, description):
        if not description:
            raise ValueError("Description cannot be empty")
        self._description = description
    
    @property
    def due_date(self):
        return self._due_date
    
    @due_date.setter
    def due_date(self, due_date):
        if not due_date:
            raise ValueError("Due date cannot be empty")
        try:
            datetime.strptime(due_date, "%d-%m-%Y")
        except ValueError:
            raise ValueError("Invalid date format. Please use DD-MM-YYYY")
        self._due_date = due_date
    
    def __str__(self):
        return f"Task:\nDescription:{self.description} Priority: {self.priority.name} Status: {self.status.name} Due to: {self.due_date} "

    def __hash__(self):
        return hash((self.description, self.due_date, self.priority, self.status))

    def __eq__(self, other):
        if not isinstance(other, Task):
            return NotImplemented
        return self.description == other.description and self.due_date == other.due_date and self.priority == other.priority and self.status == other.status
