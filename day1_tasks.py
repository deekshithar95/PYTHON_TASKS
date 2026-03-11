'''Task 1 - Print Formatting
Print the following output using sep and end.
Expected Output:
Hello World Welcome Python
Laptop | Mouse | Keyboard
'''
print("Hello World", end=" ")
print("Welcome Python")

print("Laptop","Mouse","Keyboard", sep=" | ")


'''
Task 2 - Variables
Create variables:
name = "Ravi"
age = 22
city = "Chennai"
Print them in one line separated by -
Example output:
Ravi-22-Chennai
'''
name = "Ravi"
age = 22
city = "Chennai"
print(name,age,city,sep="-")


'''
Task 3 - Multiple Assignment
Assign values using multiple assignment
name = "Meena"
age = 20
student = True
Print the output.
'''
(name,age,student) = ("Meena",20, True)
print(name,age,student)


'''
Task 4 - Indexing
Given:
word = "Python"
Print:
First letter
Third letter
Last letter
'''
word = "Python"
print(word[0])
print(word[2])
print(word[-1])


'''
Task 5 - Arithmetic Operators
Calculate and print:
25 + 10
50 - 20
8 * 5
100 / 10
10 % 3
2 ** 4
20 // 3
'''
print(25 + 10)    # output:35
print(50 - 20)    # output:30
print(8 * 5)      # output:40
print(100 / 10)   # output:10.0
print(10 % 3)     # output:1
print(2 ** 4)     # output:16
print(20 // 3)    # output:6


'''
Task 6  BODMAS Expression
Find the result:
print(3 + 2 * 5 ** 2)
Ask the team to predict the answer first, then run the code.
'''
# answer : 53
print(3 + 2 * 5 ** 2)


'''
Task 7 - Assignment Operator
num = 50
num += 25
Print the final value.
Then try:
num = 100
num /= 10
Print the result.
'''
num = 50
num += 25
print(num)  #output:75

num = 100
num /= 10
print(num) #output:10.0


'''
Task 8 - Comparison Operators
Print the result of the following:
10 > 5
20 < 15
5 == 5
10 != 8
7 >= 7
6 <= 2
'''
print(10 > 5)      #output: True
print(20 < 15)     #output: False
print(5 == 5)      #output: True
print(10 != 8)     #output: True
print(7 >= 7)      #output: True
print(6 <= 2)      #output: False


'''
Task 9 - String Comparison
a = "apple"
b = "Apple"
Check:
print(a == b)
Ask the team why the result is False.
'''
a = "apple"
b = "Apple"
print(a == b) # output: False
# Reason: The result is False because Python string comparison is case-sensitive, so "apple" and "Apple" are considered different.


'''
Task 10 - Logical Operators
Find the output:
print(10 > 5 and 5 == 5)
print(5 > 10 or 10 == 10)
print(not(5 > 2))
'''
print(10 > 5 and 5 == 5)    #output: True
print(5 > 10 or 10 == 10)   #output: True
print(not(5 > 2))           #output: False


'''
Task 11 - Membership Operator
numbers = [10,20,30,40,50]
Check:
20 in numbers
60 in numbers
30 not in numbers
'''
numbers = [10,20,30,40,50]
print(20 in numbers)        #output: True
print(60 in numbers)        #output: False
print(30 not in numbers)    #output: False


'''
Task 12 - Swap Variables
a = 10
b = 20
Swap the values using single line swap
Expected Output:
a = 20
b = 10
'''
a = 10
b = 20
a,b = b, a
print("a =", a)   #output: 20
print("b =", b)   #output: 10


'''
Task 13 - Bitwise XOR
a = 6
b = 3
Print:
a ^ b
Ask them to check the binary calculation.
'''
a = 6
b = 3
print(a ^ b)  #output: 5

# binary calculation
# a = 6 --> 110
# b = 3 --> 011
# ----------------
#XOR(^)  =  101 (Binary Value)
#        =   5  (Decimal Value)
