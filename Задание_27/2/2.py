f = open('27-1B.txt')
n = int(f.readline())
a = []
cnt2 = cnt31 = cnt62 = 0
for i in range(n):
    x=int(f.readline())
    if x % 62 == 0:
        cnt62 += 1
    elif x % 31 == 0:
        cnt31 += 1
    elif x % 2 == 0:
        cnt2 += 1
cnt = cnt62*(cnt62-1)//2+cnt2*cnt31+cnt62*(n-cnt62)
print(cnt)
f.close()