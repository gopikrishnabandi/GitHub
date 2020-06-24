filename=input('Enter the file name:')
#placing in same directory will require no additional path, can directly give file name
try:
    fhandle=open(filename,'r')
except:
    print("Invalid file name")
    #continue and break can only be used in for or while loops
    quit()
for x in fhandle:
    x=x.rstrip()
    print(x.upper())
