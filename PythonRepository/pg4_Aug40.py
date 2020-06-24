'''You are given a string S and width w .
Your task is to wrap the string into a paragraph of width .
Input Format
The first line contains a string,S .
The second line contains the width,w .
Output Format
Print the text wrapped paragraph.
Sample Input 0
ABCDEFGHIJKLIMNOQRSTUVWXYZ
4
Sample Output 0
ABCD
EFGH
IJKL
IMNO
QRST
UVWX
YZ'''
#what i wrote
'''def wrap(string, max_width):
    x=int(len(string)/max_width)
    y=len(string)%x
    position=0
    if y==0:
        for i in range(x):
            print(string[position:position+max_width])
            position=position+max_width
    else:
        for i in range(x+1):
            if i<x:
                print(string[position:position+max_width])
                position=position+max_width
            else:
                print(string[position:len(string)])
                break
if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)'''

'''#Actual Answer'''
import textwrap
S = input()
w = input()
print textwrap.fill(S,w)


#without textwrap:#Better than mine
'''def wrap(string, max_width):
    return "\n".join([string[i:i+max_width] for i in range(0, len(string), max_width)])'''
