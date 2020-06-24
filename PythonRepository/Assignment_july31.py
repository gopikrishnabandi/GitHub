total=0
count=0
smallest=None
largest=None
while True:
    number=input('Enter a number:')
    if number=='Done':
        break
    else:
        try:
            num=int(number)
            count=count+1
            total=total+num
            if smallest is None:
                smallest=num
            elif num<smallest:
                smallest=num
            if largest is None:
                largest=num
            elif num>largest:
                largest=num
        except:
            print('Invalid input')
            continue
print('smallest number is',smallest)
print('largest number is',largest)
print('total is',total)
print('average is',total/count)
