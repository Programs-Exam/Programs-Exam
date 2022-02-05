m = []
for i in range(1, 500):
   b = bin(i)[2:]
   for j in range(3):
      if b.count('1') == b.count('0'):
         b += b[-1]
      elif b.count('1') > b.count('0'):
         b += '0'
      elif b.count('1') < b.count('0'):
         b += '1'
   if int(b, 2) % 4 == 0 and int(b, 2) % 8 != 0:
      m += [i]
print(max(m))
