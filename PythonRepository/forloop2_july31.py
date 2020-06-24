#finding largest number
i=-1#will not work for negative numbers, see below , we should use none
print('before implementation it is',i)
numbers=[2,3,4,75,8]
for number in numbers:
    if number>i:
        i=number
        #we can write a print to know value at each step,print(i,number)
print('after logic implementation it is',i)
#finding a small value
smallest=None#flag value
print('before implementation it is',smallest)
for number in [1,51,26,9,64,8]:
    if smallest is None:#only first time value will be none , after which smallest becomes 9 after which this condition will always be false
#is and is not are logical opeartors which return treu or false, they are same as == and != but more powerful than them
        smallest=number
    elif number<smallest:
        smallest=number
        print(smallest,number)#we can write a print to know value at each step,print(smallest,number)
print('after logic implementation it is',smallest)
#keeping a counter , in this below count number of things
count=0
for thing in [12,34,5,61,23]:
    count=count+1
print('counter value is ',count)
#totaling
total=0
count=0
for i in [20,30,40,70,100]:
    count=count+1
    total=total+i
    print('Running total in round',count,'is',total)
    print('Running average in round',count,'is',total/count)
print('Final Total is',total)
print('Final average is',total/count)
#filtering and searching using boolean
value=False
for j in [2,100,50,4,5,72,81,9]:
    if j>20:#first this condition is executed for first value in the list and  control goes to next if with same value
        print(j,'is a large number')
    if j==72:
        value=True
        #can use break to come out of the loop
        #break
    print(value,j)#if this intended then the value will be only printed only when it is 72 i.e., if condition is met only it goes in to the loop, else even for false values it will be printed
print('Done')
