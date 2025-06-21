import matplotlib
matplotlib.use('TkAgg') # Spróbuj najpierw tego
# Jeśli 'TkAgg' nie zadziała, odkomentuj poniższą linię i zakomentuj powyższą:
matplotlib.use('Qt5Agg')

import numpy as np
import matplotlib.pyplot as plt

data1 = np.random.normal(0, 1, 1000)
data2 = np.random.normal(3, 2, 1000)
data3 = np.random.normal(6, 8, 1000)

plt.hist(data1, bins=30, density=True, alpha=0.5, color='blue', label='N(0, 1)')
plt.hist(data2, bins=30, density=True, alpha=0.5, color='orange', label='N(3, 2)')
plt.hist(data3, bins=30, density=True, alpha=0.5, color='green', label='N(6, 8)')
plt.legend()
plt.title("Porównanie rozkładów N(0,1) i N(3,2)")
plt.xlabel("Wartość")
plt.ylabel("Gęstość")

plt.show()