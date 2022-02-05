c = 12 ** 34 + 7*12 ** 26 - 3*12 ** 16 + 2*12 ** 5 + 552
ost = []
while c != 0:
   ost += [c % 12]
   c //= 12
print(len(set(ost)))
