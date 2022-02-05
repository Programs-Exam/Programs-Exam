def f(x, finish):
   if x == finish:
      return 1
   if x > finish or x == 21:
      return 0
   if x % 2:
      x3 = x+x+1
   else:
      x3 = x+x+2
   return f(x+1, finish)+f(x+4, finish)+f(x3, finish)
print(f(2, 11)*f(11, 26))
