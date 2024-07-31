Feature: Search by a none existing date
    @noneDate
    Scenario: Filter task by a none existing date
        Given list to-do 
        | DESCRIPTION               | DATE       | STATUS        | PRIORITY |
        | Buy Book: Animal Farm     | 23-07-2023 | COMPLETED     | LOW      |
        | Buy groceries             | 01-08-2023 | NOT_COMPLETED | MEDIUM   |
        | SE homework               | 31-07-2023 | IN_PROGRESS   | HIGH     |
        | Clean the bathroom        | 08-08-2023 | NOT_COMPLETED | HIGH     |
        When the user search by a none existing date "05-06-2020"
        Then show no task on list 
        And to-do list is
        | DESCRIPTION               | DATE       | STATUS        | PRIORITY |

