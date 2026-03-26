'''
Task 1: User Info Manager (Functions + Dictionary)
Create a function:
def create_user(name, age, role):
Return user as a dictionary
Store multiple users in a list
Print all users
👉 Add:
Format names using .title()
'''
def create_user(name, age, role):
    user = {
        'name': name.title(),
        'age': age,
        'role': role
    }
    return user 
users = []
users.append(create_user('john doe', 30, 'admin'))
users.append(create_user('jane smith', 25, 'user'))
users.append(create_user('alice johnson', 28, 'editor'))
users.append(create_user('bob brown', 35, 'moderator'))
print(users)

'''
Task 2: Dynamic Calculator (*args)
Create:
def calculate_total(*numbers):
Return sum of all numbers
Accept unlimited inputs
👉 Bonus:
Also return average
'''
def calculate_total(*numbers):
    total = sum(numbers)
    average = total / len(numbers) if numbers else 0
    return total, average
total, average = calculate_total(10, 20, 30, 40)
print(f'Total: {total}, Average: {average}')

'''
Task 3: Keyword Config System (**kwargs)
Create:
def system_config(**settings):
Print all key-value pairs
👉 Example:
mode: debug
version: 1.0
'''
def system_config(**settings):
    for key, value in settings.items():
        print(f'{key}: {value}')
system_config(mode='debug', version='1.0', debug=True)

'''
Task 4: Factorial Service (Recursion)
Create:
def factorial(n):
Handle:
n = 0
negative numbers (show error)
'''
def factorial(n):
    if n < 0:
        return 'Error: Factorial is not defined for negative numbers.'
    elif n == 0:
        return 1
    else:
        return n * factorial(n - 1)
print(factorial(5))  # Output: 120
print(factorial(0))  # Output: 1
print(factorial(-3)) # Output: Error message

'''
Task 5: Memory Optimization (Generator)
Create:
def square_generator(n):
Yield squares instead of storing in list
👉 Compare:
Normal list vs generator (print type)
'''
def square_generator(n):
    for i in range(n):
        yield i ** 2
# Using generator
squares_gen = square_generator(10)
print(type(squares_gen))  # Output: <class 'generator'>
print(list(squares_gen))  # Output: [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
# Using list comprehension
squares_list = [i ** 2 for i in range(10)]
print(type(squares_list))  # Output: <class 'list'>
print(squares_list)  # Output: [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

'''
Task 6: Exception Handling Module
Take input:
numerator
denominator
Handle:
divide by zero
invalid input
👉 Always print:
Program Completed
'''
def divide_numbers(numerator, denominator):
    try:
        result = numerator / denominator
        print(f'Result: {result}')
    except ZeroDivisionError:
        print('Error: Cannot divide by zero.')
    except TypeError:
        print('Error: Invalid input. Please enter numbers.')
    finally:
        print('Program Completed')
divide_numbers(10, 2)  # Valid input
divide_numbers(10, 0)  # Divide by zero
divide_numbers(10, 'a')  # Invalid input

'''
 Task 7: File Handling
Create file: team_data.txt
Write user details into file
Read and display content
👉 Bonus:
Check if file is closed
'''
def write_to_file(filename, data):
    with open(filename, 'w') as file:
        for user in data:
            file.write(f"{user['name']}, {user['age']}, {user['role']}\n")
def read_from_file(filename):
    with open(filename, 'r') as file:
        content = file.read()
        print(content)
        print(f'File closed: {file.closed}')
users = [
    {'name': 'John Doe', 'age': 30, 'role': 'admin'},
    {'name': 'Jane Smith', 'age': 25, 'role': 'user'},
    {'name': 'Alice Johnson', 'age': 28, 'role': 'editor'},
    {'name': 'Bob Brown', 'age': 35, 'role': 'moderator'}
]   
write_to_file('team_data.txt', users)
read_from_file('team_data.txt')




