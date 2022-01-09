f=open('17-1.txt')
mas=[]
sall=0
for line in f:
   mas+=[int(line)]
   sall += int(line)
f.close()
sr=sall/len(mas)
cnt=maxs=0
for i in range(len(mas)-1):
   s = mas[i]+mas[i+1]
   if mas[i]>sr and mas[i+1]>sr and s%100==35:
      cnt+=1
      if s>maxs:
         maxs=s
print(cnt,maxs)