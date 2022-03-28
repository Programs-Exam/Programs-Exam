for i in range(256):
    n=bin(i)[2:]
    while len(n)!=8:
        n='0'+n
    new=''
    for c in n:
        if c=='1': new+='0'
        else: new+='1'
    if int(new,2)==220:
        print(i)
        break