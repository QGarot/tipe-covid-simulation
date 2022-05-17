from simulation.simulationc import Simulation


# --------------------- Paramètres --------------------- #

height = 700
width = 700
scale = 25  # 25 pixels sur le dessin représente 1 mètre
n = 52  # Nombre d'individus à représenter

stantard_contact = {
    "distance": 1,  # distance inférieure ou égale à 1 mètre en cas de contact...
    "durée": 5  # ... PENDANT une durée de 5 minutes
}
point_data = {
    "diameter": 20,
    "colors": ["green", "orange", "red"]
}

# --------------------- Simulation --------------------- #

sim = Simulation(height, width, stantard_contact, point_data)
sim.put_points(n)
sim.display()

