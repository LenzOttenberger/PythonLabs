import numpy as np

lengths = np.array(list(map(float, input('Enter lengths of all plots through the space: ').split())))
speeds = np.array(list(map(float, input('Enter speeds on all plots through the space: ').split())))
k = int(input('Enter a numb of a start plot: '))
p = int(input('Enter a number of a end plot: '))

lengths_sel = lengths[k-1:p]
speeds_sel = speeds[k-1:p]

S = np.sum(lengths_sel)
T = np.sum(lengths_sel / speeds_sel)
V = S / T

print(f'S = {S:.0f} km, T = {T:.2f} h, V = {V:.2f} km/h')
#S = 51 km, T = 1.12 h, V = 45.61 km/h почему расхождение с примером в методичке?