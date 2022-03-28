f=open('24-175.txt')
s=f.readline()
p=s.split('KEGE')
maxLen=0
for i in range(len(p)-2):
    chunk=p[i]+"KEGE"+p[i+1]+"KEGE"+p[i+2]
    if i!=0: chunk='EGE'+chunk #если учитываем первый кусок
    if i+2!=len(p)-1: chunk=chunk+'KEG' #если учитываем последний кусок
    maxLen=max(len(chunk),maxLen)
print(maxLen)