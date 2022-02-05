m=[]
for i in range(-1000,10000):
   s=i
   n=-5
   while s>10:
      s=s-8
      n=n+3
   if n == 67:
      m+=[i]
print(m[-1],m[0])