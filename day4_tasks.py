'''
Mini Project 1: Employee Management System
Concepts: Dictionary, List, Functions
👉 Build a system to manage employees.
Requirements:
Store multiple employees (list of dictionaries)
Each employee: name, age, role, salary
Add new employee
Update employee details
Delete employee
Display all employees
'''
# Employee Management System
employees = []
def add_employee(name, age, role, salary):
    employee = {
        'name': name,
        'age': age,
        'role': role,
        'salary': salary
    }
    employees.append(employee)
    print(f"Employee {name} added successfully.")    

def update_employee(name, age=None, role=None, salary=None):
    for employee in employees:
        if employee['name'] == name:
            if age is not None:
                employee['age'] = age
            if role is not None:
                employee['role'] = role
            if salary is not None:
                employee['salary'] = salary
            print(f"Employee {name} updated successfully.")
            return
    print(f"Employee {name} not found.")    

def delete_employee(name):
    global employees
    employees = [emp for emp in employees if emp['name'] != name]
    print(f"Employee {name} deleted successfully.") 

def display_employees():
    if not employees:
        print("No employees to display.")
        return
    for emp in employees:
        print(f"Name: {emp['name']}, Age: {emp['age']}, Role: {emp['role']}, Salary: {emp['salary']}")  

# Example usage function calls
add_employee("Alice", 30, "Developer", 70000)
add_employee("Bob", 25, "Designer", 60000)
add_employee("Charlie", 35, "Manager", 90000)
add_employee("Diana", 28, "Tester", 65000)
display_employees()
update_employee("Alice", salary=75000) 
update_employee("Bob", role="Senior Designer")
display_employees()
delete_employee("Bob")
display_employees()

'''
Mini Project 2: Student Report Card
Concepts: Dictionary, Functions, Formatting
👉 Create a report system.
Requirements:
Store student name and marks (3 subjects)
Calculate total and average
Print formatted report card
Display grade based on average
'''
# Student Report Card
def create_report_card(name, marks):
    total = sum(marks)
    average = total / len(marks)
    grade = calculate_grade(average)
    print(f"Report Card for {name}")
    print(f"Marks: {marks}")
    print(f"Total: {total}")
    print(f"Average: {average:.2f}")
    print(f"Grade: {grade}")
def calculate_grade(average):
    if average >= 90:
        return 'A'
    elif average >= 80:
        return 'B'
    elif average >= 70:
        return 'C'
    elif average >= 60:
        return 'D'
    else:
        return 'F'
# Example usage function calls
create_report_card("Emily", [85, 92, 78])
create_report_card("David", [65, 70, 72])
create_report_card("Sophia", [55, 60, 58])
create_report_card("Michael", [95, 98, 100])
create_report_card("Olivia", [80, 85, 88])

'''
Mini Project 3: Shopping Cart System
Concepts: List, Dictionary, Loop
👉 Simulate an online cart.
Requirements:
Add products (name, price, quantity)
Calculate total bill
Remove item from cart
Display all items in formatted way
'''
# Shopping Cart System
cart = []
def add_to_cart(name, price, quantity):
    item = {
        'name': name,
        'price': price,
        'quantity': quantity
    }
    cart.append(item)
    print(f"Added {quantity} of {name} to cart.")
def calculate_total():
    total = sum(item['price'] * item['quantity'] for item in cart)
    print(f"Total Bill: ${total:.2f}")

def display_cart():
    if not cart:
        print("Cart is empty.")
        return
    print("Items in Cart:")
    for item in cart:
        print(f"Name: {item['name']}, Price: ${item['price']:.2f}, Quantity: {item['quantity']}")   
def remove_from_cart(name):
    global cart
    cart = [item for item in cart if item['name'] != name]
    print(f"Removed {name} from cart.")
# Example usage function calls
add_to_cart("Laptop", 999.99, 1)
add_to_cart("Headphones", 199.99, 2)
add_to_cart("Mouse", 49.99, 1)
add_to_cart("Keyboard", 89.99, 1)
add_to_cart("Monitor", 299.99, 1)
add_to_cart("USB Cable", 9.99, 3)
display_cart()
calculate_total()
remove_from_cart("Headphones")
display_cart()
calculate_total()

'''
Mini Project 4: Login & User Validation
Concepts: Dictionary, Condition
👉 Basic authentication system.
Requirements:
Store users (username & password)
Take login input
Validate credentials
Print success or failure message
'''
# Login & User Validation
users = {
    "admin": "password123",
    "user1": "mypassword",
    "user2": "anotherpassword"
}

def login(username, password):
    if username in users and users[username] == password:
        print("Login successful.")
    else:
        print("Invalid username or password.")
# Example usage function calls
login("admin", "password123")  # Should print "Login successful."
login("user1", "wrongpassword")  # Should print "Invalid username or password."
login("user2", "anotherpassword")  # Should print "Login successful."
login("nonexistent", "nopassword")  # Should print "Invalid username or password."

'''
Mini Project 5: Unique Visitor Counter
Concepts: Set
👉 Track unique visitors.
Requirements:
Store visitor names in a set
Avoid duplicates
Print total unique visitors
'''
# Unique Visitor Counter
unique_visitors = set() 
def add_visitor(name):
    unique_visitors.add(name)
    print(f"Visitor {name} added.")
def total_unique_visitors():
    print(f"Total Unique Visitors: {len(unique_visitors)}")
# Example usage function calls
add_visitor("Alice")
add_visitor("Bob")
add_visitor("Charlie")
add_visitor("Alice")  # Duplicate, should not increase count
add_visitor("Diana")
total_unique_visitors()  # Should print 4 unique visitors

'''
Mini Project 6: String Formatter Tool
Concepts: String Formatting
👉 Build a formatting utility.
Requirements:
Input name and product
Display formatted sentence
Show padded output (left, right, center)
'''
# String Formatter Tool
def format_string(name, product):
    formatted = f"{name} bought a {product}."
    print(formatted)
def padded_output(text, width):
    left_padded = text.ljust(width)
    right_padded = text.rjust(width)
    center_padded = text.center(width)
    print(f"Left Padded: '{left_padded}'")
    print(f"Right Padded: '{right_padded}'")
    print(f"Center Padded: '{center_padded}'")
# Example usage function calls
format_string("Alice", "laptop")
padded_output("Hello", 20)

'''
Mini Project 7: Bank Account System
Concepts: Functions, Dictionary
👉 Simulate bank operations.
Requirements:
Create account (name, balance)
Deposit money
Withdraw money
Check balance
'''
# Bank Account System
accounts = {}
def create_account(name, balance):
    accounts[name] = balance
    print(f"Account for {name} created with balance ${balance:.2f}.")
def deposit(name, amount):
    if name in accounts:
        accounts[name] += amount
        print(f"Deposited ${amount:.2f} to {name}'s account.")
    else:
        print(f"Account for {name} does not exist.")
def withdraw(name, amount):
    if name in accounts:
        if accounts[name] >= amount:
            accounts[name] -= amount
            print(f"Withdrew ${amount:.2f} from {name}'s account.")
        else:
            print(f"Insufficient funds in {name}'s account.")
    else:
        print(f"Account for {name} does not exist.")
def check_balance(name):
    if name in accounts:
        print(f"Balance for {name}: ${accounts[name]:.2f}")
    else:
        print(f"Account for {name} does not exist.")
# Example usage function calls
create_account("Alice", 1000)
create_account("Bob", 500)
deposit("Alice", 200)
withdraw("Bob", 100)
check_balance("Alice")
check_balance("Bob")

'''
 Mini Project 8: Voting System
Concepts: Dictionary, Loop
👉 Count votes for candidates.
Requirements:
Store candidates and votes
Add vote
Display winner
'''
# Voting System
votes = {}
def add_vote(candidate):
    if candidate in votes:
        votes[candidate] += 1
    else:
        votes[candidate] = 1
    print(f"Vote added for {candidate}.")
def display_winner():
    if not votes:
        print("No votes cast.")
        return
    winner = max(votes, key=votes.get)
    print(f"Winner: {winner} with {votes[winner]} votes.")
# Example usage function calls
add_vote("Alice")
add_vote("Bob")
add_vote("Alice")
add_vote("Charlie")
add_vote("Bob")
add_vote("Alice")
display_winner()  # Should print "Winner: Alice with 3 votes."

'''
Mini Project 9: Course Enrollment System
Concepts: List + Dictionary
👉 Manage student enrollments.
Requirements:
Add student with course list
Update courses
Display student details
'''
# Course Enrollment System
students = {}
def add_student(name, courses):
    students[name] = courses
    print(f"Student {name} added with courses: {courses}")
def update_courses(name, courses):
    if name in students:
        students[name] = courses
        print(f"Courses for {name} updated to: {courses}")
    else:
        print(f"Student {name} not found.")
def display_student(name):
    if name in students:
        print(f"Student: {name}, Courses: {students[name]}")
    else:
        print(f"Student {name} not found.")
# Example usage function calls
add_student("Alice", ["Math", "Science"])
add_student("Bob", ["History", "Art"])
update_courses("Alice", ["Math", "Science", "Literature"])
display_student("Alice")
display_student("Bob")

'''
Mini Project 10: Number Utility Tool
Concepts: Functions, Formatting
👉 Work with numbers.
Requirements:
Convert number to binary, octal, hex
Format large numbers with commas
Print scientific notation
'''
# Number Utility Tool
def convert_number(num):
    print(f"Binary: {bin(num)}")
    print(f"Octal: {oct(num)}")
    print(f"Hexadecimal: {hex(num)}")
def format_large_number(num):
    formatted = f"{num:,}"
    print(f"Formatted Number: {formatted}")
def scientific_notation(num):
    print(f"Scientific Notation: {num:.2e}")
# Example usage function calls
convert_number(255)
format_large_number(1000000)
scientific_notation(0.000123)
