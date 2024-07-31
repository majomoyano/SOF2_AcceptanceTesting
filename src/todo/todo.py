from datetime import datetime
from utils.enums import Status
from utils.validator import Validator

class TodoList():
    def __init__(self):
        self.tasks = []
        self.validator = Validator()

    def add_task(self, task):
        self.tasks.append(task)

    def list_tasks(self):
        for task in self.tasks:
            print(task)

    def mark_task_completed(self, description):
        self.validator.validate_description(description)
        for task in self.tasks:
            if task.description == description:
                task.status = Status.COMPLETED
                break


    def mark_task_in_progress(self, description):
        self.validator.validate_description(description)
        for task in self.tasks:
            if task.description == description:
                task.status = Status.IN_PROGRESS
                break

    def mark_task_incomplete(self, description):
        self.validator.validate_description(description)
        for task in self.tasks:
            if task.description == description:
                task.status = Status.NOT_COMPLETED
                break

    def get_tasks_by_date_range(self, start_date, end_date):
        self.validator.validate_date(start_date)
        self.validator.validate_date(end_date)

        by_date_range = []
        start_date = datetime.strptime(start_date, "%d-%m-%Y").date().strftime("%d-%m-%Y")
        end_date = datetime.strptime(end_date, "%d-%m-%Y").date().strftime("%d-%m-%Y")
        for task in self.tasks:
            if task.due_date >= start_date and task.due_date <= end_date:
                print(task)
                by_date_range.append(task)
        return by_date_range

    def get_tasks_by_priority(self, priority):
        self.validator.validate_priority(priority)
        by_priority = []
        for task in self.tasks:
            if task.priority.name == priority:
                print(task)
                by_priority.append(task)
        return by_priority

    def get_tasks_by_status(self, status):
        self.validator.validate_status(status)
        by_status = []
        for task in self.tasks:
            if task.status.name == status:
                print(task)
                by_status.append(task)
        return by_status

    def get_tasks_by_description(self, description):
        self.validator.validate_description(description)
        for task in self.tasks:
            if task.description == description:
                return task
        return None

    def delete_task(self, description):
        self.validator.validate_description(description)
        for i,task in enumerate(self.tasks):
            if task.description == description:
                del self.tasks[i]
                return True
        return False

    def clear_tasks(self):
        self.tasks = []



