from matplotlib import pyplot as plt

interval = [i for i in range(-10, 11)]

def f(x):
    if x**2 - 9 != 0:
        return 5 / (x ** 2 - 9)
    else:
        return None

f_val = [f(i) for i in interval]

plt.plot(interval, f_val, label="f(x)", color="red", linewidth=2, linestyle="-")
plt.legend()
plt.grid(True)
plt.title("f(x)")
plt.xlabel("x")
plt.ylabel("f(x)")
plt.show()



