class InvalidDate(Exception):
    def __init__(self):
        super().__init__("Invalid date format. Please use DD-MM-YYYY")

class InvalidPriority(Exception):
    def __init__(self):
        super().__init__("Invalid priority. Please use LOW, MEDIUM or HIGH")

class InvalidStatus(Exception):
    def __init__(self):
        super().__init__("Invalid status. Please use NOT_COMPLETED, IN_PROGRESS or COMPLETED")

class InvalidTask(Exception):
    def __init__(self):
        super().__init__("Invalid task. Please use a valid task")
        