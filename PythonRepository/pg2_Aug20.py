'''Task
Read two integers from STDIN and print three lines where:

The first line contains the sum of the two numbers.
The second line contains the difference of the two numbers (first - second).
The third line contains the product of the two numbers.
Input Format

The first line contains the first integer,a . The second line contains the second integer,b .'''
a=int(input())
b=int(input())
print(a+b)
print(a-b)
print(a*b)

"""We add a Leap Day on February 29, almost every four years. The leap day is an extra, or intercalary day and we add it to the shortest month of the year, February.
In the Gregorian calendar three criteria must be taken into account to identify leap years:

The year can be evenly divided by 4, is a leap year, unless:
The year can be evenly divided by 100, it is NOT a leap year, unless:
The year is also evenly divisible by 400. Then it is a leap year.
This means that in the Gregorian calendar, the years 2000 and 2400 are leap years, while 1800, 1900, 2100, 2200, 2300 and 2500 are NOT leap years

Task
You are given the year, and you have to write a function to check if the year is leap or not.

Note that you have to complete the function and remaining code is given as template.

Input Format

Read y, the year that needs to be checked."""
def is_leap(year):
    return (year % 400 == 0) or (( year % 100 != 0) and (year % 4 == 0))
#below also is a valid code
    """if n % 400 == 0:
        return True
    if n % 100 == 0:
        return False
    if n % 4 == 0:
        return True
    return False"""
year = int(input())
print(is_leap(year))
"""Read an integer .
Without using any string methods, try to print the following:
Note that "" represents the values in between.
Input Format
The first line contains an integer .
Output Format
Output the answer as explained in the task.
Sample Input 0
3
Sample Output 0
123"""
if __name__ == '__main__':
    n = int(input())
    i=1
    while i<=n:
        print(i,end='')
        i=i+1
