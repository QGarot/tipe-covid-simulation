from simulation.simulationc import Simulation
from server.database import Database


# --------------------- Paramètres --------------------- #

height = 700
width = 700
scale = 35  # 25 pixels sur le dessin représente 1 mètre
point_dimension = scale  # ODG Individu : 1m
n = 5  # Nombre d'individus à représenter

stantard_contact = {
    "distance": 1,  # distance inférieure ou égale à 1 mètre en cas de contact...
    "durée": 5,  # ... PENDANT une durée de 5 minutes
    "beta": 1  # Probabilité d'être infecté après avoir été en contact avec un individu infecté
}
point_data = {
    "diameter": point_dimension,
    "colors": ["green", "orange", "red"],
    "diameter_attractor": 200
}

db = Database("localhost", "root", "", "tipe")

# --------------------- Simulation --------------------- #

sim = Simulation(height, width, stantard_contact, point_data, scale, db)
sim.put_points(n)
sim.display()

