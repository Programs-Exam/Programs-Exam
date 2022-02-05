f=open('27-1B.txt')
n=int(f.readline())
cnt=n2=n5=n7=n10=0
for i in range(n):
   x=int(f.readline())
   if x%10==0:
      n10+=1
   elif x%7==0:
      n7+=1
   elif x%5==0:
      n5+=1
   elif x%2==0:
      n2+=1
cnt=(n*(n-1)//2)-n10*(n10-1)//2-n10*(n-n10)-n2*n5-n7*(n7-1)//2-n7*(n-n10-n7)
print(cnt)