#convert europe lift floors to US floors
inp=input('Enter Europe Floor :')
out=int(inp)+1
print('The US floor is',out)
#single quotes or double are fine in python for string
print("The US floor is %d"%out)
#8/4 is 2.0 and not 2
x = 1 + 2 * 3 - 8 / 4
print(x)
x=int(input('Enter a value:'))
if x>10:#will iterate all blocks unlike if elif else blocks sequentially
    print('enetred value is greater than 10')
if x<10:
    print('entered value is less than 10')
#= is an assignment operator, whereas ==  is asking a question
if x==10:
    print('entered value is 10')
if x>=100:
    print('entered value is greater than or equal to 100')
if x<=100:
    print('entered value is less than or equal to 100')
if x!=100:
    print('entered value is not equal to 100')
print('end of if loop')
#avoid tabs in other text editors , as python will think it needs to add a space, no issue with atom
#dont mix tabs and spaces as python cares a lot about indentation, may get errors based on tools u are using, use spaces and not tabs
#range is 0 to 9
for i in range(10):
    print(i)
    #and is the logical operator, & is bitwise
    if i%2==0 and i!=0:
        print(i,'is an even number')
    print('done with',i)
print('done with all')
a=int(input('Enter 1st number:'))
b=int(input('Enter 2nd number:'))
#bitwise and operation
c=a&b
print('bitwise of above 2 numbers is',c)
"""y=int(input('Enter a value:'))
if y>10:
    print('number is greater than 10')
        if y<100: this line is producing an error because even though it is a loop with in a loop, python is expecting you to start at same indentation position as print , because there is no need to start at a differnt position because seeing an if within an if it understands it is a conditional loop , no need for again taking an extra space in the front, hence it will result in an error t
            print('it is less than 100')
        print('end of inner block')
    print('end of outer block')
print('out of all blocks')"""
y=int(input('Enter a value:'))
if y>10:
    print('number is greater than 10')
    if y<100:#will come into this block only if first condition is met in the loop
        print('it is less than 100')
    print('end of inner block')
print('end of outer/all block')#will definitely printed as it is outside the block
z=int(input('enter a number for if else block:'))
#in an if else block once a condition is met the loop exits and comes out , the block is from if till the else i.e, from line 57 to 62, so only block of it is exexuted and it comes out, else is like the catch block, once any of conditions is met , it will execute and come out and print the last statement
if z<2:
    print('small')
elif z<10:
    print('Medium')
else:
    print('large')
print('all done')
