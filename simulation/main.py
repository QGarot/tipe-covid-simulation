from simulation.simulationc import Simulation


# Paramètres
height = 700
width = 700

stantard_contact = {
    "distance": 1,  # distance inférieure ou égale à 1 mètre en cas de contact...
    "durée": 5  # ... PENDANT une durée de 5 minutes
}

point_data = {
    "diameter": 20,
    "colors": ["green", "orange", "red"]
}

sim = Simulation(height, width, stantard_contact, point_data)
sim.put_points(20)
sim.create_attractor_point()
sim.display()

