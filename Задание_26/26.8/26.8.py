f = open('26-k5.txt')
n, k, m = map(int, f.readline().split())
a = []
for line in f:
   a.append(int(line))
a = sorted(a, reverse=True)
prem = a[:m]
bud = a[-k:]
print(prem[-1])
print(sum(bud)//len(bud))
