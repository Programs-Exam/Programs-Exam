for i in range(190280, 190201-1,-1):
   divs=[]
   ans=[]
   for d in range(1,round(i**0.5)+1):
      if i%d==0:
         divs+=[d,i//d]
   divs=sorted(set(divs))
   cnt2=0
   for j in divs:
      if j%2==0:
         ans+=[j]
         cnt2+=1
   if cnt2==4:
      print(*sorted(ans,reverse=True),sep='')
      break
#ans:1902769513842