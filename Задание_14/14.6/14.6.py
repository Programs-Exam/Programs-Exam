ch=((5**300 * 15**100) - (25**50 + 125**100))
nch=''
while ch!=0:
    nch+=str(ch%5)
    ch//=5
s=0
for c in nch[::-1]:
    if int(c) != 4:
        s+=int(c)
print(s)