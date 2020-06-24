'''You are asked to ensure that the first and last names
of people begin with a capital letter in their passports.
For example, alison heck should be capitalised correctly as Alison Heck.
gopi krishna bandu should be Gopi Krishna Bandi'''
#My Solution
def solve(s):
        a=s.split(' ')
        b=len(a)
        s=' '.join(str(a[i]).capitalize() for i in range(b))
        return s

if __name__ == '__main__':
    s = input()
    result = solve(s)
    print(result,end='')

'''#Actual solution
# Complete the solve function below.
#!/bin/python3
import math
import os
import random
import re
import sys
def solve(s):
    return ' '.join(word.capitalize() for word in s.split(' '))

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = solve(s)

    fptr.write(result + '\n')

    fptr.close()'''
