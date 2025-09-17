p = float(input('Enter pressure (Pa): '))
v = float(input('Enter volume (cbm): '))
t = float(input('Enter temperature (k): '))
n = p*v/8.31*t
print(f'n = {round(n, 1)}')
