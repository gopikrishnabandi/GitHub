print('gopi')
print('krishna')
#print('she isn't coming home) python thinks string ends at n
#one way to mitigate it is use double quotes
print("she isn't coming home")
#opposite of it is to use single quotes when sentence has double
print('she said.."what the hell"')
#with this aproach the problem comes when there are both singel and
#double quotes , we cannot use the above approaches, so we use escaping
#\ tells python that it is not end and treat it as a common character
#\ means something special for python
print('she isn\'t coming home,"hurray"')
print('D:\newfiles')#what is the issue here ?
#\n means new line in python, so D: and ewfiles (in new line) will be printed
#to avoid issues , we can put r to print raw string 9whatever is b/w single quotes
print(r'D:\newfiles')
#print(r'D:\newfiles she isn't coming home) to check issue uncomment and see
#issue with above line is r tells whatever is in b/w single quotes as raw string, single quotes ending after n
print(r'D:\newfiles she isn\'t coming home')#fixed
#r is generally used when dealing with file paths
print('gopi'+'krishna')#no space
print('gopi','krihna')#space added when sepearted by ,
print('gopi'*3)#gopigopigopi
print('bandi'.join('gopi'))#till end of string joins
#gbandiobandipbandii
print('-'.join('gopi'))
#g-o-p-i, - is used to fill b/w letters till the end
print('abc'.join('M'))
#only one letter M , so abc cannot be used as a glue to join M, had there been two it would be different
