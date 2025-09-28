R = 8.31
pressure = float(input('Enter pressure (Pa): '))
volume = float(input('Enter volume (cbm): '))
temperature = float(input('Enter temperature (k): '))
p = (pressure*volume)/(R*temperature)
print(f'p = {round(p, 1)}')
