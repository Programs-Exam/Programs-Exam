cnt = 0
for a in range(200, 1, -1):
   ok = True
   for x in range(1000):
      if not((x % 40 == 0 and x % 45 == 0) <= (x % a == 0 and (a*(a - 30) < 30 * (a + 180)))):
         ok = False
         break
   if ok:
      print(a)
      break
