'''You are given an integer,N . Your task is to print an alphabet rangoli of size N . (Rangoli is a form of Indian folk art based on creation of patterns.)
Different sizes of alphabet rangoli are shown below:
#size 3
----c----
--c-b-c--
c-b-a-b-c
--c-b-c--
----c----
#size 5
--------e--------
------e-d-e------
----e-d-c-d-e----
--e-d-c-b-c-d-e--
e-d-c-b-a-b-c-d-e
--e-d-c-b-c-d-e--
----e-d-c-d-e----
------e-d-e------
--------e--------
The center of the rangoli has the first alphabet letter a, and the boundary has the Nth alphabet letter (in alphabetical order).
Input Format
Only one line of input containing N , the size of the rangoli.
Output Format
Print the alphabet rangoli in the format explained above.
'''
#copied

import string
def print_rangoli(size):
    # your code goes here
    #Top half including center line
    for i in range(size):
        s = "-".join(chr(ord('a')+size-j-1) for j in range(i+1))
        print((s+s[::-1][1:]).center(size*4-3, '-'))

        #below linesin output
    '''for i in range(size-1):
        s = "-".join(chr(ord('a')+size-j-1) for j in range(n-i-1))
        print((s+s[::-1][1:]).center(size*4-3, '-'))'''


if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)
