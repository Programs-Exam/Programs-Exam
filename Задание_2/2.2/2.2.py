print('c', 'a', 'd', 'b')  # head of the table
for a in 0, 1:  # possible binary numbers
   for b in 0, 1:
      for c in 0, 1:
         for d in 0, 1:
            if not(a and not(b) or (a or b) and c or d):
               print(c, a, d, b)  # outputs already in the correct form
               
#ans:cadb
