f = open('26-k4.txt')
spis = []
n, k = map(int, f.readline().split())
for line in f:
   spis += [int(line)]
spis = sorted(spis)[::-1]
otl = spis[:k]
hor = spis[k:k+k]
print(sum(hor)//len(hor), end=' ')
print(sum(otl)//len(otl))
