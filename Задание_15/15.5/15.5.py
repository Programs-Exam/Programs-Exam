for A in range(1000):
   ok = True
   for x in range(100):
      for y in range(100):
         if not(((x < 3) <= (x*x <= A)) and ((y*y < A) <= (y < 15))):
            ok = False
            break
   if ok:
      print(A)
      break
