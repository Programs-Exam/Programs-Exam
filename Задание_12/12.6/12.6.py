for x in range(50):
    for y in range(50):
        for z in range(50):
            s='0'+'1'*x+'2'*y+'3'*z+'0'
            while not '00' in s:
                s = s.replace('01', '21022', 1)
                s = s.replace('02', '310', 1)
                s = s.replace('03', '230112', 1)
            if s.count('1')==104 and s.count('2')==39 and\
                s.count('3')==83:
                    print(x+y+z+2)