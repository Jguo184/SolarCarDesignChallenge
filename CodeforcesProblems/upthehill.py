x = int(input(""))
y = int(input(""))
n = x+y+1

uphill = [i for i in range(y+1,n+1)]
downhill = [(y-i) for i in range(0,y)]
print(*(uphill+downhill))