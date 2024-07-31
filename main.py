# Add a new task to the to-do list.
# • List all the tasks in the to-do list.
# • Mark a task as completed.
# • Clear the entire to-do list.

# Get todo list tasks by date range
# Get todo list by priority (high, medium, low)
# Get todo list by status (completed, not completed)
from utils.custom_ex import InvalidDate, InvalidPriority, InvalidStatus, InvalidTask
from src.task.task import Task
from src.todo.todo import TodoList

def print_menu():
    print()
    print("What would you like to do?")
    print("1. Add a new task")
    print("2. List all the tasks")
    print("3. Mark a task as completed")
    print("4. Clear the entire to-do list")
    print("5. Get to-dos by priority")
    print("6. Get to-dos by status")
    print("7. Get to-dos by due date")
    print("8. Quit")

def main():
    print("Welcome to the Todo List App of T1!")
    todo_list = TodoList()
    
    user_quit = False

    while not user_quit:
        print_menu()
        user_input = input("Enter your choice: ")
        try:
            if user_input == "1":
                description = input("Enter the task description: ")
                priority = input("Enter the priority (HIGH, LOW, MEDIUM): ")
                date = input("Enter the due date (DD-MM-YYYY): ")
                created_task = Task(description, date, priority)
                todo_list.add_task(created_task)
            elif user_input == "2":
                todo_list.list_tasks()
            elif user_input == "3":
                description = input("Enter the task description: ")
                todo_list.mark_task_completed(description)
            elif user_input == "4":
                todo_list.clear_tasks()
            elif user_input == "5":
                priority = input("Enter the priority (HIGH, LOW, MEDIUM): ")
                todo_list.get_tasks_by_priority(priority)
            elif user_input == "6":
                status = input("Enter the status (COMPLETED, NOT_COMPLETED, IN_PROGRESS): ")
                todo_list.get_tasks_by_status(status)
            elif user_input == "7":
                start_date = input("Enter the start date (DD-MM-YYYY): ")
                end_date = input("Enter the end date (DD-MM-YYYY): ")
                todo_list.get_tasks_by_date_range(start_date, end_date)
            elif user_input == "8":
                user_quit = True
            else:
                print("Invalid choice input")
        except InvalidDate as e:
            print(e)
        except InvalidPriority as e:
            print(e)
        except InvalidStatus as e:
            print(e)
        except InvalidTask as e:
            print(e)
        except Exception as e:
            print(e)
            

    print("Thank you for using the Todo List App!")


if __name__ == "__main__":      
    main()
    