f = open('26-k2.txt')
izm = []
n, k= map(int, f.readline().split())
for line in f:
   izm += [int(line)]
izm=sorted(izm)
ned = izm[:k]+izm[-k:]
izm = izm[k:-k]
print(izm[0],sum(ned)//len(ned))