import numpy as np
from matplotlib import pyplot as plt
from matplotlib.patches import *
import pygame
import sys


def graph():
    xmin, xmax, ymin, ymax = -10, 10, -10, 10
    ticks_frequency = 1

    ax.set(xlim=(xmin - 1, xmax + 1), ylim=(ymin - 1, ymax + 1), aspect='equal')

    ax.spines['bottom'].set_position('zero')
    ax.spines['left'].set_position('zero')
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)

    ax.set_xlabel('x', size=14, labelpad=-24, x=1.03)
    ax.set_ylabel('y', size=14, labelpad=-21, y=1.02, rotation=0)

    x_ticks = np.arange(xmin, xmax + 1, ticks_frequency)
    y_ticks = np.arange(ymin, ymax + 1, ticks_frequency)

    ax.set_xticks(x_ticks[x_ticks != 0])
    ax.set_yticks(y_ticks[y_ticks != 0])
    ax.set_xticks(np.arange(xmin, xmax + 1), minor=True)
    ax.set_yticks(np.arange(ymin, ymax + 1), minor=True)

    ax.grid(which='both', color='grey', linewidth=1, linestyle='-', alpha=0.2)

    arrow_fmt = dict(markersize=4, color='black', clip_on=False)
    ax.plot((1), (0), marker='>', transform=ax.get_yaxis_transform(), **arrow_fmt)
    ax.plot((0), (1), marker='^', transform=ax.get_xaxis_transform(), **arrow_fmt)
    return ax


fig, ax = plt.subplots(figsize=(100, 100))
ax = graph()
try:
    file = open("input.txt")
    linexy = list(map(float, file.readline().split()))
    rectF = list(map(float, file.readline().split()))
    cir = list(map(float, file.readline().split()))
    point = list(map(float, file.readline().split()))
    w = abs(rectF[0] - rectF[2])
    h = abs(rectF[1] - rectF[3])
    start_positiony = max(rectF[1], rectF[3]) - h
    start_positionx = min(rectF[0], rectF[2])
    file.close()
except ValueError:
    print("Тип данных в файле не соответствет требованию")
    sys.exit()
except FileNotFoundError:
    print("Такого файла нет")
    sys.exit()
r, c, l, kf = False, False, False, False
r1, r2, = False, False
x5 = min(rectF[0], rectF[2])
y5 = min(rectF[1], rectF[3])
x6 = max(rectF[0], rectF[2])
y6 = max(rectF[1], rectF[3])
f = (point[0] - cir[0]) ** 2 + (point[1] - cir[1]) ** 2
d = (point[0] - linexy[0]) * (linexy[3] - linexy[1]) - (point[1] - linexy[1]) * (linexy[2] - linexy[0])

# print("Введите координаты первой точки прямоугольника")
# rectF[0] = float(input())
# rectF[1] = float(input())
rec_first = (rectF[0], rectF[1])

# print("Введите координаты второй точки прямоугольника")
# rectF[2] = float(input())
# rectF[3] = float(input())
rec_second = (rectF[2], rectF[3])

rec_third_x = min(rectF[0], rectF[2])
rec_third_y = max(rectF[1], rectF[3])
rec_four_x = max(rectF[0], rectF[2])
rec_four_y = min(rectF[1], rectF[3])

gabela = False
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
x1 = 300
y1 = 300
i = 0
dis = pygame.display.set_mode((400, 600))

if (point[0] > rec_third_x) and (point[0] < rec_four_x) and (point[1] > rec_four_y) and (point[1] < rec_third_y):
    print("Точка лежит в прямоугольнике")
    r1 = True
elif (point[0] < rec_third_x) or (point[0] > rec_four_x) or (point[1] < rec_four_y) or (point[1] > rec_third_y):
    print("Точка лежит вне прямоугольника")
else:
    print("Точка лежит на прямоугольнике")
    r = True

"""if ((point[0] == x5 or point[0] == x6) and (point[1] <= point[1] <= point[1])) or (
        (point[1] == point[1] or point[1] == point[1]) and (x5 <= point[0] <= x6)):
    print('точка лежит на грани прямоугольника')
    r = True
elif (x5 < point[0] < x6) and (point[1] < point[1] < point[1]):
    print('точка лежит внутри прямоугольника')
else:
    print('точка лежит вне прямоугольника')
"""
if d > 0:
    print("Точка лежит справа.")
elif d == 0:
    print("Точка лежит на прямой.")
    l = True
else:
    print("Точка лежит слева.")

plt.ion()

while not gabela:
    f = (point[0] - cir[0]) ** 2 + (point[1] - cir[1]) ** 2

    if f < cir[2] ** 2:
        pass
        # print('Точка лежит внутри круга.')
    elif f == cir[2] ** 2:
        # print('Точка лежит на круге.')
        c = True
    else:
        # print('Точка лежит снаружи круга.')
        pass
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gabela = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                cir[0] -= 1

            elif event.key == pygame.K_d:
                cir[0] += 1

            elif event.key == pygame.K_w:
                cir[1] += 1

            elif event.key == pygame.K_s:
                cir[1] -= 1

            ax.clear()
            ax = graph()
            circle2 = plt.Circle(
                (cir[0], cir[1]), cir[2],
                color="Black",
                fill=False
            )
            rect2 = plt.Rectangle(
                (start_positionx, start_positiony), w, h,
                color="Black",
                fill=False, alpha=1
            )

            # !!!!plt.pause(0.1)
            if r or c or l:
                rect = plt.Rectangle(
                    (start_positionx, start_positiony), w, h,
                    color="Pink",
                    fill=False
                )
                circle1 = plt.Circle(
                    (cir[0], cir[1]), cir[2],
                    color="Pink",
                    fill=False, alpha=0.6
                )
                ax.add_patch(circle1)
                ax.add_patch(rect)
            else:
                if (x5 < point[0] < x6) and (y5 < point[1] < y6) and f < cir[2] ** 2:
                    rect = plt.Rectangle(
                        (start_positionx, start_positiony), w, h,
                        color="Pink",
                        fill=True
                    )
                    circle1 = plt.Circle(
                        (cir[0], cir[1]), cir[2],
                        color="Pink",
                        fill=False, alpha=0.6
                    )
                    ax.add_patch(circle1)
                    ax.add_patch(rect)
                else:
                    if f < cir[2] ** 2:
                        rect = plt.Rectangle(
                            (start_positionx, start_positiony), w, h,
                            color="White",
                            fill=True
                        )
                        circle1 = plt.Circle(
                            (cir[0], cir[1]), cir[2],
                            color="Pink",
                            fill=True, alpha=0.6
                        )
                        ax.add_patch(circle1)
                        ax.add_patch(rect)

                    else:
                        circle1 = plt.Circle(
                            (cir[0], cir[1]), cir[2],
                            color="Black",
                            fill=False

                        )
            if r1:
                rect = plt.Rectangle(
                    (start_positionx, start_positiony), w, h,
                    color="Pink",
                    fill=True
                )
                circle1 = plt.Circle(
                    (cir[0], cir[1]), cir[2],
                    color="White",
                    fill=True)
                kf = True
                ax.add_patch(rect)
                ax.add_patch(circle1)

            if d > 0:
                plt.fill_between(x=[linexy[0], linexy[2]], y1=[linexy[1], linexy[3]], y2=10, color="w", alpha=1)
            else:
                plt.fill_between(x=[linexy[0], linexy[2]], y1=[linexy[1], linexy[3]], y2=-10, color="w", alpha=1)

            ax.plot((linexy[0], linexy[2]), (linexy[1], linexy[3]))  # Постоянно вставлять
            ax.scatter(point[0], point[1], color="purple")
            ax.add_patch(rect2)
            ax.add_patch(circle2)
            plt.pause(0.1)
# plt.draw()
plt.ioff()

pygame.quit()
quit()
# ax.plot((linexy[0], linexy[2]), (linexy[1], linexy[3]))#Постоянно вставлять
# ax.scatter(point[0], point[1], color="purple")
# ax.add_patch(rect2)
# ax.add_patch(circle2)

# plt.show()
"""
       if i==0:
                ax.clear()
                ax = graph()
                #k = plt.Circle((cir[0],cir[1]),cir[2],)
                plt.draw()
                ax.plot((linexy[0], linexy[2]), (linexy[1], linexy[3]))#Постоянно вставлять
                ax.scatter(point[0], point[1], color="purple")
                ax.add_patch(rect2)
                ax.add_patch(circle2)
                #ax.add_patch(k)
                plt.pause(0.1)
            else:
                #k = plt.Circle((x,y),r,fill=False)
                #plt.draw()
                #ax.add_patch(k)
                #plt.plot(linex,liney)
                #plt.pause(0.1)
                ax.plot((linexy[0], linexy[2]), (linexy[1], linexy[3]))#Постоянно вставлять
                ax.scatter(point[0], point[1], color="purple")
                ax.add_patch(rect2)
                ax.add_patch(circle2)
    i+=1        
    dis.fill(white)
    pygame.draw.rect(dis, black, [x1, y1, 10, 10])
    pygame.display.update()
"""
