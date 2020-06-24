'''Mr. Vincent works in a door mat manufacturing company. One day, he designed a new door mat with the following specifications:
Mat size must be NXM. (N is an odd natural number, and M is 3 times N .)
The design should have 'WELCOME' written in the center.
The design pattern should only use |, . and - characters.
Sample Designs
9,6,3
    Size: 7 x 21
    ---------.|.---------
    ------.|..|..|.------
    ---.|..|..|..|..|.---
    -------WELCOME-------
    ---.|..|..|..|..|.---
    ------.|..|..|.------
    ---------.|.---------
Python 2: print ("string").center(width)
Python 3: print ("string".center(width))
Python 2: print ("string" + varible).center(width)
Python 3: print (("string" + varible).center(width))'''
#copied

n, m = map(int,input().split())
pattern = [('.|.'*(2*i + 1)).center(m, '-') for i in range(n//2)]
print('\n'.join(pattern + ['WELCOME'.center(m, '-')] + pattern[::-1]))
#pattern[::-1]does exact reverse of pattern

N,M = map(int,input().split())
for i in range(1, N, 2):
    print (('.|.'*i).center(M,'-'))
print ("WELCOME".center(M,'-'))
for i in range(N-2, -1, -2):
    print (('.|.'*i).center(M, '-'))
