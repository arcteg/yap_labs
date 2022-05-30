import matplotlib.pyplot as plt
import numpy as np
import sys
import pygame
from matplotlib.patches import *


def cust():
    # Длина графика
    xmin, xmax, ymin, ymax = -10, 10, -10, 10
    ticks_frequency = 1

    # Plot points Создание графика

    # Set identical scales for both axes
    ax.set(xlim=(xmin - 1, xmax + 1), ylim=(ymin - 1, ymax + 1), aspect='equal')

    # Убираем ненужное по бокам
    ax.spines['bottom'].set_position('zero')
    ax.spines['left'].set_position('zero')

    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)

    # Create 'x' and 'y' labels placed at the end of the axes
    ax.set_xlabel('x', size=14, labelpad=-24, x=1.03)
    ax.set_ylabel('y', size=14, labelpad=-21, y=1.02, rotation=0)

    # Create custom major ticks to determine position of tick labels
    x_ticks = np.arange(xmin, xmax + 1, ticks_frequency)
    y_ticks = np.arange(ymin, ymax + 1, ticks_frequency)
    ax.set_xticks(x_ticks[x_ticks != 0])
    ax.set_yticks(y_ticks[y_ticks != 0])

    # Create minor ticks placed at each integer to enable drawing of minor grid
    # lines: note that this has no effect in this example with ticks_frequency=1
    ax.set_xticks(np.arange(xmin, xmax + 1), minor=True)
    ax.set_yticks(np.arange(ymin, ymax + 1), minor=True)

    # Draw major and minor grid lines
    ax.grid(which='both', color='grey', linewidth=1, linestyle='-', alpha=0.2)

    # рисуем стрелки
    arrow_fmt = dict(markersize=4, color='black', clip_on=False)
    ax.plot((1), (0), marker='>', transform=ax.get_yaxis_transform(), **arrow_fmt)
    ax.plot((0), (1), marker='^', transform=ax.get_xaxis_transform(), **arrow_fmt)
    return ax


k = 0
fig, ax = plt.subplots(figsize=(10, 10))
try:
    file = open('l81.txt')
    while True:
        s = file.readline()
        k += 1
        if s == '':
            break
        if k == 2:
            xo, yo = map(float, s.split())  # центр окружности
        elif k == 3:
            r = float(s)  # радиус окружности
    file.close()
except ValueError:
    print("Тип данных не тот")
    sys.exit()
except FileNotFoundError:
    print("А хде файл")
    sys.exit()
print(xo, yo, r)


def F(xo, yo, r):
    k = 0
    file = open('l8.txt')
    while True:
        s = file.readline()
        k += 1
        if s == '':
            break
        elif k == 6:
            xr, yr = map(float, s.split())  # координаты левого нижнего угла прямоугольника
        elif k == 8:
            w, h = map(float, s.split())  # ширина, высота
        elif k == 10:
            x1, y1 = map(float, s.split())  # первая точка прямой
        elif k == 11:
            x2, y2 = map(float, s.split())  # вторая точка прямой
        elif k == 13:
            x3, y3 = map(float, s.split())  # координаты точки
    ax = cust()
    ax.clear()
    ax = cust()

    # Переменные прямой
    x = np.linspace(-10, 10, 10)
    y = (x - x1) * (y2 - y1) / (x2 - x1) + y1
    # прямоугольник
    rect = plt.Rectangle((xr, yr), w, h, color="y", fill=True, alpha=0.5)  # закрасить
    rectw = plt.Rectangle((xr, yr), w, h, color="w", fill=True, alpha=1)  # закрасить в белый
    rect_ = plt.Rectangle((xr, yr), w, h, color="y", fill=False, alpha=1)  # окантовка

    # круг
    cir = plt.Circle((xo, yo), r, color="m", fill=True, alpha=0.5)  # закрасить
    cirw = plt.Circle((xo, yo), r, color="w", fill=True, alpha=1)  # закрасить в белый
    cir_ = plt.Circle((xo, yo), r, color="m", fill=False, alpha=1)  # окантовка

    # если точка и в окружности, и в прямоугольнике
    if (xr < x3 < xr + w) and (yr < y3 < yr + h) and ((x3 - xo) ** 2 + (y3 - yo) ** 2) < r ** 2:
        ax.add_patch(cir)
        plt.fill_between(x, yr + h, 1000, color='w')  # красим вверх
        plt.fill_between(x, yr, -1000, color='w')  # красим вниз
        ax.axvspan(-100, xr, color='w')  # красим влево
        ax.axvspan(xr + w, 100, color='w')  # красим вправо

    # если точка в прямоугольнике
    elif (xr < x3 < xr + w) and (yr < y3 < yr + h):
        ax.add_patch(rect)
        ax.add_patch(cirw)  # закрашиваем круг белым

    # если точка в окружности
    elif ((x3 - xo) ** 2 + (y3 - yo) ** 2) < r ** 2:
        ax.add_patch(cir)
        ax.add_patch(rectw)

    # положение точки относительно прямой
    # если прямая вертикальная
    if x1 == x2:
        if x3 < x1:
            ax.axvspan(x1, 100, color='w')  # красим вправо
        if x3 > x1:
            ax.axvspan(-100, x1, color='w')  # красим влево
    # если прямая горизонтальная
    elif y1 == y2:
        if y < y1:
            plt.fill_between(x, y, -1000, color='w')  # красим вниз
        if y > y1:
            plt.fill_between(x, y, 1000, color='w')  # красим вверх
    # если прямая наклонная
    else:
        if y3 > ((x3 - x1) * (y2 - y1) / (x2 - x1) + y1):
            plt.fill_between(x, y, -1000, color='w')  # красим вниз
        else:
            plt.fill_between(x, y, 1000, color='w')  # красим вверх
    # cust()
    # прямая
    ax.plot(x, y, color='g')
    # точка
    ax.scatter(x3, y3, marker='o', color="red")
    ax.add_patch(rect_)
    ax.add_patch(cir_)
    plt.savefig('fig.png')


# fig, ax = plt.subplots()
print(xo, yo, r)
F(xo, yo, r)
plt.savefig('fig.png')

pygame.init()
screen = pygame.display.set_mode((1000, 1000))

run = True
while run:
    im = pygame.image.load('fig.png')
    screen.blit(im, (0, 0))
    pygame.display.update()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                xo -= 1
            if event.key == pygame.K_d:
                xo += 1
            if event.key == pygame.K_w:
                yo += 1
            if event.key == pygame.K_s:
                yo -= 1
            print(xo, yo)
            F(xo, yo, r)
pygame.quit()
quit()



