def D(x,d): return x%d==0
allA=[A for A in range(101,1000)
      if all(
         (D(x,A) and D(x,36))<=D(x,324)
         for x in range(1,100000))
      ]
print(allA[0])