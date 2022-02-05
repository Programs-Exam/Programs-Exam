for i in range(162, 10001):  # при i<162 b отрицательный
   x = i
   a = 5*x + 345
   b = 5*x - 807
   while a != 0 and b != 0:
      if a > b:
         a -= b
      else:
         b -= a
   if a == 96:
      print(i)
      break
