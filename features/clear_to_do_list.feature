Feature: Clear the entire to-do list.
    @clearTodo
        Scenario: Delete all tasks of to-do list.
            Given a set list of to-do
            | DESCRIPTION                 | DATE       | STATUS      | PRIORITY|
            | Clean the car        | 31-07-2023 | NOT_COMPLETED | MEDIUM  |
            | Buy the bottle water | 30-07-2023 | NOT_COMPLETED | LOW     |
            When the user click on "Delete All" icon
            Then the todo list should be empty.
            | DESCRIPTION                 | DATE       | STATUS       | PRIORITY |
