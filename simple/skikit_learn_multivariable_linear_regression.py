# regresja liniowa
from sklearn.linear_model import LinearRegression
import numpy as np

# heights, ages, and BMI
X = np.array([ [160, 30, 22.0],
               [165, 35, 23.5],
               [170, 40, 24.0],
               [175, 45, 25.0],
               [180, 50, 26.0]])
# weights
y = np.array([55, 60, 65, 70, 75])

model = LinearRegression()
model.fit(X, y)

print("Wagi (współczynniki):", model.coef_)
print("Bias:", model.intercept_)

# Predict weight for a new data point
print("Waga osoby (172 cm, 38 lat, BMI 23.5):", model.predict([[198, 40, 27]]))