cnt = 0
for i in range(1, 100+1):
    s = '1'*i
    while '111' in s:
        s = s.replace('111', '2', 1)
        s = s.replace('222', '3', 1)
        s = s.replace('333', '1', 1)
    if s == '321':
        cnt += 1
print(cnt)
