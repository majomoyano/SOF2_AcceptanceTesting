Feature: Search by none existing priority
    @nonePriority
    Scenario: Filter task by a none existing priority 
        Given to-do list
        | DESCRIPTION               | DATE       | STATUS        | PRIORITY |
        | Buy groceries             | 01-08-2023 | NOT_COMPLETED | MEDIUM   |
        | SE homework               | 31-07-2023 | IN_PROGRESS   | HIGH     |
        | Clean the bathroom        | 08-08-2023 | NOT_COMPLETED | HIGH     |
        When the user search by a none existing priority "LOW"
        Then show no task on the to-do list
        And the to-do list is
        | DESCRIPTION                   | DATE       | STATUS        | PRIORITY |
  

