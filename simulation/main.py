from simulation.simulationc import Simulation


# --------------------- Paramètres --------------------- #

height = 700
width = 700
scale = 25  # 25 pixels sur le dessin représente 1 mètre
n = 10  # Nombre d'individus à représenter

stantard_contact = {
    "distance": 1,  # distance inférieure ou égale à 1 mètre en cas de contact...
    "durée": 5,  # ... PENDANT une durée de 5 minutes
    "beta": 1  # Probabilité d'être infecté après avoir été en contact avec un individu infecté
}
point_data = {
    "diameter": 35,
    "colors": ["green", "orange", "red"],
    "diameter_attractor": 200
}

# --------------------- Simulation --------------------- #

sim = Simulation(height, width, stantard_contact, point_data, scale)
sim.put_points(n)
sim.display()

