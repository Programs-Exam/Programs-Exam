s = '5'*29+23*'4'+'3'*17  # в таком порядке количество троек максимально
while '43' in s or '53' in s:
    if '43' in s:
        s = s.replace('43', '33', 1)
    else:
        s = s.replace('53', '433', 1)
print(len(s))
