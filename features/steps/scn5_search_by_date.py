from behave import *
from src.todo.todo import TodoList
from src.task.task import Task
#Condiciones antes de empezar cualquier STEP
def before_scenario(context, scenario):
	context = {}

# Step 1: Given the to-do list
@given('list to-do')
def step_impl(context):
# Set the to-do list
    global to_do_list
    to_do_list = TodoList()

    for row in context.table:
        tsk = Task(row["DESCRIPTION"],row["DATE"],row["PRIORITY"])
        to_do_list.add_task(tsk)

    to_do_list.mark_task_completed(to_do_list.tasks[0].description)
    to_do_list.mark_task_in_progress(to_do_list.tasks[2].description)

    context.todolist = to_do_list

# Step 2: When the user search by a none existing date "05-06-2020"
@when('the user search by a none existing date "{task}"')
def step_impl(context, task):
    global to_do_list, tsk
    to_do_list = context.todolist
    context.tsk = task
    tsk = context.tsk

# Step 3: Then show no task on the to-do list
@then('show no task on list')
def step_impl(context):
    global to_do_list, tsk
    to_do_list = context.todolist
    tsk = context.tsk

# Step 4: And the to-do list is
@then('to-do list is')
def step_impl(context):
    global to_do_list, tsk
    to_do_list = context.todolist
    tsk = context.tsk
    tsk_list =TodoList()


    for row in context.table:
        t = Task(row["DESCRIPTION"],row["DATE"],row["PRIORITY"])
        tsk_list.add_task(t)

    filtered_list = to_do_list.get_tasks_by_date_range(tsk,tsk)

    assert filtered_list == []




