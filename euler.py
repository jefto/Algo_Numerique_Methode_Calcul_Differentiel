import matplotlib.pyplot as plt

def euler_method(f, x0, y0, h, n):
    x = x0
    y = y0
    x_values = [x]
    y_values = [y]

    print("______________________________________________________________________________________________________")
    print("")
    print("Bienvenue sur la plateforme de calcul différentiel par la methode de d'Eulère")
    print("______________________________________________________________________________________________________\n")

    for i in range(n):
        y = y + h * f(x, y)
        x = x + h
        x_values.append(x)
        y_values.append(y)

    return x_values, y_values

def plot_euler(x_values, y_values):
    plt.plot(x_values, y_values, marker='o')
    plt.title("Méthode d'Euler")
    plt.xlabel("x")
    plt.ylabel("y")
    plt.grid(True)
    plt.show()