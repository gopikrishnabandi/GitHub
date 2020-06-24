players=[1,3,9,15,37]#try with 01 as an element , it will throw error
print(players[0])
print(players[1])
#assigning
players[0]=10
print(players)#[10,3,9,15,37]
#appending lists in two ways
players=players+[47,48,52]
print(players)#[10, 3, 9, 15, 37, 47, 48, 52]
players.append(90)
print(players)#[10, 3, 9, 15, 37, 47, 48, 52, 90]
#slicing lists
print(players[2:5])#from 2 till 5 i.e., [9,15,37]
players[2:5]=[10,11,28]#we can assign
print(players)#[10,3,10,11,28,47,48,52,90]
#remove from list
players.remove(10)#removes first occuerence of that elemet permananetly
players.remove(10)
print('end')
