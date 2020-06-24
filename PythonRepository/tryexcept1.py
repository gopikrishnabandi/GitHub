#str1 alone is not valid declaration, below is the way to declare
'''str1=''#global variable
#Try except is used to mitigate potential errors with a way out , which otherwise would end up in a traceback
try:
    str1=int(input('Enter a number:'))
    #if there is an error/traceback here , immediately control will move to except bloc and will not come back from there again to continute next statements in try block
    print('try block is completed')
except:
    str1='string'
    try:
        if str1>0:#will throw error if string is entered
            print('entered value is positive')
        elif str1<0:
            print('entered value is negative')
    except:
        print(str1,'is eneterted which is a string')'''
try:
    str1=int(input('enter age of india PM:'))
except:
    str1=65
print(str1)
