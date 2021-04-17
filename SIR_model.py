import matplotlib.pyplot as plt
import numpy as np
from scipy.integrate import odeint

# Conditions initiales sur la population
POPULATION = 1000
I0 = 1
R0 = 0
S0 = POPULATION - I0 - R0

# Les taux

# BETA correspond au taux d'infection / probabilité d'être infecté après avoir été en contact avec un individu infecté
BETA = 0.8

# GAMMA correspond à la probabilité de ne plus pouvoir transmettre le virus
GAMMA = 0.05


# Les variations des grandeurs S(t), I(t) et R(t) => Dérivées ds/dt, di/dt, dr/dt
def variation(y, t, beta, gamma, n):
    s = y[0]
    i = y[1]
    r = y[2]
    dsdt = - beta * s * i / n
    didt = beta * s * i / n - gamma * i
    drdt = gamma * i
    return [dsdt, didt, drdt]



# Tableau représentant l'échelle du temps
t = np.linspace(0, 90, 90)
print(t)

# Intégration du système
sir = odeint(variation, [S0, I0, R0], t, args=(BETA, GAMMA, POPULATION))
print(sir)

# Affichage des courbes

plt.figure("Modèle SIR")
plt.title("Evolution de la taille des 3 catégories de personnes au cours du temps")
plt.xlabel("Temps (en jours)")
plt.ylabel("Population")

plt.plot(t, sir[:, 0], label="Sains")
plt.plot(t, sir[:, 1], label="Infectés")
plt.plot(t, sir[:, 2], label="Rétablis")

plt.legend()
plt.show()
