import matplotlib.pyplot as plt
import numpy as np
from scipy.integrate import odeint

# Conditions initiales sur la population
POPULATION = 1000
I0 = 1
R0 = 0
S0 = POPULATION - I0 - R0

y0 = S0, I0, R0

# Les taux
BETA = 0.8
GAMMA = 0.05


# Les variations des grandeurs S(t), I(t) et R(t)
def variation(y, t, beta, gamma):
    s, i, r = y
    dsdt = - beta * s * i
    didt = beta * s * i - gamma * i
    drdt = gamma * i
    return dsdt, didt, drdt


# Creation des tableaux
t = np.linspace(0, 50)

# Intégration du système
res = odeint(variation, y0, t, args=(BETA, GAMMA))

plt.figure("Modèle SIR")
plt.title("Evolution de la taille des 3 catégories de personnes au cours du temps")
plt.xlabel("Temps (en jours)")
plt.ylabel("Population")

plt.plot(t, res[:, 0], label="Sains")
plt.plot(t, res[:, 1], label="Infectés")
plt.plot(t, res[:, 2], label="Rétablis")

plt.legend()
plt.show()
