import numpy as np
import matplotlib.pyplot as plt

# Funkcja i jej pochodna
def f(x):
    return 3*x**3 - 2*x**2 + x - 5

def df(x):
    return 9*x**2 - 4*x + 1

x = np.linspace(-3, 3, 300)
y = f(x)
dy = df(x)

# Wykres
plt.figure(figsize=(8, 5))
plt.plot(x, y, label='f(x) = 3x³ - 2x² + x - 5')
plt.plot(x, dy, label="f'(x) = 9x² - 4x + 1", linestyle='--')
plt.axhline(0, color='gray', linestyle=':')
plt.legend()
plt.grid(True)
plt.title("Funkcja i jej pochodna")
plt.xlabel("x")
plt.ylabel("y")
plt.show()
