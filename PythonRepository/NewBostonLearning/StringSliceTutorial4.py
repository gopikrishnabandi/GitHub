import string
user='gopi krishna'
user1='Gopi Bandi'
print(user[0])#computesr count from 0, hence g
print(user[4])#will print space
print(user[-1])#while counting from back, it starts from -1 as negative 0 is 0
print(user[2:7])#prints from 2 till 7, 7 not included,so it will print pi kr
print(user[2:7:2])#what does this print ?
#starts at 2 ends till 7 with 2 as the width for every step
#so prints characters at 2,4,6 indexes i.e., p r
print(user[:5])#starting from beginning till 5th, gopi k
print(user[2:])#starting from 2 till end of string, pi krishna
print(user[:])#gopi krishna
print(user[::])#gopi krishna
print(user[::-1])#anhsirk ipog,beginning till end but in reverse
print(user[:-1])#what happens with this ?
#starts from beginning till -1 position, only with three parameters starts in reverse
#remember -1 is the starting index when counting from back
#hence will print gopi krishn
print(len(user))#12
print(len('gopi'))#same operations can be done on string directly
print('gopi'[2:4])#pi
print(user.index('g'))#0
print(user.index('pi'))#prints the starting index of that sequence
#string constants, importing string is mandatory for below to execute
a=string.ascii_letters
print(a)#prints from atoz and AtoZ together
b=string.ascii_lowercase#prints atoz
print(b)
c=string.ascii_uppercase#prints AtoZ
print(c)
d=string.digits#prints 0to9
print(d)
print(','.join(string.ascii_lowercase))
#a,b,c,.......y,z
print(user.upper())#GOPI KRISHNA
print(user1.lower())#gopi bandi
print(user.capitalize())#Gopi krishna , only first letter is capitalized
print('{0} is better than {1}'.format('Cricket','Football'))
#cricket is better than Football
print('{2},{1},{0} is the reverse order of {0}{1}{2}'.format(1,2,3))
#3,2,1 is the reverse order of 123
for i in user1:
    print(i)
teststring=' gopi krishna bandi '
print(teststring.find('k'))#position of first occurence
print(teststring.replace('a','u'))#will replace a with u
print(teststring)#prints original value
print(teststring.lstrip())
print(teststring.rstrip())
print(teststring.strip())
teststr='gopi'
print(teststr.startswith('g'))#true
if 'go' in teststr:
    print('found')
if teststr=='gopi':
    print('exact match')
