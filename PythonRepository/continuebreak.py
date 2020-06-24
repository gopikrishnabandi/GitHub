#the important thing to note in this is that continue or break takes control to top or out of the "loop" and not to the "condition" they are in
#while loops are indefinite loops
while True:
    line=input('Enter a line:')
    if line[0]=='#':
        continue#continue ends current iteration and takes control to the top of the loop to continue the next iteration
    if line[0]!='#':
        break#break will take it to the print('Done') i.e., out of the while loop
    print(line)
print('Done')
