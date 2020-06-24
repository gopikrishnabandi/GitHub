

#better and proper code samples
str1=input('Enter a number:')
try:
    str1=int(str1)
    if str1>0:
        print('entered value is positive')
    elif str1<0:
        print('entered value is negative')
except:
    str1=str(str1)
    print(str1)


#One more
try:
    number=int(input("Enter a number"))
    if number>0:
        print('Entered number is positive')
    elif number<0:
        print('Enetred number is negative')
    else:
        print('number entered is 0')
except:
    print('entered value is a string and not a number')


#next code
rawstr=input('Enter a number')
try:
    ival=int(rawstr)
except:
    ival=-1
if ival>0:
    print('Nice work')
else:
    print('Not a Number')
