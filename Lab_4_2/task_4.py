import numpy as np
from scipy import integrate as it

def f(x):
    return np.sin(x)

result1, err1 = it.quad(f, 0, np.pi)
print('Definite integral sin(x)dx from 0 to pi =', result1)
print('Error: ', err1)

def g(x,y):
    return x**2 + y**2

result2, err2 = it.dblquad(g, 0, 1, lambda x: 0, lambda x: 2)
print('Double integral (x^2 + y^2)da on [0, 1]*[0, 2] =', result2)
print('Error: ', err2)
