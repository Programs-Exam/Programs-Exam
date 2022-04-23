with open('26-16.txt') as f:
    m,n=map(int,f.readline().split())
    groups=[list(map(int,x.split())) for x in f]
    to_seat=sorted([group for group in groups if group[-1]==1],key=lambda group:group[0]/group[1])[::-1]+\
             sorted([group for group in groups if group[-1]==0],key=lambda group: group[0]/group[1])[::-1]
    komp,maxp=0,0
    cnt=0
    s=0
    for group in to_seat:
        if m-group[1]>=0:
            m-=group[1]
        else:
            maxp=max(maxp,group[0]/group[1])
            komp+=group[0]

print(komp,maxp)

