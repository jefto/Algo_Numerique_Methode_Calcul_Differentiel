from euler import euler_method, plot_euler
from runge_kutta_2 import runge_kutta_2, plot_runge_kutta_2
from runge_kutta_4 import runge_kutta_4, plot_runge_kutta_4

def menu():
    print("______________________________________________________________________________________________________")
    print("")
    print("Bienvenue sur la plateforme de Calcul Différentiel")
    print("______________________________________________________________________________________________________\n")
    print("")
    print("")
    print("|--------|")
    print("| Menu : |")
    print("|--------|")
    print("")
    print("Choisissez une méthode pour résoudre l'EDO :")
    print("1. Méthode d'Euler")
    print("2. Méthode de Runge-Kutta d'ordre 2")
    print("3. Méthode de Runge-Kutta d'ordre 4")
    print("4. Quitter")

def get_parameters():
    x0 = float(input("Entrez la valeur initiale de x (x0) : "))
    y0 = float(input("Entrez la valeur initiale de y (y0) : "))
    h = float(input("Entrez le pas (h) : "))
    n = int(input("Entrez le nombre d'itérations (n) : "))
    return x0, y0, h, n

def main():
    while True:
        menu()
        choice = input("Entrez votre choix : ")

        if choice == '1':
            x0, y0, h, n = get_parameters()
            f = lambda x, y: x + y  # Vous pouvez modifier cette fonction selon vos besoins
            x_values, y_values = euler_method(f, x0, y0, h, n)
            plot_euler(x_values, y_values)
        elif choice == '2':
            x0, y0, h, n = get_parameters()
            f = lambda x, y: x + y  # Vous pouvez modifier cette fonction selon vos besoins
            x_values, y_values = runge_kutta_2(f, x0, y0, h, n)
            plot_runge_kutta_2(x_values, y_values)
        elif choice == '3':
            x0, y0, h, n = get_parameters()
            f = lambda x, y: x + y  # Vous pouvez modifier cette fonction selon vos besoins
            x_values, y_values = runge_kutta_4(f, x0, y0, h, n)
            plot_runge_kutta_4(x_values, y_values)
        elif choice == '4':
            print("Au revoir!")
            break
        else:
            print("Choix invalide. Veuillez réessayer.")

if __name__ == "__main__":
    main()