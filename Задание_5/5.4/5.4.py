for n in range(10000000):
    s1 = s2 = 0
    for c in range(len(str(n))):
        if int(str(n)[c]) % 2 == 0:
            s1 += int(str(n)[c])
        if c % 2 == 0:
            s2 += int(str(n)[c])
    if abs(s1-s2) == 26:
        print(n)
        break