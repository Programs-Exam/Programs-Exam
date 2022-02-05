for a in range(1000, 1,-1):
   ok = True
   for x in range(1000):
      if not(x % 40 == 5) <= ((x+10) % a == 5 and (a*a + 180 > 200)):
         ok = False
         break
   if ok:
      print(a)
      break
