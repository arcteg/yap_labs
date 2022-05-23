import numpy as np
from matplotlib import pyplot as plt   
from matplotlib.patches import *


xmin, xmax, ymin, ymax = -10, 10, -10, 10
ticks_frequency = 1


fig, ax = plt.subplots(figsize=(10, 10))
ax.set(xlim=(xmin-1, xmax+1), ylim=(ymin-1, ymax+1), aspect='equal')

ax.spines['bottom'].set_position('zero')
ax.spines['left'].set_position('zero')
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)

ax.set_xlabel('x', size=14, labelpad=-24, x=1.03)
ax.set_ylabel('y', size=14, labelpad=-21, y=1.02, rotation=0)

x_ticks = np.arange(xmin, xmax+1, ticks_frequency)
y_ticks = np.arange(ymin, ymax+1, ticks_frequency)

ax.set_xticks(x_ticks[x_ticks != 0])
ax.set_yticks(y_ticks[y_ticks != 0])
ax.set_xticks(np.arange(xmin, xmax+1), minor=True)
ax.set_yticks(np.arange(ymin, ymax+1), minor=True)

ax.grid(which='both', color='grey', linewidth=1, linestyle='-', alpha=0.2)

arrow_fmt = dict(markersize=4, color='black', clip_on=False)
ax.plot((1), (0), marker='>', transform=ax.get_yaxis_transform(), **arrow_fmt)
ax.plot((0), (1), marker='^', transform=ax.get_xaxis_transform(), **arrow_fmt)

    
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


r, c, l = False, False, False
x5 = min(rectF[0], rectF[2])
y5 = min(rectF[1], rectF[3])
x6 = max(rectF[0], rectF[2])
y6 = max(rectF[1], rectF[3])
f = (point[0] - cir[0]) ** 2 + (point[1] - cir[1]) ** 2
d = (point[0] - linexy[0]) * (linexy[3]-linexy[1]) - (point[1] - linexy[1]) * (linexy[2] - linexy[0])

if ((point[0] == x5 or point[0] == x6) and (point[1] <= point[1] <= point[1])) or ((point[1] == point[1] or point[1] == point[1]) and (x5 <= point[0] <= x6)):
    print('точка лежит на грани прямоугольника')
elif (x5 < point[0] < x6) and (point[1] < point[1] < point[1]):
    print('точка лежит внутри прямоугольника')
else:
    print('точка лежит вне прямоугольника')
    
if d > 0:
    print("Точка лежит справа.")
elif d == 0:
    print("Точка лежит на прямой.")
    l = True
else:
    print("Точка лежит слева.")

f = (point[0] - cir[0]) ** 2 + (point[1] - cir[1]) ** 2

if f < cir[2]**2:
    print('Точка лежит внутри круга.')
elif f == cir[2]**2:
    print('Точка лежит на круге.')
    c = True
else:
    print('Точка лежит снаружи круга.')


ax.plot((linexy[0], linexy[2]), (linexy[1], linexy[3]))

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

if d > 0:
    plt.fill_between(x=[linexy[0], linexy[2]], y1=[linexy[1], linexy[3]], y2=10, color="w", alpha=1)
else:
    plt.fill_between(x=[linexy[0], linexy[2]], y1=[linexy[1], linexy[3]], y2=-10, color="w", alpha=1)
ax.scatter(point[0], point[1], color="purple")
ax.add_patch(rect2)
ax.add_patch(circle2)
plt.show()
