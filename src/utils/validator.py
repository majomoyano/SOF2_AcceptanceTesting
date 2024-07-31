from utils.enums import Status, Priority
from datetime import datetime
from utils.custom_ex import InvalidDate, InvalidPriority, InvalidStatus, InvalidTask

class Validator():
    def __init__(self):
        pass

    def validate_date(self, date):
        try:
            datetime.strptime(date, "%d-%m-%Y")
        except ValueError:
            raise InvalidDate
        return date
    
    def validate_priority(self, priority):
        try:
            priority = Priority[priority]
        except KeyError:
            raise InvalidPriority
        return priority
    
    def validate_status(self, status):
        try:
            status = Status[status]
        except KeyError:
            raise InvalidStatus
        return status
    
    def validate_description(self, description, list_of_tasks):
        if not description:
            raise InvalidTask
        if description not in list_of_tasks:
            raise InvalidTask
        return description
    