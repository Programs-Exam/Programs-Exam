f=open('26-k3.txt')
spis=[]
n,k,m=map(int,f.readline().split())
for line in f:
   spis+=[int(line)]
spis=sorted(spis)[::-1]
print(spis[k],spis[0])