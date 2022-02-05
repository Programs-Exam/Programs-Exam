from itertools import combinations
def nok(a, b):
   a1, b1 = a, b
   while a1 != 0 and b1 != 0:
      if a1 > b1:
         a1 %= b1
      else:
         b1 %= a1
   return a*b//(a1+b1)
f = open('27-77b.txt')
n = int(f.readline())
s = [0]
for i in range(n):
   a = [int(x) for x in f.readline().split()[1:]]
   noks = []
   for j in combinations(a, 2):
      noks.append(nok(j[0], j[1]))
   cmb = [a+b for a in s for b in noks]
   s = {x % 33: x for x in sorted(cmb)}.values()
m = max(x for x in s if (x % 3 == 0) != (x % 11 == 0))
print(m)
#ans: 2260788 1254402259
