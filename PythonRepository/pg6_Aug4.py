'''Given an integer, , print the following values for each integer i from 1 to n :
Decimal
Octal
Hexadecimal (capitalized)
Binary
The four values must be printed on a single line in the order specified above for each i from 1 to n. Each value should be space-padded to match the width of the binary value of n.
Input Format
A single integer denoting n.
Output Format
Print n lines where each line i (in the range 1 to n ) contains the respective decimal, octal, capitalized hexadecimal, and binary values of i. Each printed value must be formatted to the width of the binary value of n.'''

#My Code after help with rjust and upper, used capitalize which is wrong as only first letter is modified in it
def print_formatted(number):
    # your code goes here
    width=len(bin(number))-2#2 indicates 0b which are the first two characters in decimal, can also use[2:] i.e., len(bin(number)[2:])
    for i in range(1,number):
        print(str(i).rjust(width),str(oct(i)[2:]).rjust(width),str(hex(i)[2:].upper()).rjust(width),str(bin(i)[2:]).rjust(width),end='\n')
    print(str(number).rjust(width),str(oct(number)[2:]).rjust(width),str(hex(number)[2:]).upper().rjust(width),str(bin(number)[2:]).rjust(width),end='')
if __name__ == '__main__':
    n = int(input())
    print_formatted(n)
#can be done with with format also, which is used to substitute values in {}
