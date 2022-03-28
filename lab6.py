# 1 1 2 3 5 8 13 21 ...
def fib(n):
    try:
        c = 1
        if n > 2:
            c = fib(n - 1) + fib(n - 2)
        return c
    except RecursionError:
        print('Число превышает рекурсивную допустмую глубину!')
        raise SystemExit


n = int(input('Введите число (не превышающее допустимую рекурсивную глубину):  '))
print(fib(n))