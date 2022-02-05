f = open('27-40b.txt')
n = int(f.readline())
s1 = s2 = s3 = 0
dmin = 10000
for i in range(n):
   x1, x2, x3 = (sorted(map(int, f.readline().split()))[::-1])
   s1 += x1
   s2 += x2
   s3 += x3
   if (x1-x2) % 2 != 0 and (x1-x2) < dmin:
      dmin = x1-x2
   if (x1-x3) % 2 != 0 and (x1-x3) < dmin:
      dmin = x1-x3
if (s1+s2) % 2 != 0:
   print(s3)
else:
   print(s3+dmin)
#ans: 245 20069046
