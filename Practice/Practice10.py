import numpy as np
import time

def test_run():
    nd1=np.array([1,2,3])
    nd2=np.array([(1,2,3),(3,4,5)])
    print(nd1)#This will print a nd array and not a list
    print(nd2)
    #create an empty array
    nd3=np.empty(5)
    nd4=np.empty((5,4))
    #when you print, it is supposed to be empty, but it will print whataever values are there in the computers memory
    print(nd3)
    print(nd4)
    #Creating array of ones
    print(np.ones((3,4),dtype=int))
    #creating array of zeros
    print(np.zeros((5,4),dtype=int))
    #generate random values btween 0.0 and 1.0 (1.0 exclusive)
    print(np.random.random(5))
    print(np.random.random((5,4)))
    #with rand no need to give a tuple
    print(np.random.rand(5,4))
    #sample numbers from a normal distribution, a normal distribution is a graph with mean 0 and standard devaiation 1
    print(np.random.normal(size=(2,3))) #mean =0 , sd=1
    print(np.random.normal(50,10,size=(2,3))) #say we want to generate array with Mean value as 50 and Standard deviation 10
    print(np.random.randint(0,10,size=5))#1d array between 0 and 10 , with 5 elemsnts
    print(np.random.randint(0,10,size=(3,3)))#numbers can be repeated
    #Getting shape of an array
    a=np.random.random((5,4))
    print(a.shape)#returns tuple with no of rows and no of columns
    print(a.shape[0]) #No of rows
    print(a.shape[1]) #No of columns
    print(len(a.shape))#no of dimensions of the array
    print(a.size)#No of elements in array 5*4,size and shape  useful for iterating
    print(a.dtype)#data type of the array
    #Operations on ndarray
    np.random.seed(144848)#This is used so that random numbers always generated are the same
    b=np.random.randint(0,10,size=(3,3))
    print("Array:\n",b)
    #sum of elements
    print("sum of elements in array :",b.sum())
    #Sum along direction, i.e., along columns
    print("Sum of each column \n",b.sum(axis=0))
    #sum along rows
    print("sum of each row \n",b.sum(axis=1))
    #Minimum , Maximum and Mean
    print('Minimum along columns \n:',b.min(axis=0))
    print("Maximum Along Rows \n",b.max(axis=1))
    #Calculate Mean
    print("Mean along rows \n",b.mean(axis=1))
    print("Total mean of array \n",b.mean(dtype=int))
    print(b[0])#First row
    print(b[0,0])#first row first element

def get_index_max(a):
    return a.argmax()



if __name__=="__main__":
    t1=time.time()
    test_run()
    t2=time.time()
    c=np.array([1,2,3])
    t3=time.time()
    print(get_index_max(c))
    print(t1,t2-t1,t3-t2)