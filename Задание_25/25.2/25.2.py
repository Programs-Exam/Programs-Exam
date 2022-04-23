for i in range(1245,1000000+1):
    if str(i)[:2]=='12' and '45' in str(i):
        if i%51==0:
            print(i,i//51)