# 1 1 2 3 5 8 13 21 ...
def fib(n):
    c = 1
    if n > 2:
        c = fib(n - 1) + fib(n - 2)
    return c


n = int(input("Введите число: "))
print(fib(n))