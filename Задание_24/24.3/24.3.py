f = open('24-181.txt')
s = f.readline()
clen=mlen=tcnt=0
for i in s:
   if i not in 'TRN':
      clen+=1
      if i=='.':
         tcnt+=1
      if tcnt>=5:
         mlen=max(clen,mlen)
   else:
      clen=0
      tcnt=0
print(mlen)