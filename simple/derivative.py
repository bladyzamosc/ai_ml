def f(x):
    return x**2

def derivative(f, x, h=1e-5):
    return (f(x + h) - f(x)) / h

print("Pochodna f(x)=x^2 w x=2:", derivative(f, 2))
