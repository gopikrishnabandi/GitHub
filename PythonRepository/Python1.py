#Sequential program lines folow
x=int(input("Enter the number: "))#input function takes a string , explicit conversion to int
#int to str coversion using format key word, format only converts something to string, not vice versa
print("The number entered is:"+format(x))
print('the numbers entered is',x)#also valid way to use print function
#using the traditional % operator
print("The number entered is:%d" %x)#for this syntax no , in between
#x is a variable that is allocated a piece of memory
x=x**3#this is assignment with expression, RHS is  firts calculated with the value of x that is there currently and is assigned as a new value for xx
print(x)
#print with single quotes is same as print with double
print('pora')
print("puski")
x=x*3
print (x)
#if else block example, the final else is the default catch,conditional programming
if x>375:
    print("Number enetred is greater than 5")
elif x<375:
    print("number entered is less than 5")
else:
    print('number enetred is 5')
    #testing a while block,iterative/recurring
while x>300:
    x=x-100
    print (x)
print(98.6)
print('98.6+23.4')#This prints as a string
#variables are case sensitive
x=2 #assignment statement
X=3
#Variable names can start with letters or underscores , but avoid underscores as python uses it for a diff purpose
_variable=20
print(_variable)
#variablenames cannot start with number, uncomment below lines to see error
#23spam=45
#print(23spam)
#variable below is fine numbers or underscores followed by letters or underscores
spam23=100
#spam23.2 is not valid variable name, cannot use symbols which are other than numbers or characters
#Different:=2 is not valid as : is not a symbol that python expects in a Variable name
#use Mnemonic method to name variable names , choose variable names based on what we are using it for
rateperday=10
noofdays=5
cost=rateperday*noofdays
print("hotel cost is %d" %cost)
#+is add, - add is subtract,* is multiplication, / is division , ** is raised to the power/exponentitaion, % is reminder
x=1+2*3-4/5**6
print(x)
#first is paranthesis or bracket, next is exponentitation,Multiplication division and reminder are equal, addition and subtraction left to right
#so above line will become x=1+(2*3)-(4/(5**6)) i.e x=1+6-(4/15625)=6.999744
a=1+2
b="hello"+" there" #string concatenation using plus operator (concatenates/adds same data types) , can use single or double quotes
c='hello'+' there'
print(a)
print(b)
print(c)
#d=c+1 will return an error, cannot concatenate integer and string , program will stop quits at that line
print(type(c)) #type returns the type of the variable or constants
print(float(99)+1) #converting 99 to float, so resultant will be float
print(9/2)#used to be 4 in python 2, now it is 4.5
print(10/2)#is 5.0
#we can convert strings to int or float if it has only numbers
str='123'
print(type(str))
ival1=int(str)
ival2=float(str)
print(ival1)
print(ival2)
#str='abc' cannot be converted to int, will produce an error as it has no digits
userdata=input('what is your name ?')
#Input is used to take user input, python pauses and reads data from the user, input function returns a string, so user datavarable is returned a string
print('name is '+userdata)#+is concatenate operator , print(userdata) if we just want to print without senetence
print('welcome',userdata)#one more way to use print function to join different strings and variables. The , operartor adds a space
print('welcome',userdata,ival1)#we can add in a int as well
print ('welcome',userdata,ival1+ival2)#adding two variables and printing
"""please note that print when given even with space or without space is not making
any difference, these comments unlike above which are given in triple quotes are called
documentation comments, but as a general practice space are not preferred"""
