def f(n):
    if n<=1:
        return 1
    elif n>0 and n%2==0:
        return f(n-1)+11*n
    else: return 11*f(n-2)+n
mas=[]
for i in range(35,50+1):
    mas+=[f(i)]
print(len(str(sum(j for j in mas if j%2==0))))