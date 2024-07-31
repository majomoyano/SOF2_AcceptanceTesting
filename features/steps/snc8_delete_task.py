from behave import *
from src.todo.todo import TodoList
from src.task.task import Task

# Condiciones antes de empezar cualquier STEP
def before_scenario(context, scenario):
    context = {}

@given('a set of todo list')
def step_impl(context):
    global to_do_list
    to_do_list  = TodoList()

    for row in context.table:
        tsk = Task(row["DESCRIPTION"],row["DATE"],row["PRIORITY"])
        to_do_list.add_task(tsk)

    context.to_do_list = to_do_list
    assert len(to_do_list.tasks) > 0, f'Not task added in to-do list.'


@when('the user click on "Delete" icon on "{description}" task')
def step_impl(context,description):
    global to_do_list
    to_do_list = context.to_do_list

    deleted = to_do_list.delete_task(description)
    assert deleted == True, f'Task {description} doesnt exists.'


@then('the task "{description}" should not appear on the todo list.')
def step_impl(context, description):
    global to_do_list
    to_do_list = context.to_do_list

    deleted = to_do_list.delete_task(description)
    assert deleted == False, f'The task {description} has not been deleted.'
