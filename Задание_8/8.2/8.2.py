cnt = 0
for i in range(10000, 99999+1, 5):
   ch = str(i)
   if len(ch) == len(set(ch)):
      ok = True
      for c in range(len(ch)-1):
         if (int(ch[c]) % 2) == (int(ch[c+1]) % 2):
            ok = False
            break
      if ok:
         cnt += 1
print(cnt)
