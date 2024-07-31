Feature: List all tasks in the to-do list
    @listAllTask
    Scenario: List all task on the to-do list
        Given the to-do list
        | DESCRIPTION               | DATE       | STATUS        | PRIORITY |
        | Buy Book: Animal Farm     | 23-07-2023 | COMPLETED     | LOW      |
        | Buy groceries             | 01-08-2023 | NOT_COMPLETED | MEDIUM   |
        | SE homework               | 31-07-2023 | IN_PROGRESS   | HIGH     |
        | Clean the bathroom        | 08-08-2023 | NOT_COMPLETED | HIGH     |
        When the user wants to see the to-do list
        Then show all the to-do list 
        And print all the to-do list
        | DESCRIPTION               | DATE       | STATUS        | PRIORITY |
        | Buy Book: Animal Farm     | 23-07-2023 | COMPLETED     | LOW      |
        | Buy groceries             | 01-08-2023 | NOT_COMPLETED | MEDIUM   |
        | SE homework               | 31-07-2023 | IN_PROGRESS   | HIGH     |
        | Clean the bathroom        | 08-08-2023 | NOT_COMPLETED | HIGH     |
        