#convert upper to lower and vice versa in a string
def swap_case(s):
    result=s.swapcase()
    return result

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)
'''Task
You are given a string. Split the string on a " " (space) delimiter and join using a - hyphen.
Input Format
The first line contains a string consisting of space separated words.
Output Format
Print the formatted string as explained above.
Sample Input
this is a string
Sample Output
this-is-a-string'''
def split_and_join(line):
    # write your code here
    result=line.split(' ')
    result='-'.join(result)
    return result

if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)
'''You are given the firstname and lastname of a person on two different lines. Your task is to read them and print the following:
Hello firstname lastname! You just delved into python.
Input Format
The first line contains the first name, and the second line contains the last name.
Constraints
The length of the first and last name ≤10 .
Output Format
Print the output as mentioned above.
Sample Input 0
Ross
Taylor
Sample Output 0
Hello Ross Taylor! You just delved into python.'''
def print_full_name(a, b):
    print("Hello",a,b+'!','You just delved into python.')

if __name__ == '__main__':#unless imported from an other module, by default the default variable the __name__ is set to __main__
    first_name = input()
    last_name = input()
    print_full_name(first_name, last_name)
'''Task
Read a given string, change the character at a given index and then print the modified string.
Input Format
The first line contains a string ,S .
The next line contains an integer i, denoting the index location and a character c separated by a space.
Output Format
Using any of the methods explained above, replace the character at index i with character c .
Sample Input
abracadabra
5 k
Sample Output
abrackdabra'''
def mutate_string(string, position, character):
    part1=string[:position]
    part2=string[position+1:]
    new=part1+character+part2
    return new

if __name__ == '__main__':
    s = input()
    i, c = input().split()
    s_new = mutate_string(s, int(i), c)
    print(s_new)
'''In this challenge, the user enters a string and a substring. You have to print the number of times that the substring occurs in the given string. String traversal will take place from left to right, not from right to left.
NOTE: String letters are case-sensitive.
Input Format
The first line of input contains the original string. The next line contains the substring.
Constraints
1<=len(string)<=200
Each character in the string is an ascii character.
Output Format
Output the integer number indicating the total number of occurrences of the substring in the original string.
Sample Input
ABCDCDC
CDC
Sample Output
2'''
#copied from solution

def count_substring(string, sub_string):
    count = 0
    for i in range(len(string) - len(sub_string) + 1):
        if string[i:i+len(sub_string)] == sub_string:
            count += 1
    return count

if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()

    count = count_substring(string, sub_string)
    print(count)
#copied from solution
'''Task
You are given a string S.
Your task is to find out if the string S contains: alphanumeric characters, alphabetical characters, digits, lowercase and uppercase characters.
Input Format
A single line containing a string S .
Output Format
In the first line, print True if S has any alphanumeric characters. Otherwise, print False.
In the second line, print True if S  has any alphabetical characters. Otherwise, print False.
In the third line, print True if S has any digits. Otherwise, print False.
In the fourth line, print True if S has any lowercase characters. Otherwise, print False.
In the fifth line, print True if S has any uppercase characters. Otherwise, print False.'''
if __name__ == '__main__':
    str=input()
    print(any(c.isalnum()  for c in str))
    print(any(c.isalpha() for c in str))
    print(any(c.isdigit() for c in str))
    print(any(c.islower() for c in str))
    print(any(c.isupper() for c in str))


#Replace all ______ with rjust, ljust or center.

thickness = int(input()) #This must be an odd number
c = 'H'

#Top Cone
for i in range(thickness):
    print((c*i).rjust(thickness-1)+c+(c*i).ljust(thickness-1))

#Top Pillars
for i in range(thickness+1):
    print((c*thickness).center(thickness*2)+(c*thickness).center(thickness*6))

#Middle Belt
for i in range((thickness+1)//2):
    print((c*thickness*5).center(thickness*6))

#Bottom Pillars
for i in range(thickness+1):
    print((c*thickness).center(thickness*2)+(c*thickness).center(thickness*6))

#Bottom Cone
for i in range(thickness):
    print(((c*(thickness-i-1)).rjust(thickness)+c+(c*(thickness-i-1)).ljust(thickness)).rjust(thickness*6))
