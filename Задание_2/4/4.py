print('a b c d')
for a in 0, 1:
   for b in 0, 1:
      for c in 0, 1:
         for d in 0, 1:
            if not(a and not(b) or (a or b) and c or d):
               print(a, b, c, d)
# cadb
