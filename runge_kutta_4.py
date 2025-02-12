import matplotlib.pyplot as plt

def runge_kutta_4(f, x0, y0, h, n):
    x = x0
    y = y0
    x_values = [x]
    y_values = [y]
    
    print("______________________________________________________________________________________________________")
    print("")
    print("Bienvenue sur la plateforme de calcul différentiel par la methode de de Runge Kunta d'ordre 4")
    print("______________________________________________________________________________________________________\n")

    for i in range(n):
        k1 = h * f(x, y)
        k2 = h * f(x + 0.5 * h, y + 0.5 * k1)
        k3 = h * f(x + 0.5 * h, y + 0.5 * k2)
        k4 = h * f(x + h, y + k3)
        y = y + (k1 + 2 * k2 + 2 * k3 + k4) / 6
        x = x + h
        x_values.append(x)
        y_values.append(y)

    return x_values, y_values

def plot_runge_kutta_4(x_values, y_values):
    plt.plot(x_values, y_values, marker='o')
    plt.title("Méthode de Runge-Kutta d'ordre 4")
    plt.xlabel("x")
    plt.ylabel("y")
    plt.grid(True)
    plt.show()