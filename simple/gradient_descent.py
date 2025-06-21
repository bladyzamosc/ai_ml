# Przykład ręczny:
import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-5, 5, 100)
y = x**2
dy_dx = 2 * x  # pochodna analityczna f(x) = x^2

plt.plot(x, y, label='f(x) = x^2')
plt.plot(x, dy_dx, label="f'(x) = 2x", linestyle='--')
plt.axhline(0, color='gray', linestyle=':')
plt.legend()
plt.title("Funkcja i jej pochodna")
plt.show()
