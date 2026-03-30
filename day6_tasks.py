'''
OOP Practice Tasks (Python)
🔐 Task 1: Encapsulation (User Class)
👉 Create a class User with proper encapsulation
Requirements:
Make variables private
__user_name
__pwd
Create:
set_user(user_name, pwd)
get_user() → return username only (hide password)
Add:
register() → print username
login() → print login message
🎯 Expected Output:
Registering user: john
Logging in: john
'''

class User:
    def __init__(self):
        self.__user_name = None
        self.__pwd = None

    def set_user(self, user_name, pwd):
        self.__user_name = user_name
        self.__pwd = pwd

    def get_user(self):
        return self.__user_name

    def register(self):
        print(f"Registering user: {self.__user_name}")

    def login(self):
        print(f"Logging in: {self.__user_name}")

# Example usage
user = User()   
user.set_user("john", "password123")
user.register()  # Output: Registering user: john
user.login()     # Output: Logging in: john

'''
🧬 Task 2: Inheritance (User → Student, Faculty)
👉 Create parent class User
Parent Class:
register()
login()
Child Classes:
Student
student_greet() → print "Hello Student"
Faculty
faculty_greet() → print "Hello Faculty"
TempFaculty (Multilevel)
Inherit from Faculty
tempFaculty_greet() → print "Hello Temp Faculty"
🎯 Practice:
Call all methods using objects
Show:
Child can access parent methods
Parent cannot access child methods
'''

# Parent Class
class User:
    def register(self):
        print("Registering user...")

    def login(self):
        print("Logging in...")

# Child Class: Student
class Student(User):
    def student_greet(self):
        print("Hello Student")

# Child Class: Faculty
class Faculty(User):
    def faculty_greet(self):
        print("Hello Faculty")

# Multilevel Inheritance: TempFaculty inherits from Faculty
class TempFaculty(Faculty):
    def tempFaculty_greet(self):
        print("Hello Temp Faculty")


# --- Practice Demonstration ---

# Student object
s1 = Student()
s1.register()        # Access parent method
s1.login()           # Access parent method
s1.student_greet()   # Access child method


# Faculty object
f1 = Faculty()
f1.register()        # Access parent method
f1.login()           # Access parent method
f1.faculty_greet()   # Access child method


# TempFaculty object
t1 = TempFaculty()
t1.register()            # Access parent method
t1.login()               # Access parent method
t1.faculty_greet()       # Access Faculty method
t1.tempFaculty_greet()   # Access TempFaculty method


# Parent object (cannot access child methods)
u1 = User()
u1.register()
u1.login()
# u1.student_greet()   # Error: Parent cannot access child methods
# u1.faculty_greet()   # Error

'''
🔁 Task 3: Method Overriding
👉 Use same User, Student, Faculty
Requirement:
Override greet() method
Parent:
def greet():
    print("Welcome User")
Student:
print("Welcome Student")
Faculty:
print("Welcome Faculty")
🎯 Expected:
student.greet() → Welcome Student
faculty.greet() → Welcome Faculty
'''

# Parent Class
class User: 
    def greet(self):
        print("Welcome User")
# Child Class: Student
class Student(User):
    def greet(self):
        print("Welcome Student")    
# Child Class: Faculty
class Faculty(User):
    def greet(self):
        print("Welcome Faculty")
# Example usage
student = Student()             
faculty = Faculty()
student.greet()  # Output: Welcome Student
faculty.greet()  # Output: Welcome Faculty

'''
🔗 Task 4: Method Chaining
👉 Create class User
Methods:
register()
login()
greet()
Rule:
Each method must return self
🎯 Example:
user = User()

user.login().greet().register()
Expected Output:
logined
enjoy everyone
registered
'''
class User:
    def register(self):
        print("registered")
        return self

    def login(self):
        print("logined")
        return self

    def greet(self):
        print("enjoy everyone")
        return self
    
# Example usage
user = User()   
user.login().greet().register()


'''
🔥 Task 5: Combined Task (Real-Time)
👉 Build a Mini User System
Features:
Encapsulation for user data
Inheritance:
User
Student
Faculty
Method overriding for greet()
Method chaining for:
user.login().greet().register()
Bonus:
Add class variable:
users_count
Increment on each object creation
'''

class User:
    users_count = 0  # Class variable to count users

    def __init__(self):
        self.__user_name = None
        self.__pwd = None
        User.users_count += 1  # Increment user count on each object creation

    def set_user(self, user_name, pwd):
        self.__user_name = user_name
        self.__pwd = pwd

    def get_user(self):
        return self.__user_name

    def register(self):
        print(f"Registering user: {self.__user_name}")
        return self

    def login(self):
        print(f"Logging in: {self.__user_name}")
        return self

    def greet(self):
        print("Welcome User")
        return self
# Child Class: Student
class Student(User):
    def greet(self):
        print("Welcome Student")
        return self
# Child Class: Faculty
class Faculty(User):
    def greet(self):
        print("Welcome Faculty")
        return self
# Example usage
student = Student()
student.set_user("alice", "pass123")
student.login().greet().register()  # Method chaining
faculty = Faculty()
faculty.set_user("prof_bob", "secure456")
faculty.login().greet().register()  # Method chaining
print(f"Total users created: {User.users_count}")  # Output total users



    
