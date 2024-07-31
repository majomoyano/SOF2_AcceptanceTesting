Feature: Change status of the task.
    @changeStatus
    Scenario: Change status of task.
        Given set of to-do list
        | DESCRIPTION          | DATE       | STATUS        | PRIORITY|
        | Clean the car        | 31-07-2023 | NOT_COMPLETED | MEDIUM  |
        | Buy the bottle water | 30-07-2023 | NOT_COMPLETED | LOW     |
        Given the user click on status of task
        When the user select "Clean the car, NOT_COMPLETED" Status
        Then the status of task change to "IN_PROGRESS" and updated it.
        | DESCRIPTION          | DATE       | STATUS          | PRIORITY |
        | Clean the car        | 31-07-2023 | IN_PROGRESS     | MEDIUM   |
        | Buy the bottle water | 30-07-2023 | NOT_COMPLETED   | LOW      |

