f = open('27-3b.txt')
n = int(f.readline())
s = 0
dmin = 10000
for i in range(n):
    a = list(map(int, f.readline().split()))
    s += max(a)
    raz = abs(a[0]-a[1])
    if raz % 7 != 0:
        dmin = min(dmin, raz)
if s % 7 != 0:
    print(s)
else:
   print(s-dmin)
