Feature: Delete task from to do list.
    @deleteTask
        Scenario: Remove task of to do list.
            Given a set of todo list
            | DESCRIPTION          | DATE       | STATUS      | PRIORITY|
            | Clean the car        | 31-07-2023 | NOT_COMPLETED | MEDIUM  |
            | Buy the bottle water | 30-07-2023 | NOT_COMPLETED | LOW     |
            When the user click on "Delete" icon on "Clean the car" task
            Then the task "Clean the car" should not appear on the todo list.
            | DESCRIPTION          | DATE       | STATUS       | PRIORITY |
            | Buy the bottle water | 30-07-2023 | NOT_COMPLETED  | LOW      |
