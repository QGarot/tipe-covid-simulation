import matplotlib.pyplot as plt
import numpy as np
from scipy.integrate import odeint

# Conditions initiales sur la population
POPULATION = 1000
I0 = 1
R0 = 0
S0 = POPULATION - I0 - R0

# Vecteur représentant les 3 conditions initiales.
y0 = S0, I0, R0

# Les taux

# BETA correspond au taux d'infection / probabilité d'être infecté après avoir été en contact avec un individu infecté
BETA = 0.8

# GAMMA correspond à la probabilité de ne plus pouvoir transmettre le virus
GAMMA = 0.05


# Les variations des grandeurs S(t), I(t) et R(t) => Dérivées ds/dt, di/dt, dr/dt
def variation(y, t, beta, gamma):
    s, i, r = y
    dsdt = - beta * s * i
    didt = beta * s * i - gamma * i
    drdt = gamma * i
    return dsdt, didt, drdt


# Creation des tableaux

# Tableau représentant l'échelle du temps
t = np.linspace(0, 50)

# Intégration du système par rapport au temps
res = odeint(variation, y0, t, args=(BETA, GAMMA))

# Affichage des courbes

plt.figure("Modèle SIR")
plt.title("Evolution de la taille des 3 catégories de personnes au cours du temps")
plt.xlabel("Temps (en jours)")
plt.ylabel("Population")

plt.plot(t, res[:, 0], label="Sains")
plt.plot(t, res[:, 1], label="Infectés")
plt.plot(t, res[:, 2], label="Rétablis")

plt.legend()
plt.show()
