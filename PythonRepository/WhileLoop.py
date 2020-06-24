n=5
while n>0:#n is an iteration variable(controls how long the iteration is going to run)
    print(n)
    n=n-1#without this it becomes an indefinite loop i.e., it runs infinite times
print('end of loop')
print('n value is',n)
while True:#creates and infinite loop , as this will never get false , we use a break statement to break it
    line=input('Enter input:')
    if line=='done':
        break#break statements ends the current loop and jumps to the immediately statement after the loop
    print(line)
print('done')
