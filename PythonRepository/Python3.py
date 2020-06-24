x=int(input('enter a number in if block:'))
if x<20:
    print('less than 20')
if x<10:
    print('less than 10')
else:
    print('default catch block 1')
y=int(input('enter a second number in if elif block:'))
if y<20:
    print('less than 20')
#the difference in multiple ifs and if elif block is in if elif blocks once a condition is met , other blocks are not executed, unlike the above if bloocks, try with number 9 for unde
elif y<10:
    print('less than 10')
else:
    print('default catch block 2')
if y<2:
    print('less than 2')
elif y>=2:
    print('greater than or equal to 2')
    #this else will never be executed , as y is either <2 , or >=2
else:
    print('something else')
y=int(input('rewrite y again:'))
if y<2:
    print('good')
else:
    print('bad')
print('value of y is',y)
