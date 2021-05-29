import consts
import matplotlib.pyplot as plt

# Sains


def sir(points, tf, beta, gamma, y):

    # CI
    x = 0
    s = y[0]
    i = y[1]
    r = y[2]

    # Listes
    t = [0]
    y = [[s, i, r]]

    # Dérivées au points 0
    deriv_s = - beta * i * s
    deriv_i = beta * i * s - gamma * i
    deriv_r = gamma * i

    delta = tf / points

    # Méthode d'Euler
    for k in range(1, points + 1):
        print(k)
        x = x + delta

        # Calcul approximatif des images s, i et r, connaissant les dérivées
        s = s + delta * deriv_s
        i = i + delta * deriv_i
        r = r + delta * deriv_r
        t.append(x)
        y.append([s, i, r])

        # Dérivées aux points de coordonnées (x, s), (x, i) et (x, r)
        deriv_s = - beta * i * s
        deriv_i = beta * i * s - gamma * i
        deriv_r = gamma * i

    print(s, i, r)
    return t, y


sir_euler_method = sir(100, 90, consts.BETA, consts.GAMMA, [consts.S0, consts.I0, consts.R0])
t, y = sir_euler_method
s = [i[0] for i in y]
i = [i[1] for i in y]
r = [i[2] for i in y]

plt.figure("Modèle SIR")
plt.title("Evolution de la taille des 3 catégories de personnes au cours du temps")
plt.xlabel("Temps (en jours)")
plt.ylabel("Population")

plt.scatter(t, s, marker=".")
plt.scatter(t, i, marker=".")
plt.scatter(t, r, marker=".")

plt.show()
