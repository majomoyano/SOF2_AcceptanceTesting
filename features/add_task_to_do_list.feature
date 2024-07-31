Feature: Add a task to the to-do list
    @addTask
    Scenario: Adding a task to the to-do list
        Given the to-do list is empty
        When the user adds
        | DESCRIPTION                   | DATE       | STATUS        | PRIORITY |
        | Buy Book: Animal Farm         | 31-07-2023 | NOT_COMPLETED | LOW      | 
        Then the to-do list should contain "Buy Book: Animal Farm,31-07-2023,LOW"
        And the task added is
        | DESCRIPTION                   | DATE       | STATUS        | PRIORITY |
        | Buy Book: Animal Farm         | 31-07-2023 | NOT_COMPLETED | LOW      |
