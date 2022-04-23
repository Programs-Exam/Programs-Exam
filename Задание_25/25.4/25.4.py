for i in range(862346, 1056242+1):
    delit=[]
    for d in range(2, round(i**(0.5))+1):
        if i % d == 0:
            delit+=[d,i//d]
    delit=sorted(set(delit))
    if len(delit)>1:
        ok=True
        for j in range(len(delit)-1):
            if delit[j+1]-delit[j]!=100:
                ok=False
                break
        if ok:
            print(i,max(delit))