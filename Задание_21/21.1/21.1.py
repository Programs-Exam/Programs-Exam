def f(x, p):
   if x >= 20 or p > 5:
      return (p == 3 or p==5)
   if p%2==0:
      return f(x+2, p+1) or f(x*2, p+1)
   else:
      return f(x+2, p+1) and f(x*2, p+1)
def f2(x, p):
   if x >= 20 or p > 3:
      return (p == 3)
   if p%2==0:
      return f2(x+2, p+1) or f2(x*2, p+1)
   else:
      return f2(x+2, p+1) and f2(x*2, p+1)
for s in range(1, 17):
   if f(s, 1):
      print(s)
print('---')
for s in range(1, 17):
   if f2(s, 1):
      print(s)
# ans: 5