f = open('27-40b.txt')
n = int(f.readline())
s1 = s2 = s3 = 0
dmin=10000
for i in range(n):
   x1, x2, x3=(sorted(map(int, f.readline().split())))
   s1 += x1
   s2 += x2
   s3 += x3
   if (x3-x2) % 7 != 0 and (x3-x2) < dmin:
      dmin = x3-x2
   if (x3-x1) % 7 != 0 and (x3-x1) < dmin:
      dmin = x3-x1
if (s1+s2) % 7 != 0:
   print(s3)
else:
   print(s3-dmin)
# ans: 628 103914685
