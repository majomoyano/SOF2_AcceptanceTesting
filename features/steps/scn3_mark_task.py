from behave import *
from src.todo.todo import TodoList
from src.task.task import Task

# Condiciones antes de empezar cualquier STEP
def before_scenario(context, scenario):
    context = {}

# Step 1: Given the to-do list
@given('a set of tasks on the to-do list')
def step_impl(context):
    global to_do_list
    to_do_list  = TodoList()

    for row in context.table:
        tsk = Task(row["DESCRIPTION"],row["DATE"],row["PRIORITY"])
        to_do_list.add_task(tsk)

    context.to_do_list = to_do_list

@when('the user select "{description}" description')
def step_impl(context,description):
    global to_do_list
    to_do_list = context.to_do_list
    context.description = description

@then('change to name of the description to "{new_description}" and updated it.')
def step_impl(context, new_description):
    global to_do_list
    to_do_list = context.to_do_list
    tasks = to_do_list.tasks

    for t in tasks:
        if t.description == context.description:
            t.description = new_description
            assert t.description == new_description, f'Description not updated it!'
