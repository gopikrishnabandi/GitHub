#comparision operators
print(10<3)
print(10>=3)
print(10=="10")
print(10!="10")
print("bag">"apple")
print("bag">"Bag")
print(ord("b"))#98
print(ord("B"))#66
#conditional operators
temp=int(input('Enter temperature:'))
if temp>30:
    print('Hot Day')
elif temp<30 and temp>25:
    print('Perfect Day')
else:#if none of the other conditions are true
    print('cooler day')
print('Have a good day')
#ternary operator
age=int(input('Enter age:'))
message="Eligible" if age>=21 else "not eligible"
print(message)
#logical operators : And, Or , Not
high_income=True
good_credit=True
if high_income and good_credit:
    print('credit eligible')
else:
    print('credit not eligible')
a=int(input('Enter Loan amount Required:'))
b=int(input('Enter asset prood value:'))
if b>a or a<=10000:
    print('Loan will be sanctioned')
elif a>b and b<10000:
    print('Asset value less to grant loan')
else:
    print('Contact the manager for details')
s=input('Enter if student or not(Y/N):')
if s not in 'Y':
    print('Proceed to front desk')
else:
    print('Proceed to seminar hall')
employee=True
Contract=False
FixPay=True
if (employee or FixPay) and not Contract:
    print('Add as employee record in table')
else:
    print('Add to temporary table')
#short circuiting in python, python interpreter stops evaluation for an And expression after it enecounters a False
#similarly for Or opeartor, it stops when it fisrt encounters True

#Chaining comparision, similar to math style, see if below
age=int(input('Enter age to check job eligibility:'))
if 18<=age<65:#other wise it should have been if age>=18 and age<65:
    print('eligible')
#for loop
for i in range(1,10,2):
    print('attempt',i,i*'.')
fruit='apple'
for i in fruit:
    print(i)
fruits=['apple','Mango','Lemon']
for i in fruits:
    print(i)
#for else loop
a=int(input('Enter an integer'))
for i in range(1):
    print('Entering loop with input value as ',a)
    if(a==2):
        print(a,'is 2')
        break
else:
    print(a,'is not 2')
#Nested loops
for x in range(3):
    for y in range(3):
        print(f'({x}, {y})')
#iterables
print(type(range(5)))#class range which is a complex type
#range is an iterable , we can use to iterate over it and can be used in for loops
#eg for x in range(5):
#strings are also iterable
str='Python'
for x in str:
    print(x)
#List is also an iterable
list = [1,2,3,4]
for i in list:
    print(i)
# we can create our own custom object later which is an iterable
#eg: for item in shopping_cart: here shopping_cart is an iterable

#while loops(indefinite , number of iterations not known at the start)
j=3
while j>0:
    print('j is ',j)
    j=j-1
command=''
while command.lower()!='quit':#lower will convert any to small case, so QUIT or Quit anything will be converted
    command=input('>enter an expression to evaluate, quit to exit')
    print(eval(command))
#infinite loops
j=3
while j>=0:
    print('printing 6/j ',6/j)
    break#to mitigate infinite loop
while True:#always true , will run until we exit with break, without which it will be an infinite loop
    command=int(input('Enter value:'))
    print(command,'is entered value',',Enter 0 to quit')
    if command==0:
        break#used to exit the loop 
#Exercise to print even numbers b/w 1 to 10 and a message of count
count=0
for i in range(1,10):
    if i%2==0:
        count += 1
        print(i)
print(f'we have {count} even numbers')
