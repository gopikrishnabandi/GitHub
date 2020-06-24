str='X-DPSAM-Confidence: 0.8745'
nstr=str.find(':')
print(nstr)
nstr1=str[nstr+1:]#use nstr+2 to directly to fetch only numeric part
print(nstr1)
x=float(nstr1)#Float automatically removes spaces
print(x)
#Alternate Way
#y=nstr1.strip()
#print(y)
