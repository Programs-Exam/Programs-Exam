m = []
for A in range(1, 1000):
   ok = True
   for x in range(1, 1000):
      if (x & A != 0) and (x & 58 == 0) and (x & 22 == 0):
         ok = False
         break
   if ok:
      m += [A]
print(m[-1])
