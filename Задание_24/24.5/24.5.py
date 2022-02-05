f = open("24-j9.txt")
s = f.readline()
cnt = 0
for i in range(len(s)//2):
   if s[i] == s[-i-1]:
      cnt += 1
print(cnt)
