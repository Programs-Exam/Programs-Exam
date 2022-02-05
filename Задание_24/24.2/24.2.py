s = open('24-2.txt').readline()
l = 1
ml = 1
mx = s[0]
x = s[0]
for i in range(1, len(s)):
   if s[i-1] > s[i]:
      x += s[i]
      l += 1
      ml = max(ml, l)
   else:
      if len(mx) < len(x):
         mx = x
      x = s[i]
      l = 1
print(mx, x)  # вдруг, мы закончили на самой длинной
# ans: vkgfZN80
