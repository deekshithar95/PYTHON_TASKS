
'''
Smart Expense Manager (Real-Time Project)
🎯 Objective
Build a Smart Expense Management System using:

Track daily expenses
Categorize spending
Analyze where money is going'''

from abc import ABC, abstractmethod
import mysql.connector
from functools import reduce

class Database(ABC):
    @abstractmethod
    def connect(self):
        pass

class User(Database):
    def __init__(self, name):
        self.__name = name   # private variable
        self.user_id = None

    def connect(self):
        return mysql.connector.connect(
            host="localhost",
            user="root",
            password="Anju@123",
            port=3306,
            database="final_task"
        )

    def create_user(self):
        conn = self.connect()
        cursor = conn.cursor()
        cursor.execute("INSERT INTO users (name) VALUES (%s)", (self.__name,))
        conn.commit()
        self.user_id = cursor.lastrowid
        conn.close()
        print(f"User {self.__name} created with ID {self.user_id}")

class Expense(User):
    def __init__(self, user_id, amount, category, description, date):
        super().__init__(name=None)  # super() usage
        self.user_id = user_id
        self.amount = amount
        self.category = category
        self.description = description
        self.date = date

    def add_expense(self):
        conn = self.connect()
        cursor = conn.cursor()
        cursor.execute("""INSERT INTO expenses (user_id, amount, category, description, date)
                          VALUES (%s, %s, %s, %s, %s)""",
                       (self.user_id, self.amount, self.category, self.description, self.date))
        conn.commit()
        conn.close()
        print("Expense added successfully!")

    def view_expenses(self):
        conn = self.connect()
        cursor = conn.cursor()
        cursor.execute("""SELECT u.name, e.amount, e.category, e.description, e.date
                          FROM expenses e JOIN users u ON e.user_id = u.user_id
                          WHERE e.user_id = %s""", (self.user_id,))
        rows = cursor.fetchall()
        conn.close()
        for row in rows:
            print(row)

def filter_by_category(expenses, category):
    return list(filter(lambda x: x[2] == category, expenses))

def filter_by_date(expenses, date):
    return [exp for exp in expenses if exp[4] == date]

def total_expense(expenses):
    amounts = list(map(lambda x: x[1], expenses))
    return reduce(lambda a, b: a + b, amounts)

def category_spending(expenses):
    categories = {exp[2]: 0 for exp in expenses}
    for exp in expenses:
        categories[exp[2]] += exp[1]
    return {cat: amt for cat, amt in categories.items()}

def delete_expense(exp_id):
    conn = mysql.connector.connect(host="localhost", user="root", password="", database="expense_db")
    cursor = conn.cursor()
    cursor.execute("DELETE FROM expenses WHERE exp_id=%s", (exp_id,))
    conn.commit()
    conn.close()

def update_expense(exp_id, amount):
    conn = mysql.connector.connect(host="localhost", user="root", password="", database="expense_db")
    cursor = conn.cursor()
    cursor.execute("UPDATE expenses SET amount=%s WHERE exp_id=%s", (amount, exp_id))
    conn.commit()
    conn.close()

def monthly_report(expenses):
    report = {}
    for exp in expenses:
        month = exp[4].strftime("%Y-%m")
        report[month] = report.get(month, 0) + exp[1]
    return report

def highest_expense(expenses):
    return reduce(lambda a, b: a if a[1] > b[1] else b, expenses)

def smart_insight(expenses):
    category_totals = category_spending(expenses)
    max_cat = max(category_totals, key=category_totals.get)
    print(f"You are spending too much on {max_cat} this month")

# Create user
u1 = User("Darshan")
u1.create_user()

# Add expense
e1 = Expense(u1.user_id, 500, "Food", "Lunch", "2026-04-07")
e1.add_expense()

# View expenses
e1.view_expenses()

# Insights
expenses = [(u1.user_id, 500, "Food", "Lunch", "2026-04-07"),
            (u1.user_id, 1500, "Travel", "Flight", "2026-04-07")]
print(total_expense(expenses))
print(category_spending(expenses))
print(highest_expense(expenses))
smart_insight(expenses)
