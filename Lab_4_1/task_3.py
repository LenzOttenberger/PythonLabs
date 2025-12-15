from matplotlib import pyplot as plt
from matplotlib import patches as pt

fig, ax = plt.subplots()
ax.axis('off')

night = pt.Rectangle((0, 0), 1, 1, facecolor='blue')
ax.add_patch(night)

wall = pt.Rectangle((0, 0), 0.4, 0.7, facecolor='brown', edgecolor='black')
ax.add_patch(wall)

roof = pt.Polygon((
    (0, 0.7),
    (0.4, 0.7),
    (0.2, 0.8)
), facecolor='red', edgecolor='black')
ax.add_patch(roof)

window1 = pt.Rectangle((0.05, 0.1), 0.1, 0.15, facecolor='yellow', edgecolor='black')
ax.add_patch(window1)

window2 = pt.Rectangle((0.05, 0.3), 0.1, 0.15, facecolor='blue', edgecolor='black')
ax.add_patch(window2)

window3 = pt.Rectangle((0.25, 0.3), 0.1, 0.15, facecolor='yellow', edgecolor='black')
ax.add_patch(window3)

window4 = pt.Rectangle((0.05, 0.5), 0.1, 0.15, facecolor='yellow', edgecolor='black')
ax.add_patch(window4)

window5 = pt.Rectangle((0.25, 0.5), 0.1, 0.15, facecolor='blue', edgecolor='black')
ax.add_patch(window5)

door = pt.Rectangle((0.25, 0), 0.1, 0.25, facecolor='white', edgecolor='black')
ax.add_patch(door)

ddd = pt.Circle((0.33, 0.125), 0.01, facecolor='yellow', edgecolor='black')
ax.add_patch(ddd)

plt.title('Домик')
plt.show()