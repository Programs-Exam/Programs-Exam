print('y w z x')  # head of the table
for x in 0, 1:  # possible binary numbers
   for y in 0, 1:
      for w in 0, 1:
         for z in 0, 1:
            if x and (y and z or y and not (w) or not (z) and not (w)):
               print(y, w, z, x)  # outputs already in the correct form
               
#ans:ywzx
