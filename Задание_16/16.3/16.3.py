def g(n):
    if n > 40:
        return 10
    elif n < 41:
        return 30 + f(n + 600 // n)
def f(n):
    if n < 50:
        return n
    elif n > 49:
        return  2*g(50 - n // 2)

print(f(80))