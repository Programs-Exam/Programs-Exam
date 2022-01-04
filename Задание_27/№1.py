f = open('27-14b.txt')
n = int(f.readline())
el = [0]*31
cnt = 0
for i in range(n):
   x = int(f.readline())
   cnt += el[(31-(x % 31)) % 31]
   el[x % 31] += 1
print(cnt)
