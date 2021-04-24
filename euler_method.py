import consts
import numpy as np
import matplotlib.pyplot as plt

# Sains
def sir(delta, tf, beta, gamma, population, y):

    # CI
    x = 0
    s = y[0]
    i = y[1]
    r = y[2]

    # Listes
    t = [0]
    y = [[s, i, r]]

    # Dérivées au points 0
    deriv_s = - beta * i * s / population
    deriv_i = beta * i * s / population - gamma * i
    deriv_r = gamma * i

    # Méthode d'Euler
    for i in range(1, int(tf // delta) + 1):
        x = x + delta * i

        # Calcul approximatif des images s, i et r, connaissant les dérivées
        s = s + delta * deriv_s
        i = i + delta * deriv_i
        r = r + delta * deriv_s
        t.append(x)
        y.append([s, i, r])

        # Dérivées aux points de coordonnées (x, s), (x, i) et (x, r)
        deriv_s = - beta * i * s / population
        deriv_i = beta * i * s / population - gamma * i
        deriv_r = gamma * i

    return t, y


sir_euler_method = sir(0.5, 90, consts.BETA, consts.GAMMA, consts.POPULATION, [consts.S0, consts.I0, consts.R0])
t, y = sir_euler_method
s = [i[0] for i in y]
i = [i[1] for i in y]
r = [i[2] for i in y]

plt.figure("Modèle SIR")
plt.title("Evolution de la taille des 3 catégories de personnes au cours du temps")
plt.xlabel("Temps (en jours)")
plt.ylabel("Population")

plt.plot(t, s, ":", label="Sains")
plt.plot(t, i, ":", label="Infectés")
plt.plot(t, r, ":", label="Rétablis")

#plt.xlim([0, 90])
plt.show()
   