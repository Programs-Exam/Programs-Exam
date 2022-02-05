def f(x, p):
   if x >= 20 or p > 4:
      return (p == 4)
   if p % 2 != 0:
      return f(x+2, p+1) or f(x*2, p+1)
   else:
      return f(x+2, p+1) and f(x*2, p+1)


m = []
for s in range(1, 17):
   if f(s, 1):
      m += [s]
print(min(m), max(m))
# ответ:4 7
