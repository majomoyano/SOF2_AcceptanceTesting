from behave import *
from src.todo.todo import TodoList
from src.task.task import Task

# Condiciones antes de empezar cualquier STEP
def before_scenario(context, scenario):
    context = {}

@given('a set list of to-do')
def step_impl(context):
    global to_do_list
    to_do_list  = TodoList()

    for row in context.table:
        tsk = Task(row["DESCRIPTION"],row["DATE"],row["PRIORITY"])
        to_do_list.add_task(tsk)

    context.to_do_list = to_do_list
    assert len(to_do_list.tasks) > 0, f'Not task added in to-do list.'


@when('the user click on "Delete All" icon')
def step_impl(context):
    global to_do_list
    to_do_list = context.to_do_list


@then('the todo list should be empty.')
def step_impl(context):
    global to_do_list
    to_do_list = context.to_do_list

    to_do_list.clear_tasks()
    assert len(to_do_list.tasks) == 0, f'List is not empty.'
