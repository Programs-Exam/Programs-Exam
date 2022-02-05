f=open('26-1d.txt')
n=int(f.readline())
mas=[0]*150
cnt=0
for line in f:
   x=int(line)
   mas[x]+=1
for i in range(1,75):
   cnt+=min(mas[i],mas[-i])
cnt+=mas[75]//2
print(cnt)


# f=open('26-1d.txt')
# n=int(f.readline())
# a=[]
# cnt=0
# for line in f:
#    a.append(int(line))
# for i in range(n-1):
#    for j in range(i+1,n):
#       if a[i]+a[j]==150:
#          cnt+=1
#          a[i]=a[j]=0
# print(cnt)
