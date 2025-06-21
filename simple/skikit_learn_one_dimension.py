# regresja liniowa
from sklearn.linear_model import LinearRegression
import numpy as np

# Sample data - heights and weights
heights = np.array([[160], [165], [170], [175], [180]])
weights = np.array([50, 60, 65, 70, 80])

# model
model = LinearRegression()
model.fit(heights, weights)

# Predict weight for a new height

print("Współczynnik (waga):", model.coef_)
print("Bias (przesunięcie):", model.intercept_)

print("Predicted weight for height 172 cm:", model.predict([[198]]))