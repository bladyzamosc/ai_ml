def f(x):
    return x**2 + 4*x + 3

def df(x):
    return 2*x + 4

x = 0.0  # start point
learning_rate = 0.1
epochs = 20

for i in range(epochs):
    grad = df(x)
    x = x - learning_rate * grad
    print(f"Iteracja {i+1}: x = {x:.4f}, f(x) = {f(x):.4f}")

print("\nMinimum znalezione w x =", round(x, 4))
