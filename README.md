# Project Description 
## Overview
This project involves implementing two classes, **Expense** and **ExpenseDatabase** which would be used to model and manage financial expenses. Several methods would be defined on each of the classes to carry out different actions such as the addition of records, modification of existing records, deletion of records, etc.

## Modules Used
* UUID: The module *UUID* was imported to help generate random unique identifiers which would be used as the '**id**'.
* DATETIME: The module *datetime* was imported to generate a timestamp to indicate when an event occurred to be used with '**created_at**' and '***updated_at**' attributes. 

## Classes
A class called '**Expense**' was created and consisted of 4 methods (__init __, update(), to_dict() and __repr __). The __init __ method is referred to as a constructor, the attributes relating to this class('**Expense**') were declared in the __init __ method. 

The second class called '**ExpenseDatabase**' was created. This class had 6 methods (__init __, add_expense(), remove_expense(), get_expense_by_id(), get_expense_by_title(), to_dict()). The class functions as a database that stores expense records from the class '**Expense**' and performs several actions on these records using various methods already defined in the class '**ExpenseDatabase**'.


# How to Clone Repository
To clone a repository, you have to have installed git bash on your local system.

Step 1 - Go to the repository you want to clone

Step 2 - Click on the "**<> Code**" button and copy the HTTPS link(For this repo it would be https://github.com/bazuayelewis/financial_expenses.git)

Step 3 - Go to git bash and run the command git clone https://github.com/ *username* / *repo_name*.git


# How to run Code
To run the code, we initialize the class '**Expense**' and provide data to satisfy the required arguments. Then we initialize the class '**ExpenseDatabase**' and using the method '***add_expense()***' the initialized expense records would be added to the empty list already specified  

```python
if __name__ == "__main__":
    test_1 = Expense("John", 20.8)
    test_2 = Expense("Lewis", 50)
    test_3 = Expense("James", 9.57)

    edb = ExpenseDatabase()
    for i in [test_1, test_2, test_3]:
        edb.add_expense(i)
```

![Screenshot 2023-12-24 112804](https://github.com/bazuayelewis/financial_expenses/assets/107050974/8392dfa3-8527-494f-9eee-c593089e20ca)

Let's explore one more method, the '***get_expense_by_title()***' method. This method takes in one argument and that is the '**title**' and returns a matching expense record and if no record matches the title 'None' is displayed.

```python
    print(edb.get_expense_by_title("Lewis"))
```

![Screenshot 2023-12-24 123741](https://github.com/bazuayelewis/financial_expenses/assets/107050974/003bda57-a099-40bf-985d-3e0cb4c2f029)




