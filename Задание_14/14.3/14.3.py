x = 2
s = (99 + 3*9 ** x)*9 ** x + 99 + 9 ** 9
ch9 = []
while s != 0:
    ch9 += [s % 9]
    s //= 9
print(sum(ch9))
