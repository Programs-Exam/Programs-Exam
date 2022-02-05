f = open('27-40a.txt')
n = f.readline()
s1 = s2 = s3 = 0
dmin = 10000000
for line in f:
   x1, x2, x3 = sorted(map(int, line.split()))[::-1]
   s1 += x1
   s2 += x2
   s3 += x3
   if x1-x3 < dmin and (x1-x3) % 2 != 0:
      dmin = x1-x3
   if x2-x3 < dmin and (x2-x3) % 2 != 0:
      dmin = x2-x3
if s1 % 2 != s2 % 2:
   print(s3)
else:
   print(s3+dmin)
