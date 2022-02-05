f = open('26-j4.txt')
fa = []
n= int(f.readline())
k=n//10
for line in f:
   fa += [int(line)]
fa = sorted(fa)[k:-k]
print(sum(fa),fa[-1])