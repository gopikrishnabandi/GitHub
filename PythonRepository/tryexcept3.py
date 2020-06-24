hours=input('Enter hours:')
rate=input('Enter rate:')
try:
    hr=float(hours)#if string is entered , will result in error, hence try except
    rt=float(rate)
except:
    print('Please enter numeric input:')
    quit()
print(hr,rt)#without quit above the print will throw an error/traceback because in case of Wrong Input, statements wont be executed and variables above will be undefined to print
if hr>40:
    bonus=10
    totalpay=(hr*rt)+(hr-40)*bonus
else:
    totalpay=hr*rt
print("The totalpay is",totalpay)
