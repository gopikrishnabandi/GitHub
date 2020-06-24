#Implementing a queue using a list 
#This is Not ideal, Performance is slow,so we should Use deque class from collections instead, but lets first try using a list
#queue-FIFO, WITH List implemnetation O(n) is the complexity whereas with Dequeue it is O(1)
#Dequeue is FIFO , Enqueue is FILO(First In last Out)
q=[]
size=int(input('Enter your size of queue:'))
for i in range(size):
    q.append(int(input('Enter Next Value:')))
print(q)
no_of_elements=int(input('Enter Number of elements to be removed:'))
for i in range(no_of_elements):
    q.pop(0)
print(q)

#implementation using dequeue
from collections import deque
q1=deque()
size1=int(input('Enter size of queue:'))
#lets try with whiel instead of for
counter=0
while counter<size1:
    q1.append(int(input('Enter Next Value:')))
    counter+=1
print(q1)
no_of_elements_1=int(input('Enter No of Elements to be removed:'))
for i in range(no_of_elements_1):
    q1.popleft()
print(q1)

