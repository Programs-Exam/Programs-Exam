f = open('17-275.txt')
mas=[int(line[:len(line)-1]) for line in f]
cnt=0
ms=-25000
for i in range(1,len(mas)):
    s=mas[i-1]+mas[i]
    if s%11==0:
        ms=max(ms,s)
        cnt+=1
print(cnt,ms)