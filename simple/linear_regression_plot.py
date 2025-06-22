import numpy as np
import matplotlib.pyplot as plt

# Dane wejściowe (np. wzrost)
X = np.array([160, 165, 170, 175, 180])
# Dane wyjściowe (np. waga)
y = np.array([55, 60, 65, 70, 75])

# Oblicz parametry a i b ręcznie
# Wzory z matematyki: a = cov(X, y) / var(X), b = ȳ - a * x̄
x_mean = np.mean(X)
y_mean = np.mean(y)

a = np.sum((X - x_mean) * (y - y_mean)) / np.sum((X - x_mean)**2)
b = y_mean - a * x_mean

print(f"Model: y = {a:.2f} * x + {b:.2f}")

# Przewidujemy wartości
y_pred = a * X + b

# Wykres
plt.scatter(X, y, color='blue', label='Dane rzeczywiste')
plt.plot(X, y_pred, color='red', label='Regresja liniowa')
plt.xlabel('Wzrost (cm)')
plt.ylabel('Waga (kg)')
plt.title('Regresja liniowa: wzrost vs. waga')
plt.legend()
plt.grid(True)
plt.show()
