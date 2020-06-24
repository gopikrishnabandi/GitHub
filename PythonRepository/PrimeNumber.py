lower =int(input('Enter the lower range:'))
upper =int(input('Enter the upper range:'))

print("Prime numbers between",lower,"and",upper,"are:")

for num in range(lower,upper + 1):
   # prime numbers are greater than 1
   if num > 1:
       for i in range(2,num):
           if (num % i) == 0:
               break
       else:
           print(num)


#for num in range(1,11)
#1 to 10
#num in 1
#num in 2 and so on
#eg:3
#2>1
#for i in range(2,3)
#2
#2%2 is 0
#break
#print(2)
#2
