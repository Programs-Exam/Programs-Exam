with open('24-178.txt') as f:
   s = f.readline()
#подвох задачи в том, что в файле помимо строки есть '\n', который разделяет наше "кольцо" и мы получаем неправильный ответ
s = s.split()
s = ''.join(s)*2
res = local = 1
for i in range(len(s)-1):
   if s[i] <= s[i+1]:
      local += 1
      res = max(res, local)
   else:
      local = 1
      res = max(res, local)
print(res)
# ans: 8
