'''
Section 1: Loop Basics (1-10)
Print numbers from 1 to 50 using for loop
Print even numbers from 1 to 100
Print odd numbers from 1 to 100
Print multiplication table of 7
Find sum of numbers from 1 to 100
Print numbers in reverse from 50 to 1
Count how many numbers are divisible by 3 (1-100)
Print squares of numbers from 1 to 10
Print cube of first 10 numbers
Take input n, print numbers from 1 to n
'''
# 1. Print numbers from 1 to 50 using for loop
for i in range(1, 51):
    print(i)
# 2. Print even numbers from 1 to 100
for i in range(1, 101):
    if i % 2 == 0:
        print(i)
# 3. Print odd numbers from 1 to 100
for i in range(1, 101):
    if i % 2 != 0:
        print(i)
# 4. Print multiplication table of 7
for i in range(1, 11):
    print(f"7 x {i} = {7 * i}") 
# 5. Find sum of numbers from 1 to 100
total_sum = 0   
for i in range(1, 101):
    total_sum += i
print(f"Sum of numbers from 1 to 100 is: {total_sum}")
# 6. Print numbers in reverse from 50 to 1
for i in range(50, 0, -1):
    print(i)    
# 7. Count how many numbers are divisible by 3 (1-100)
count_divisible_by_3 = 0
for i in range(1, 101):
    if i % 3 == 0:
        count_divisible_by_3 += 1
print(f"Count of numbers divisible by 3 (1-100): {count_divisible_by_3}")
# 8. Print squares of numbers from 1 to 10
for i in range(1, 11):
    print(f"{i}^2 = {i**2}")
# 9. Print cube of first 10 numbers
for i in range(1, 11):
    print(f"{i}^3 = {i**3}")
# 10. Take input n, print numbers from 1 to n
n = int(input("Enter a number n: "))
for i in range(1, n + 1):
    print(i)

'''
Section 2: While Loop (11-15)
Print numbers from 1 to 20 using while
Find factorial of a number using while
Reverse a number using while
Count digits in a number
Keep asking input until user enters "stop"
'''
# 11. Print numbers from 1 to 20 using while
i = 1
while i <= 20:
    print(i)
    i += 1
# 12. Find factorial of a number using while    
num = int(input("Enter a number to find its factorial: "))
factorial = 1
while num > 0:
    factorial *= num
    num -= 1
print(f"Factorial: {factorial}")
# 13. Reverse a number using while
num = int(input("Enter a number to reverse: "))
reverse = 0
while num > 0:
    digit = num % 10
    reverse = reverse * 10 + digit
    num //= 10
print(f"Reversed number: {reverse}")
# 14. Count digits in a number
num = int(input("Enter a number to count its digits: "))
count = 0
while num > 0:
    num //= 10
    count += 1
print(f"Number of digits: {count}")
# 15. Keep asking input until user enters "stop"
while True:
    user_input = input("Enter something (type 'stop' to end): ")
    if user_input.lower() == "stop":
        break

'''
Section 3: Nested Loop (16-20)
Print pattern:
*
**
***
****
Print pattern:
1
12
123
1234
Print multiplication table (1 to 5) using nested loop
Print:
A B C
A B C
A B C
Print:
1 2 3
4 5 6
7 8 9
'''
# 16. Print pattern:
for i in range(1, 5):
    for j in range(i):
        print("*", end="")
    print()
# 17. Print pattern:
for i in range(1, 5):
    for j in range(1, i + 1):
        print(j, end="")
    print()
# 18. Print multiplication table (1 to 5) using nested loop
for i in range(1, 6):
    for j in range(1, 6):
        print(f"{i} x {j} = {i * j}")
    print()  # Add a newline after each table
# 19. Print:
for i in range(3):
    for j in ["A", "B", "C"]:
        print(j, end=" ")
    print()
# 20. Print:
num = 1
for i in range(1, 4):
    for j in range(1, 4):
        print(num, end=" ")
        num += 1
    print()

'''
Section 4: String Basics (21-25)
Count total characters in a string
Count vowels in a string
Count consonants in a string
Reverse a string using loop
Check if string is palindrome
'''
# 21. Count total characters in a string
input_string = input("Enter a string: ")
character_count = 0
for char in input_string:
    character_count += 1
print(f"Total characters: {character_count}")
# 22. Count vowels in a string
input_string = input("Enter a string: ")
vowel_count = 0
vowels = "aeiouAEIOU"
for char in input_string:
    if char in vowels:
        vowel_count += 1
print(f"Number of vowels: {vowel_count}")
# 23. Count consonants in a string
input_string = input("Enter a string: ")
consonant_count = 0
vowels = "aeiouAEIOU"
for char in input_string:
    if char.isalpha() and char not in vowels:
        consonant_count += 1
print(f"Number of consonants: {consonant_count}")
# 24. Reverse a string using loop
input_string = input("Enter a string to reverse: ")
reversed_string = ""
for char in input_string:
    reversed_string = char + reversed_string
print(f"Reversed string: {reversed_string}")
# 25. Check if string is palindrome
input_string = input("Enter a string to check if it's a palindrome: ")
reversed_string = ""
for char in input_string:
    reversed_string = char + reversed_string
if input_string == reversed_string:
    print("The string is a palindrome.")
else:
    print("The string is not a palindrome.")

'''
Section 5: String Slicing (26–30)
Print first 5 characters of a string
Print last 3 characters
Print string in reverse using slicing
Print every 2nd character
Remove first and last character from string
'''
# 26. Print first 5 characters of a string
input_string = input("Enter a string: ")
print(f"First 5 characters: {input_string[:5]}")
# 27. Print last 3 characters
input_string = input("Enter a string: ")
print(f"Last 3 characters: {input_string[-3:]}")
# 28. Print string in reverse using slicing
input_string = input("Enter a string: ")
print(f"Reversed string: {input_string[::-1]}")
# 29. Print every 2nd character
input_string = input("Enter a string: ")
print(f"Every 2nd character: {input_string[::2]}")
# 30. Remove first and last character from string
input_string = input("Enter a string: ")
if len(input_string) > 2:
    modified_string = input_string[1:-1]
    print(f"String after removing first and last character: {modified_string}")
else:
    print("String is too short to remove characters.")

'''
Section 6: List Basics (31-35)
Create a list of 5 numbers and print sum
Find maximum value in list
Find minimum value in list
Count total elements in list
Check if element exists in list
'''
# 31. Create a list of 5 numbers and print sum
numbers = [10, 20, 30, 40, 50]
total_sum = 0
for num in numbers:
    total_sum += num
print(f"Sum of numbers: {total_sum}")
# 32. Find maximum value in list
numbers = [10, 20, 30, 40, 50]
max_value = numbers[0]
for num in numbers:
    if num > max_value:
        max_value = num
print(f"Maximum value: {max_value}")
# 33. Find minimum value in list
numbers = [10, 20, 30, 40, 50]
min_value = numbers[0]
for num in numbers:
    if num < min_value:
        min_value = num
print(f"Minimum value: {min_value}")
# 34. Count total elements in list
numbers = [10, 20, 30, 40, 50]
count = 0
for num in numbers:
    count += 1
print(f"Total elements in list: {count}")
# 35. Check if element exists in list
numbers = [10, 20, 30, 40, 50]
element = int(input("Enter a number to check if it exists in the list: "))
exists = False
for num in numbers:
    if num == element:
        exists = True
        break
if exists:
    print(f"{element} exists in the list.")
else:
    print(f"{element} does not exist in the list.")

'''
Section 7: List Operations (36–40)
Add 3 elements using append()
Insert element at specific index
Remove element using remove()
Reverse list without using .reverse()
Sort list without using .sort()
'''
# 36. Add 3 elements using append()
my_list = []
my_list.append(10)
my_list.append(20)
my_list.append(30)
print(f"List after adding elements: {my_list}")
# 37. Insert element at specific index
my_list = [10, 20, 30]
my_list.insert(1, 15)  # Insert 15 at index 1
print(f"List after insertion: {my_list}")
# 38. Remove element using remove()
my_list = [10, 15, 20, 30]
my_list.remove(15)  # Remove element 15
print(f"List after removal: {my_list}")
# 39. Reverse list without using .reverse()
my_list = [10, 20, 30]
reversed_list = []
for i in range(len(my_list) - 1, -1, -1):
    reversed_list.append(my_list[i])
print(f"Reversed list: {reversed_list}")
# 40. Sort list without using .sort()
my_list = [30, 10, 20]
sorted_list = []
while my_list:
    min_value = my_list[0]
    for num in my_list:
        if num < min_value:
            min_value = num
    sorted_list.append(min_value)
    my_list.remove(min_value)
print(f"Sorted list: {sorted_list}")
