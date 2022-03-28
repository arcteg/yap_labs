number = int(input("Введите число: "))
x = 2
while number % x != 0:
    x += 1
if x == number:
    print('Число является простым.')
else:
    print('Число не является простым.')
