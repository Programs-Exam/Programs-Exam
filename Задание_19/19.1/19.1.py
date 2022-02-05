def f(x, p):
   if x >= 20 or p > 3:
      return (p == 3)
   return f(x+2, p+1) or f(x*2, p+1)


for s in range(1, 17):
   if f(s, 1):
      print(s)
      break
# ответ:5
