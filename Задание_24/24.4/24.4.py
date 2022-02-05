f = open("24-j7.txt")
s=f.readline().strip()
clen=mlen=1
def mode(ch):
   return int(ch)%2
for i in range(len(s)-1):
   if mode(s[i]) == mode(s[i+1]):
      clen+=1
      mlen=max(mlen,clen)
   else:
      mlen = max(mlen, clen)
      clen=1
print(mlen)
