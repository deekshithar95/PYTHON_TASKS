# Bitwise Operator Tasks (1–8)
'''
1.
Create two variables a = 10 and b = 6.
Print the result of a & b.
'''
a = 10
b = 6
print(a & b)

'''
2.
Create two variables x = 12 and y = 5.
Print the result of x | y.
'''
x = 12
y = 5
print(x | y)

'''
3.
Create a variable num = 8.
Print the result of ~num.
'''
num = 8
print(~num)

'''
4.
Create two variables a = 15 and b = 9.
Print the result of a ^ b.
'''
a = 15
b = 9
print(a ^ b)

'''
5.
Create a variable num = 7.
Perform left shift by 2 and print the result.
'''
num = 7
print(num << 2)

'''
6.
Create a variable num = 20.
Perform right shift by 1 and print the result.
'''
num = 20
print(num >> 1)

'''
7.
Take two numbers from user input and print AND result.
'''
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
print(num1 & num2)

'''
8.
Take two numbers from user input and print XOR result.
'''
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
print(num1 ^ num2)


# String Tasks (9–14)
'''
9.
Create a string "hi" and print it 4 times using replication.
'''
string = "hi"
print(string * 4)

'''
10.
Create a string "python" and print it 3 times.
'''
string = "python"
print(string * 3)

'''
11.
Create two strings "super" and "man" and combine them using + operator.
'''
string1 = "super"
string2 = "man"
print(string1 + string2)

'''
12.
Create three strings "hello", " ", "world" and print "hello world".
'''
string1 = "hello"
string2 = " "
string3 = "world"
print(string1 + string2 + string3)

'''
13.
Take a name from user input and print it 5 times.
'''
name = input("Enter your name: ")
print(name * 5)

'''
14.
Take two strings from user input and concatenate them.
'''
string1 = input("Enter first string: ")
string2 = input("Enter second string: ")
print(string1 + string2)


# Input & Type Casting Tasks (15–20)
'''
15.
Take a name from user input and print its data type.
'''
name = input("Enter your name: ")
print(type(name))

'''
16.
Take age from user input and convert it into integer.
'''
age = input("Enter your age: ")
age = int(age)
print(age)

'''
17.
Take two numbers from user input and print their sum.
'''
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
print(num1 + num2)

'''
18.
Take two marks from user input and print their average.
'''
mark1 = float(input("Enter first mark: "))
mark2 = float(input("Enter second mark: "))
average = (mark1 + mark2) / 2
print(average)

'''
19.
Take two numbers from user input and print
3*a*2 + b - 2.
'''
a = float(input("Enter value for a: "))
b = float(input("Enter value for b: "))
result = 3 * a * 2 + b - 2
print(result)

'''
20.
Take a number from user input and print its data type before and after type casting.
'''
num = input("Enter a number: ")
print("Data type before type casting:", type(num))
num = float(num)
print("Data type after type casting:", type(num))


# Unit Digit Tasks (21–25)
'''
21.
Take a number as string input and print the last digit.
'''
num_str = input("Enter a number: ")
print("Last digit:", num_str[len(num_str)-1])

'''
22.
Take a number and print the unit digit using % operator.
'''
num = int(input("Enter a number: "))
print("Unit digit:", num % 10)

'''
23.
Take a number and remove the last digit using // operator.
'''
num = int(input("Enter a number: "))
print("Number after removing last digit:", num // 10)

'''
24.
Take a number and print the second last digit.
'''
num = int(input("Enter a number: "))
second_last_digit = (num // 10) % 10
print("Second last digit:", second_last_digit)

'''
25.
Take a 5 digit number and print its last digit.
'''
num = int(input("Enter a 5 digit number: "))
print("Last digit:", num % 10)


# If Statement Tasks (26–30)
'''
26.
Create a program that checks if 10 ≥ 5 and prints a message.
'''
if 10 >= 5:
    print("10 is greater than or equal to 5.")

'''
27.
Take a number from user input and check if it is greater than 50.
'''
num = float(input("Enter a number: "))
if num > 50:
    print("The number is greater than 50.")

'''
28.
Take age from user input and check if age ≥ 18.
'''
age = int(input("Enter your age: "))
if age >= 18:
    print("You are eligible to vote.")

'''
29.
Take a number and check if it is greater than 100.
'''
num = float(input("Enter a number: "))
if num > 100:
    print("The number is greater than 100.")

'''
30.
Take a number and check if number ≥ 0.
'''
num = float(input("Enter a number: "))
if num >= 0:
    print("The number is non-negative.")


# If-Else Tasks (31–34)
'''
31.
Take a number and check if it is even or odd.
'''
num = int(input("Enter a number: "))
if num % 2 == 0:
    print("The number is even.")
else:
    print("The number is odd.")

'''
32.
Take marks from user input and check if pass or fail (pass ≥ 35).
'''
marks = float(input("Enter your marks: "))
if marks >= 35:
    print("You have passed.")
else:
    print("You have failed.")

'''    
33.
Take a number and check if it is positive or negative.
'''
num = float(input("Enter a number: "))
if num > 0:
    print("The number is positive.")
elif num < 0:
    print("The number is negative.")
else:
    print("The number is zero.")

'''
34.
Take a number and check if it is greater than 10 or not.
'''
num = float(input("Enter a number: "))
if num > 10:
    print("The number is greater than 10.")
else:
    print("The number is not greater than 10.")


# Nested If Tasks (35–37)
'''
35.
Create a program for job eligibility:
Conditions
Age ≥ 18
Height ≥ 160
Weight ≥ 60
Print selected or rejected.
'''
age = int(input("Enter your age: "))
height = float(input("Enter your height in cm: "))
weight = float(input("Enter your weight in kg: "))
if age >= 18:
    if height >= 160:
        if weight >= 60:
            print("Selected")
        else:
            print("Rejected due to weight")
    else:
        print("Rejected due to height")
else:
    print("Rejected due to age")

'''
36.
Create a college admission program:
Conditions
Marks ≥ 60
Age ≥ 17
'''
marks = float(input("Enter your marks: "))
age = int(input("Enter your age: "))
if marks >= 60:
    if age >= 17:
        print("Admission granted")
    else:
        print("Admission rejected due to age")
else:
    print("Admission rejected due to marks")

'''
37.
Create a sports selection program:
Conditions
Age ≥ 16
Height ≥ 150
Weight ≥ 50
''' 
age = int(input("Enter your age: "))
height = float(input("Enter your height in cm: "))
weight = float(input("Enter your weight in kg: "))
if age >= 16:
    if height >= 150:
        if weight >= 50:
            print("Selected for sports")
        else:
            print("Rejected due to weight")
    else:
        print("Rejected due to height")
else:
    print("Rejected due to age")


# Match Statement Tasks (38–40)
'''
38.
Take a number (1-7) and print day name using match.
'''
day_num = int(input("Enter a number (1-7): "))
match day_num:
    case 1:
        print("Monday")
    case 2:
        print("Tuesday")
    case 3:
        print("Wednesday")
    case 4:
        print("Thursday")
    case 5:
        print("Friday")
    case 6:
        print("Saturday")
    case 7:
        print("Sunday")
    case _:
        print("Invalid input. Please enter a number between 1 and 7.")

'''
39.
Take a number (1-3) and print:
1 → Red
2 → Blue
3 → Green
'''
color_num = int(input("Enter a number (1-3): "))
match color_num:
    case 1:
        print("Red")
    case 2:
        print("Blue")
    case 3:
        print("Green")
    case _:
        print("Invalid input. Please enter a number between 1 and 3.")

'''
40.
Take a number (1-4) and print:
1 → Apple
2 → Mango
3 → Orange
4 → Banana
'''   
fruit_num = int(input("Enter a number (1-4): "))
match fruit_num:
    case 1:
        print("Apple")
    case 2:
        print("Mango")
    case 3:
        print("Orange")
    case 4:
        print("Banana")
    case _:
        print("Invalid input. Please enter a number between 1 and 4.")