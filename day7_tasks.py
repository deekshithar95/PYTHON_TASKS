'''
Task 1: Use super() properly
Modify constructors so child classes reuse parent initialization.
👉 Requirement:
User should have name and id
Student adds dept and fees
Faculty adds salary
TempFaculty adds duration
👉 Expected:
class Student(User):
    def __init__(self, name, id, dept, fees):
        super().__init__(name, id)
        self.dept = dept
        self.fees = fees
'''
class User:
    def __init__(self, name, id):
        self.name = name
        self.id = id

class Student(User):
    def __init__(self, name, id, dept, fees):
        super().__init__(name, id)
        self.dept = dept
        self.fees = fees

class Faculty(User):
    def __init__(self, name, id, salary):
        super().__init__(name, id)
        self.salary = salary

class TempFaculty(Faculty):
    def __init__(self, name, id, salary, duration):
        super().__init__(name, id, salary)
        self.duration = duration
# Example usage:
student = Student("Alice", 1, "Computer Science", 10000)
faculty = Faculty("Dr. Smith", 2, 50000)
temp_faculty = TempFaculty("Dr. Brown", 3, 40000, "6 months")
print(student.name, student.id, student.dept, student.fees)
print(faculty.name, faculty.id, faculty.salary)
print(temp_faculty.name, temp_faculty.id, temp_faculty.salary, temp_faculty.duration)

'''
✅ Task 2: Apply Abstraction
Create an abstract base class.
👉 Requirement:
Create AbstractUser using ABC
Add abstract method get_details()
All child classes must implement it
👉 Example expectation:
from abc import ABC, abstractmethod

class AbstractUser(ABC):
    @abstractmethod
    def get_details(self):
        pass
'''
from abc import ABC, abstractmethod
class AbstractUser(ABC):
    @abstractmethod
    def get_details(self):
        pass
class User(AbstractUser):
    def __init__(self, name, id):
        self.name = name
        self.id = id
    def get_details(self):
        return f"Name: {self.name}, ID: {self.id}"
class Student(User):
    def __init__(self, name, id, dept, fees):
        super().__init__(name, id)
        self.dept = dept
        self.fees = fees
    def get_details(self):
        return f"{super().get_details()}, Dept: {self.dept}, Fees: {self.fees}"
class Faculty(User):
    def __init__(self, name, id, salary):
        super().__init__(name, id)
        self.salary = salary
    def get_details(self):
        return f"{super().get_details()}, Salary: {self.salary}"
class TempFaculty(Faculty):
    def __init__(self, name, id, salary, duration):
        super().__init__(name, id, salary)
        self.duration = duration
    def get_details(self):
        return f"{super().get_details()}, Duration: {self.duration}"
# Example usage:
student = Student("Alice", 1, "Computer Science", 10000)    
faculty = Faculty("Dr. Smith", 2, 50000)
temp_faculty = TempFaculty("Dr. Brown", 3, 40000, "6 months")
print(student.get_details())
print(faculty.get_details())
print(temp_faculty.get_details())

'''
✅ Task 3: Sorting using key
Create a list of students and sort them.
👉 Requirement:
Sort students by fees
Sort faculty by salary
👉 Example:
students.sort(key=lambda x: x.fees)
'''
students = [
    Student("Alice", 1, "Computer Science", 10000),
    Student("Bob", 2, "Mathematics", 8000),
    Student("Charlie", 3, "Physics", 12000)
]
faculty = [
    Faculty("Dr. Smith", 1, 50000), 
    Faculty("Dr. Johnson", 2, 60000),
    Faculty("Dr. Brown", 3, 40000)
]
students.sort(key=lambda x: x.fees)
faculty.sort(key=lambda x: x.salary)
print("Sorted Students by Fees:")
for student in students:
    print(student.get_details())
print("\nSorted Faculty by Salary:")
for member in faculty:
    print(member.get_details())

'''
✅ Task 4: Use map()
Transform data.
👉 Requirement:
Extract only student names using map
👉 Example:
names = list(map(lambda s: s.name, students))
'''
students = [
    Student("Alice", 101, "CS", 50000),
    Student("Bob", 102, "Math", 30000),
    Student("Charlie", 103, "Physics", 40000)
]
names = list(map(lambda s: s.name, students))
print("Student Names:", names)

'''
✅ Task 5: Use filter()
Filter data.
👉 Requirement:
Get students with fees > 50000
Get faculty with salary > 30000
👉 Example:
high_fee_students = list(filter(lambda s: int(s.fees) > 50000, students))
'''
students = [
    Student("Alice", 101, "CS", 50000),
    Student("Bob", 102, "Math", 80000),
    Student("Charlie", 103, "Physics", 90000)
]
faculty = [
    Faculty("Dr. Smith", 1, 50000),
    Faculty("Dr. Johnson", 2, 60000),
    Faculty("Dr. Brown", 3, 40000)
]
high_fee_students = list(filter(lambda s: s.fees > 50000, students))
high_salary_faculty = list(filter(lambda f: f.salary > 30000, faculty))
print("Students with Fees > 50000:")
for student in high_fee_students:
    print(student.get_details())
print("\nFaculty with Salary > 30000:")
for member in high_salary_faculty:
    print(member.get_details())

'''
✅ Task 6: Use reduce()
Aggregate data.
👉 Requirement:
Calculate total salary of all faculty
Calculate total fees collected
👉 Example:
from functools import reduce

total_fees = reduce(lambda acc, s: acc + int(s.fees), students, 0)
'''
from functools import reduce
students = [    
    Student("Alice", 101, "CS", 50000),
    Student("Bob", 102, "Math", 80000),
    Student("Charlie", 103, "Physics", 90000)
]
faculty = [
    Faculty("Dr. Smith", 1, 50000),
    Faculty("Dr. Johnson", 2, 60000),
    Faculty("Dr. Brown", 3, 40000)
]
total_fees = reduce(lambda acc, s: acc + s.fees, students, 0)
total_salary = reduce(lambda acc, f: acc + f.salary, faculty, 0)
print("Total Fees Collected:", total_fees)
print("Total Salary of Faculty:", total_salary)

'''
✅ Task 7: Higher Order Function
Create a function that accepts another function.
👉 Requirement:
Create function process_users(users, func)
Apply any operation (map/filter)
👉 Example:
def process_users(users, func):
    return list(map(func, users))
'''
def process_users(users, func):
    return list(map(func, users))
students = [
    Student("Alice", 101, "CS", 50000),
    Student("Bob", 102, "Math", 80000),
    Student("Charlie", 103, "Physics", 90000)
]
# Example: Get student names using process_users
student_names = process_users(students, lambda s: s.name)
print("Student Names:", student_names)


'''
🧪 Final Challenge (Important 🔥)
👉 Build a mini system:
Store multiple students & faculty in lists
Print:
All details (get_details())
Sorted data
Filtered data
Total fees & salary
Use at least 3 functional programming concepts together
'''
students = [
    Student("Alice", 101, "CS", 50000),
    Student("Bob", 102, "Math", 80000),
    Student("Charlie", 103, "Physics", 90000),
    Student("David", 104, "Chemistry", 45000),
    Student("Eve", 105, "Biology", 55000),
    Student("Frank", 106, "History", 30000),
    Student("Grace", 107, "Literature", 60000)
]
faculty = [
    Faculty("Dr. Smith", 1, 50000),
    Faculty("Dr. Johnson", 2, 60000),
    Faculty("Dr. Brown", 3, 40000),
    Faculty("Dr. Green", 4, 70000),
    Faculty("Dr. White", 5, 35000),
    Faculty("Dr. Black", 6, 45000),
    Faculty("Dr. Gray", 7, 55000)
]
# Print all details
print("Student Details:")   
for student in students:
    print(student.get_details())
print("\nFaculty Details:")
for member in faculty:
    print(member.get_details())
# Sort students by fees and faculty by salary
students.sort(key=lambda s: s.fees)
faculty.sort(key=lambda f: f.salary)
print("\nSorted Students by Fees:")
for student in students:
    print(student.get_details())
print("\nSorted Faculty by Salary:")
for member in faculty:
    print(member.get_details())
# Filter students with fees > 50000 and faculty with salary > 30000
high_fee_students = list(filter(lambda s: s.fees > 50000, students))
high_salary_faculty = list(filter(lambda f: f.salary > 30000, faculty))
print("\nStudents with Fees > 50000:")
for student in high_fee_students:
    print(student.get_details())
print("\nFaculty with Salary > 30000:")
for member in high_salary_faculty:
    print(member.get_details())
# Calculate total fees and salary using reduce
total_fees = reduce(lambda acc, s: acc + s.fees, students, 0)
total_salary = reduce(lambda acc, f: acc + f.salary, faculty, 0)
print("\nTotal Fees Collected:", total_fees)
print("Total Salary of Faculty:", total_salary)



