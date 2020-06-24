x="outer"
try:
    x="inner"
except:
    pass
print(x)
#output is inner for above
y="outer"
def fn():
    global y#modiefies global variable y outside the function
    y="inner"
    print(y)
fn()
#output for above is inner
z='end'
def fn2():
    z='inner'
    print(z)
fn2()#output is inner
print(z)#prints end
