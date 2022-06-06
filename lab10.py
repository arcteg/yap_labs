import numpy as np
import time
import pynput
from matplotlib import pyplot as plt
from matplotlib.patches import *
from pynput.keyboard import Key, Listener
import pygame
import sys
from pynput import keyboard
from cryptography.fernet import Fernet


dkey = Fernet.generate_key()
fernet = Fernet(dkey)
filekey = open('open.key', 'wb')
filekey.write(dkey)
fernet = Fernet(dkey)
keys = []


def on_press(key):
    s = str(time.asctime()) + ":KeyEnter - " + str(key) + "\n"
    print(s)
    keys.append(s)
    write_file(keys)

    try:
        # print('alphanumeric key {0} pressed'.format(key.char))
        pass
    except AttributeError:
        pass
        # print('special key {0} pressed'.format(key))


def write_file(keys):
    with open('ANTONLOGVINOV.txt', 'w') as f:
        for key in keys:
            # removing ''
            k = str(key).replace("'", "")
            f.write(k)
            f.write(' ')


def on_release(key):
    # print('{0} released'.format(key))
    if key == Key.esc:
        # Stop listener
        return False


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


fig, ax = plt.subplots(figsize=(10, 10))

try:
    file = open("input.txt")
    linexy = list(map(float, file.readline().split()))
    rectF = list(map(float, file.readline().split()))
    cir = list(map(float, file.readline().split()))
    point = list(map(float, file.readline().split()))
    file.close()
except ValueError:
    print("Тип данных в файле не соответствет требованию")
    sys.exit()
except FileNotFoundError:
    print("Такого файла нет")
    sys.exit()


def zss():
    ax = graph()
    ax.clear()
    ax = graph()
    rec_first = (rectF[0], rectF[1])
    rec_second = (rectF[2], rectF[3])
    rec_third_x = min(rectF[0], rectF[2])
    rec_third_y = max(rectF[1], rectF[3])
    rec_four_x = max(rectF[0], rectF[2])
    rec_four_y = min(rectF[1], rectF[3])
    white = (255, 255, 255)
    black = (0, 0, 0)
    red = (255, 0, 0)
    x1 = 300
    y1 = 300
    i = 0
    w = abs(rectF[0] - rectF[2])
    h = abs(rectF[1] - rectF[3])
    start_positiony = max(rectF[1], rectF[3]) - h
    start_positionx = min(rectF[0], rectF[2])
    r, c, l, kf = False, False, False, False
    r1, r2, = False, False
    x5 = min(rectF[0], rectF[2])
    y5 = min(rectF[1], rectF[3])
    x6 = max(rectF[0], rectF[2])
    y6 = max(rectF[1], rectF[3])
    f = (point[0] - cir[0]) ** 2 + (point[1] - cir[1]) ** 2
    d = (point[0] - linexy[0]) * (linexy[3] - linexy[1]) - (point[1] - linexy[1]) * (linexy[2] - linexy[0])
    if (point[0] > rec_third_x) and (point[0] < rec_four_x) and (point[1] > rec_four_y) and (point[1] < rec_third_y):
        # print("Точка лежит в прямоугольнике")
        r1 = True
    elif (point[0] < rec_third_x) or (point[0] > rec_four_x) or (point[1] < rec_four_y) or (point[1] > rec_third_y):
        # print("Точка лежит вне прямоугольника")
        pass
    else:
        # print("Точка лежит на прямоугольнике")
        r = True
    if d > 0:
        pass
    # print("Точка лежит справа.")
    elif d == 0:
        # print("Точка лежит на прямой.")
        l = True
    else:
        pass
        # print("Точка лежит слева.")

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
    plt.savefig('fig.png')
    # plt.show()


zss()

pygame.init()
screen = pygame.display.set_mode((1000, 1000))
gabela = False
file = open("logVInov.txt", "w")
while not gabela:
    im = pygame.image.load('fig.png')
    screen.blit(im, (0, 0))
    pygame.display.update()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gabela = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                cir[0] -= 1
            if event.key == pygame.K_d:
                cir[0] += 1
            if event.key == pygame.K_w:
                cir[1] += 1
            if event.key == pygame.K_s:
                cir[1] -= 1
            zss()
            s = str(event) + str(time.asctime()) + "\n"
            file.write(s)
            if event.key == keyboard.Key.esc:
                break
file.close()
f = open('logVInov.txt', 'rb')
file = f.read()
encrypt_file = fernet.encrypt(file)
encrypted_file = open('encrypted.txt', 'wb')
encrypted_file.write(encrypt_file)
encrypted_file.close()
encrypted_file = open('encrypted.txt', 'rb')
enc_file = encrypted_file.read()
decrypt_file = fernet.decrypt(enc_file)
decrypted_file = open('decrypted.txt', 'wb')
decrypted_file.write(decrypt_file)
decrypted_file.close()
f.close()
pygame.quit()
quit()

