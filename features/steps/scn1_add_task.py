from behave import *
from src.todo.todo import TodoList
from src.task.task import Task

#Condiciones antes de empezar cualquier STEP
def before_scenario(context, scenario):
	context = {}

# Step 1: Given the to-do list is empty
@given('the to-do list is empty')
def step_impl(context):
# Set the to-do list as an empty list
    global to_do_list
    to_do_list = TodoList()
    context.to_do_list = to_do_list
# Step 2: When the user adds
@when('the user adds')
def step_impl(context):
    # Add the task to the to-do list
    global to_do_list
    for row in context.table:
        tsk = Task(row["DESCRIPTION"],row["DATE"],row["PRIORITY"])
        context.to_do_list.add_task(tsk)
# Step 3: Then the to-do list should contain "Buy Book: Animal Farm,LOW"
@then('the to-do list should contain "{task}"')
def step_impl(context, task):
# Check if the task is in the to-do list
    global to_do_list
    task_info = task.split(",")
    tsk = Task(task_info[0], task_info[1],task_info[2])
    for t in context.to_do_list.tasks:
        if t.description == tsk.description:
            assert True, f'Task is in the to-do list'

@then('the task added is')
def step_impl(context):
    tsk_lst = context.to_do_list.tasks
    on_lst = TodoList()
    for row in context.table:
        tsk = Task(row["DESCRIPTION"],row["DATE"],row["PRIORITY"])
        on_lst.add_task(tsk)

    tasks = on_lst.tasks

    for i in range(len(tsk_lst)):
        if (tsk_lst[i].description == tasks[i].description) and (tsk_lst[i].priority == tasks[i].priority):
            assert True, f'Task is in the to-do list'


