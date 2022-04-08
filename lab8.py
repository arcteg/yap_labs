from matplotlib import pyplot as plt


def sign():
    ax1.set_xlabel("Ось X", fontsize=15)
    ax1.set_ylabel("Ось Y", fontsize=15)
    ax2.set_xlabel("Ось X", fontsize=15)
    ax2.set_ylabel("Ось Y", fontsize=15)
    ax3.set_xlabel("Ось X", fontsize=15)
    ax3.set_ylabel("Ось Y", fontsize=15)


file = open("input.txt")
line_xy = list(map(float, file.readline().split()))
rect = list(map(float, file.readline().split()))
cir = list(map(float, file.readline().split()))
point = list(map(float, file.readline().split()))
print(line_xy)
w = abs(rect[0] - rect[2])
h = abs(rect[1] - rect[3])
start_position_x = max(rect[1], rect[3]) - h
start_position_y = min(rect[0], rect[2])
file.close()


figure = plt.figure()
ax1 = figure.add_subplot(2, 2, 1)
ax2 = figure.add_subplot(2, 2, 2)
ax3 = figure.add_subplot(2, 2, 3)
circle1 = plt.Circle(
    (cir[0], cir[1]), cir[2],
    color="Black",
    fill=False
)
rect = plt.Rectangle(
    (start_position_x, start_position_y), w, h,
    color="Green",
    fill=False
)
ax1.add_patch(circle1)
ax2.add_patch(rect)
ax3.plot((line_xy[0], line_xy[2]), (line_xy[1], line_xy[3]))
ax1.scatter(point[0], point[1], color="purple")
ax2.scatter(point[0], point[1], color="red")
ax3.scatter(point[0], point[1], color="grey")
sign()
plt.show()
