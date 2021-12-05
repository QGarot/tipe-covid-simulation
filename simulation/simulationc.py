import tkinter as tk
import random
from simulation.point import Point


class Simulation:
    def __init__(self, height, width):
        """
        Cette fonction créée une fenêtre dans laquelle se déroulera la simulation.
        :param height: hauteur de la fenêtre
        :param width: longueur de la fenêtre
        """

        self.height = height
        self.width = width
        self.window = tk.Tk()
        self.window.title("Simulation de la propagation d'un virus")
        self.canvas = tk.Canvas(self.window, width=700, height=700)

    def generate_color(self):
        return random.choice(['green', 'orange', 'red'])

    def put_points(self, n):
        point = None
        for i in range(n):
            (x, y) = (int(random.uniform(0, self.width - 20)), int(random.uniform(0, self.height - 20)))
            point = Point(x, y, self.generate_color(), self.canvas)
            point.draw()

    def display(self):
        self.canvas.pack()
        self.window.mainloop()
