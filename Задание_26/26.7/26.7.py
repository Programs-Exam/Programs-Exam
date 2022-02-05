f = open('26-J1.txt')
n = int(f.readline())
mas = [0]*100
cnt = 0
for line in f:
   x = int(line)
   mas[x] += 1
for i in range(1, 49+1):
   cnt += min(mas[i], mas[-i-1])
cnt += mas[-1]
print(cnt)


# f=open('26-J1.txt')
# n=int(f.readline())
# a=[]
# cnt=0
# for line in f:
#    a.append(int(line))
# for i in range(n-1):
#    if a[i]==99:
#       a[i]=-100
#       cnt+=1
#    else:
#       for j in range(i+1,n):
#          if a[i]+a[j]==99:
#             cnt+=1
#             a[i]=a[j]=-100
# print(cnt)
