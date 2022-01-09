for a in range(400, 1, -1):
   ok = True
   for x in range(1000):
      if not(((x//40) > 10) or not(x//20 > 4) or (x // a > 4)):
         ok = False
         break
   if ok:
      print(a)
      break
