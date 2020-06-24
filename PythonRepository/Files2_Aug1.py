#we can give filename as input and feed it to the file handle
#rememeber find gives position, startswith checks a condition and returns true/false
fhandle=open('C:\\Users\\Gopi\\Documents\\Exercise Files\\mbox-short.txt','r')
for line in fhandle:
    line=line.rstrip()#rstrip strips white space at end of every string which is present by default at end of each line in "files"
    #without which we will be priniting a gap between each line
    #rememeber with print statement there is already a new line added
    if line.startswith('From:'):
        print(line)
    #above can also be achiebed with the below code
    #if not line.startswith('From:'):
    #    continue
    #print(line)
fhandle.seek(0)
for line in fhandle:
    line=line.rstrip()
    if not '@uct.ac.za' in line:
        continue
    print(line)
