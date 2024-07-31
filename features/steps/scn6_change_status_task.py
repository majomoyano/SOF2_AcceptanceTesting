from behave import *
from src.todo.todo import TodoList
from src.task.task import Task

# Condiciones antes de empezar cualquier STEP
def before_scenario(context, scenario):
    context = {}

# Step 1: Given the to-do list
@given('set of to-do list')
def step_impl(context):
    global to_do_list
    to_do_list  = TodoList()

    for row in context.table:
        tsk = Task(row["DESCRIPTION"],row["DATE"],row["PRIORITY"])
        to_do_list.add_task(tsk)

    context.to_do_list = to_do_list

@given('the user click on status of task')
def step_given_user_clicks_on_status_of_task(context):
    global to_do_list
    to_do_list = context.to_do_list

@when('the user select "{task}" Status')
def step_impl(context,task):
    global to_do_list
    to_do_list = context.to_do_list
    list_tsk = task.split(",")
    context.description = list_tsk[0]
    context.status = list_tsk[1]


@then('the status of task change to "{status}" and updated it.')
def step_impl(context, status):
    global to_do_list
    to_do_list = context.to_do_list
    tasks = to_do_list.tasks

    for t in tasks:
        if t.description == context.description:
            if context.status == 'NOT_COMPLETED':
                to_do_list.mark_task_in_progress(context.description)
                assert t.status == status, f'Status of task {context.description} did not change correctly'
