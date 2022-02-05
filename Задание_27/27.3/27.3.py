f = open('27-3a.txt')
n = int(f.readline())
s = 0
D = 7
dMin = [10000000]*D
for i in range(n):
   a, b = map(int, f.readline().split())
   s += max(a, b)
   d = abs(b-a)
   r = d % D
   if r > 0:
      dMinNew = dMin[:]
      for k in range(1, D):
         r0 = (r+k) % D
         dMinNew[r0] = min(d+dMin[k], dMin[r0])
      dMinNew[r] = min(d, dMin[r])
      dMin = dMinNew[:]
if s % D == 0:
    print(s)
else:
   print(s-dMin[s % D])
