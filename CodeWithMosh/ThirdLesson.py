# comparision opeartors
print(10 == "10")
print(10 != "10")
print("bag" == "BAG")
print("bag" > "BAG")
print("bag" > "apple")
print(ord("b"))  # order of letter b
print(ord("a"))
print(ord("A"))
# Conditional statements
print("Enter CGPA:")
cgpa = int(input())
if cgpa > 8:
    print('You have admission, please contact front office')
elif cgpa > 7:
    print('Please submit additional docs in portal')
else:
    print('CGPA less for admission')
print('Thanks for visiting our website')
# Ternary Operator
print('Enter Inventory of the phone:')
inventory = int(input())
phone_price = 500 if inventory > 1000 else 700  # ternary operation
print('Phone price is', phone_price)
# logical operators
# and, or, not
bill_prompt_payment = True
credit_score_high = True
student = True
if (bill_prompt_payment or credit_score_high) and not student:
    print('Phone can be issued')
else:
    print('not eligible for phone ')
# short circuit evaluation
# python interpreter in a multiple "And" expression stops as soo a sit encounters a "False"
# similarly for an "or" it stops when it enecounters a "True"
# This is called short circuiting

# Chaining comparision operators
age = 25
print('age is 25')
# similar to math we use, and is called chaining else we should have written this as if age>=18 and age<65:
if 25 <= age < 65:
    print('Eligible for parliament')


# for loops
for i in range(10):
    print(i, i*'*')

for number in range(1, 10, 2):
    print(number)

# For else
# https://intoli.com/blog/for-else-in-python/
# the code in the else block runs only if the loop completes without encountering a break statement.
delivery_status = False
for i in range(1, 3):
    print('Delivery Attempt', i)
    if delivery_status:
        break
else:
    print('Failed to deliver')


delivery_status = True
for i in range(1, 3):
    print('Delivery Attempt', i)
    if delivery_status:
        print('Delivered')
        break
else:
    print('Failed to deliver')


# Nested loops, we can use coordintes example also
for students in range(1, 6):
    for cgpa in range(3, 5):
        print(f'class student {students} cgpa is {cgpa} ')

 # Iterables
 # apart from int, string and boolean primitive types we have complex types like range, lists
print(type(range(5)))  # rage object which is an iterable, we can itearte over it
# String is an iterable, so is a List
for letters in "Python":
    print(letters)
for numbers in [1, 2, 3, 4, 5]:
    print(numbers)

# While loops
i = 50
while i > 1:
    print(i)
    i //= 2

print('Enter Command')
command = ""
while command.lower() != 'quit':
    command = input()
    print('echo', command)


# Infinite Loops
# This is same as above, should have a break to come out of it
print('Enter Command')
while True:
    command = input()
    print('echo', command)
    if command.lower() == 'quit':
        break

# Exercise
count = 0
for i in range(1, 10):
    if i % 2 == 0:
        count += 1
        print(i)
print('Count is', count)
