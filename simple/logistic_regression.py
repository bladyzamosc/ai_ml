import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LogisticRegression

# Dane
X = np.array([22, 25, 47, 52, 46, 56, 48, 55, 23]).reshape(-1, 1)
y = np.array([0, 0, 1, 1, 1, 1, 1, 1, 0])  # 0 = nie kupił, 1 = kupił

# Model logistyczny
model = LogisticRegression()
model.fit(X, y)

# Przewidzenie dla wieku 30
wiek = np.array([[30]])
prawdopodobieństwo = model.predict_proba(wiek)[0][1]
klasa = model.predict(wiek)[0]

print(f"Prawdopodobieństwo zakupu: {prawdopodobieństwo:.2f}")
print(f"Decyzja: {'Kupi' if klasa == 1 else 'Nie kupi'}")

# Wykres
x_plot = np.linspace(20, 60, 300).reshape(-1, 1)
y_prob = model.predict_proba(x_plot)[:, 1]

plt.plot(x_plot, y_prob, color='red', label='Prawdopodobieństwo zakupu')
plt.scatter(X, y, color='blue', label='Dane')
plt.axhline(0.5, color='gray', linestyle='--')
plt.xlabel('Wiek')
plt.ylabel('Prawdopodobieństwo zakupu')
plt.title('Regresja logistyczna')
plt.legend()
plt.grid(True)
plt.show()
