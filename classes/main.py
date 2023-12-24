#Importing the required modules
import uuid 
from datetime import datetime, timezone


class Expense:

#Declaring the relevant attributes inside the constructor
    def __init__(self, title: str, amount: float):
        self.id = str(uuid.uuid4())
        self.title = title
        self.amount = amount
        self.created_at = datetime.utcnow()
        self.updated_at = datetime.utcnow()

#Creating a method to update title and/or amount and defaultly updating the updated_at    
    def update(self, title=None, amount=None):
        if title is not None:
           self.title = str(title)
        if amount is not None:
            self.amount = amount
        self.updated_at = datetime.utcnow()
        return f"The expense record was updated at {self.updated_at}"

    def to_dict(self):
        return dict(id = self.id, title = self.title, amount =self.amount, created_at = self.created_at, updated_at =self.updated_at)
   
    def __repr__(self):
        return f"{self.id}, {self.title}, {self.amount}, {self.created_at}, {self.updated_at}"


class ExpenseDatabase():
    def __init__(self):
        self.expenses = []

    def add_expense(self, expense):
        self.expenses.append(expense)
        print(f"{len(self.expenses)} expense record has been added successfully")
        return expense.id

    def remove_expense(self, expense_id):
        total = len(self.expenses)
        self.expenses = [expense for expense in self.expenses if expense.id != expense_id]
        if total>len(self.expenses):
            return (f"Expense record with {expense_id} has been successfully removed!")
        else:
            return ("ERROR: No matching expense record found!")

    def get_expense_by_id(self, expense_id):
        expense = [expense for expense in self.expenses if expense.id == expense_id]
        if len(expense) == 0:
            return None
        else:
            return expense[0]
        
    def get_expense_by_title(self, expense_title):
        expense = [expense for expense in self.expenses if expense.title == expense_title]
        if len(expense) == 0:
            return None
        else:
            return expense

    def to_dict(self):
        return [expense.to_dict() for expense in self.expenses]

