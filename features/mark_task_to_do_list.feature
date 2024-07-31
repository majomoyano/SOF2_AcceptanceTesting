#language: en

Feature: Change the description of a task.
    @changeDesp
    Scenario: Change the description of a task.
        Given a set of tasks on the to-do list
        | DESCRIPTION          | DATE       | STATUS        | PRIORITY|
        | Clean the car        | 31-07-2023 | NOT_COMPLETED | MEDIUM  |
        | Buy the bottle water | 30-07-2023 | NOT_COMPLETED | LOW     |
        When the user select "Clean the car" description
        Then change to name of the description to "Clean the house" and updated it.
        | DESCRIPTION          | DATE       | STATUS       | PRIORITY |
        | Clean the house      | 31-07-2023 | NOT_COMPLETED| MEDIUM   |
        | Buy the bottle water | 30-07-2023 | NOT_COMPLETED| LOW      |









