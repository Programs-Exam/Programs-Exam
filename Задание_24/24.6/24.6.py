f = open("24-21.txt")
s=f.readline()
def nomer(s):
   if s[0].isalpha() and s[1:4].isnumeric() and s[-1].isalpha()and s[-2].isalpha():
      return True
cnt=0
for i in range(len(s)-6):
   if nomer(s[i:i+6]):
      cnt+=1
print(cnt)
