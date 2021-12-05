from simulation.simulationc import Simulation


# Paramètres
height = 700
width = 700

simulation = Simulation(height, width)
simulation.put_points(7)

simulation.display()
