k=0
for i in range(1000):
    n=bin(i)[2:]
    s=sum(int(x) for x in n)
    if i%2==0:
        n=n+bin(s)[2:]
    else:
        n='1'+n+'00'
    if 500<=int(n,2)<=700:
        k+=1
print(k)