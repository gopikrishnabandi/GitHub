#a text file has \n new line at the end of the line, a blank line is nothing but a line with only \n,\n is one character when counting length
#fhandle=open(filename,mode)--open returns a file handle variable which is used to perform opeartions on the file
#eg fhandle=open('mbox.txt','r')#mode is optional, filename is always taken as a string
#file handle is like a connection to act on a while, when handle close it goes away
#if we try to open a file that does not exist, a throwback
stuff='Hello\nWorld'
print(stuff)#prints Hello and in next line World
print(len(stuff))#prints 11, since \n is one character
#How to read files and print
fhandle=open('C:\\Users\\Gopi\\Documents\\Exercise Files\\mbox-short.txt','r')
#use \\ in path instead of the default \ that is copied when you copy path , as \ is an escape character in python
for i in fhandle:
    print(i)
fhandle.seek(0)#without this the file handle will be at the end of the file and it will return count as 0 as the number of lines or will print blank for count and print respectively
#other way
#print(fhandle.readlines())--this can also be used to print, but memory intensive as whole file is loaded in memory unlike an iteration
'''printing number of characters'''
inp=fhandle.read()#will read all file into inp
print(len(inp))#will print number of characters
#counting lines in a file
fhandle.seek(0)
count=0
for j in fhandle:
    count=count+1
    #print(j) #without fhandle.seek(0) nothing gets printed as we will be at end of file after any read
print('Number of lines in the file is',count)
fhandle.seek(0)
for line in fhandle:
    line=line.rstrip()
    if line.find(':'):
        print(line)
