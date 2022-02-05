a = [int(x) for x in open ('17-243.txt')]
s33=0
for x in a:
   if x %33 ==0 :
      for c in str(x):
         s33+=int(c)
cnt = 0
ms=100000
for i in range(1,len(a)):
   if a[i] > s33 or a[i-1] > s33:
      cnt+=1
      ms=min(ms,a[i]+a[i-1])
print(cnt,ms)