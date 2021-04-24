# Conditions initiales sur la population
POPULATION = 1000
I0 = 1
R0 = 0
S0 = POPULATION - I0 - R0

# Les taux

# BETA correspond au taux d'infection / probabilité d'être infecté après avoir été en contact avec un individu infecté
BETA = 0.5

# GAMMA correspond à la probabilité de ne plus pouvoir transmettre le virus
GAMMA = 0.05