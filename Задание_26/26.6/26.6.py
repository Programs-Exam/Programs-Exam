f = open('26-k3.txt')
n,k,m=map(int,f.readline().split())
a=[]
for rez in f:
   a.append(int(rez))
f.close()
a.sort(reverse=True)
print(a[k+m-1],a[k-1])