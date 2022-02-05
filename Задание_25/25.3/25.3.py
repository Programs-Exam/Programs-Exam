def delit(ch):
   d = []
   for j in range(2, round(ch**0.5)+1):
      if ch % j == 0:
         d += [j, ch//j]
   d = sorted(set(d))
   return d
for i in range(81234, 134689+1):
   mas = delit(i)
   if len(mas) == 3:
      print(mas[0], mas[-1])
# 17 4913
# 19 6859
