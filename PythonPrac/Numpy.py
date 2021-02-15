import numpy as np

a=np.array([[1,2,3,4],[5,6,7,8]])
print(a)
a_empty=np.empty(shape=(3,4))
a_zeros=np.zeros(shape=(2,2))
a_ones=np.ones(shape=(2,3),dtype=int)
print(a_empty)
print(a_zeros)
print(a_ones)
print('-------------')
a_square=np.eye(3)
print(a_square)
a_arange=np.arange(3,12,2)
a_arange1=np.arange(3,13,2)
print(a_arange,a_arange1)
a_random=np.random.random(size=(3,2))
a_random1=np.random.randint(10,100,size=(3,2),dtype=int)
a_random2=np.random.rand(3,2)
a_random3=np.random.randn(3,2)
print(a_random)
print(a_random1)
print(a_random2)
print(a_random3)
##indexing and slicing
sample=np.array([11,1,20,3,4])
print(sample[0])
print(sample[0:3])
sample2=np.array([[1,2,5,11],[7,6,2,4]])
print(sample2)
print(sample2[0])
print(sample2[1,1])
#assigning
sample[0]=10
print(sample)
sample[0:2]=13
print(sample)
sample2[1]=2
print(sample2)
sample2[1,1:3]=4
print(sample2)
sample3=sample2[1:4,1:3] #left of comma rows to be included, right columns to be included
print(sample3)
sample4=np.array([[1,2,3],[4,5,6]])
sample5=sample4[0]
print('-------------')
print(sample5)
print('--------------')
print(sample5)
print(sample4)
arr2d = np.array([
  [1, 2, 3],
  [4, 5, 6],
  [7, 8, 9]
])
print('arr2d')
print(arr2d[0][1])
print(arr2d[1:,1])
print(arr2d[1:,1].reshape(2,1))
arr2d_change=arr2d[0]
print(arr2d_change)
print(arr2d_change.shape)
arr2d_change[0:2]=0
print(arr2d)
#new array that is created will change original also , as new array is referenced to original array
arr_2d = np.array([
  [1, 2, 3],
  [4, 5, 6],
  [7, 8, 9]
])
arr3d=arr_2d.copy()
arr3d[0:2,0:1]=0
print(arr3d)
arr_full=np.full(shape=(2,2),fill_value=1,dtype=int)
print(arr_full)

arr_eg2=np.arange(2,20,2).reshape(3,3)
print(arr_eg2)
print(arr_eg2.T)
print(arr_eg2.transpose())
arr_eg3=np.where(arr_eg2%2==0,"Even","Odd")
print(arr_eg3)
eg=np.array([[5,3],[2,1]])
print(np.sort(eg,axis=0))
print(np.sum(eg,axis=1))
num_array=np.array([1,2,3,4,5,6,6])
print(np.mean(num_array))
print(np.std(num_array))
print(np.var(num_array))
print(np.unique(num_array))
bol_array1=np.array([True,False,False,True])
bol_array2=np.array([True,True])
print(np.any(bol_array1))
print(np.all(bol_array1))
print(np.all(bol_array2))
np.save('Saved1',bol_array1)
load1=np.load('Saved1.npy')
print(load1)
eg3=np.array([[1,2,3],[4,5,6]])
print(eg3.shape[0])
print(eg3.shape[1])


def getMinMax(arr):
  res = []
  for i in range(arr.shape[0]):
    min=np.min(arr[i])
    max=np.max(arr[i])
    res.append(min)
    res.append(max)
    #Wrong Code, refer geeks for geeks
    # j = 0
    # min = arr[i][0]
    # max = arr[i][0]
    # while j <= arr.shape[1]:
    #   if min < arr[i][j + 1]:
    #     min = arr[i][j]
    #     max = arr[i][j + 1]
    #   elif min > arr[i][j + 1]:
    #     min = arr[i][j + 1]
    #     max = arr[i][j]
    #   elif min == arr[i][j + 1]:
    #     continue
    # res.append(min)
    # res.append(max)

  return res

if __name__=='__main__':
  arr1=np.array([[3,4,1,1,2,7,2,2,1,4,2],[1,1,3,2,1,1,0,4,2,4,4]])
  print(getMinMax(arr1))
  arr2=np.array([[1,2,3],[4,5,6],[7,8,9]])
  print(np.arange(arr2.shape[0]))