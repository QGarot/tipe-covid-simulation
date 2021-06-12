import matplotlib.pyplot as plt
import numpy as np
from scipy.integrate import odeint
import consts


# Les variations des grandeurs S(t), I(t) et R(t) => Dérivées ds/dt, di/dt, dr/dt
def variation(y, t, beta, gamma):
    s = y[0]
    i = y[1]
    r = y[2]
    dsdt = - beta * s * i
    didt = beta * s * i - gamma * i
    drdt = gamma * i
    return [dsdt, didt, drdt]



# Tableau représentant l'échelle du temps
t = np.linspace(0, 90, 90)
print(t)

# Intégration du système
sir = odeint(variation, [consts.S0, consts.I0, consts.R0], t, args=(consts.BETA, consts.GAMMA))
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
