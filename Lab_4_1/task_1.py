from matplotlib import pyplot as plt
import math as m

interval_deg = [i for i in range(-360, 361)]
interval_rad = [m.radians(i) for i in interval_deg]

def f(x):
    return m.exp(m.cos(x)) + m.log(m.cos(0.6*x)**2 + 1) * m.sin(x)

def h(x):
    return -(m.log((m.cos(x) + m.sin(x))**2 + 2.5) + 10)

f_val = [f(i) for i in interval_rad]
h_val = [h(i) for i in interval_rad]

plt.plot(interval_rad, f_val, label="f(x)", color="red", linewidth=2, linestyle="-")
plt.plot(interval_rad, h_val, label="h(x)", color="blue", linewidth=2)
plt.legend()
plt.title('f(x) and h(x) graph')
plt.grid(True)
plt.xlabel('x')
plt.ylabel('f(x)')
plt.show()
