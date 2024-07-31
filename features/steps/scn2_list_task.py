from behave import *
from src.todo.todo import TodoList
from src.task.task import Task

# Condiciones antes de empezar cualquier STEP
def before_scenario(context, scenario):
    context = {}

# Step 1: Given the to-do list
@given('the to-do list')
def step_impl(context):
    # Set the to-do list
    global to_do_list
    to_do_list  = TodoList()

    for row in context.table:
        tsk = Task(row["DESCRIPTION"],row["DATE"],row["PRIORITY"])
        to_do_list.add_task(tsk)

    to_do_list.mark_task_completed(to_do_list.tasks[0].description)
    to_do_list.mark_task_in_progress(to_do_list.tasks[2].description) 

    context.to_do_list = to_do_list

# Step 2: When the user wants to see the to-do list
@when('the user wants to see the to-do list')
def step_impl(context):
    global to_do_list
    to_do_list = context.to_do_list

# Step 3: Then show all the to-do list 
@then('show all the to-do list')
def step_impl(context):
    global to_do_list
    to_do_list = context.to_do_list
    
# Step 4: And all the to-do list is
@then('print all the to-do list')
def step_impl(context):
    # Print all the to-do list
    global to_do_list
    to_do_list = context.to_do_list
    tasks_list = TodoList()

    for row in context.table:
        tsk = Task(row["DESCRIPTION"],row["DATE"],row["PRIORITY"])
        tasks_list.add_task(tsk)

    tasks_list.mark_task_completed(tasks_list.tasks[0].description)
    tasks_list.mark_task_in_progress(tasks_list.tasks[2].description) 

    assert to_do_list.tasks == tasks_list.tasks