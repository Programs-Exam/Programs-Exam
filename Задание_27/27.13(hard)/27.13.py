f = open('27-71a.txt')
n = int(f.readline())
s = [[0, 0]]  # сумма и длина
maxs = minl = 0
for i in range(n):
   x = int(f.readline())
   cmb = [[pred+x, l+1] for pred, l in s]+[[x, 1]]
   s = {y[0] % 69: y for y in sorted(cmb)}
   if 0 in s:
      curs, curl = s[0]
      if curs > maxs or curs == maxs and curl < minl:
         maxs, minl = curs, curl
   s = s.values()
print(minl)
