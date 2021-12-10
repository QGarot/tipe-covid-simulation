import tkinter as tk
import random
from simulation.point import Point


class Simulation:
    def __init__(self, height, width, strd_contact, point_data):
        """
        Cette classe représente une fenêtre dans laquelle se déroulera la simulation.
        # TODO : faire la liste des différents paramètres.
        """

        # Paramètres de la fenêtre
        self.height = height
        self.width = width
        self.window = tk.Tk()
        self.window.title("Simulation de la propagation d'un virus")
        self.canvas = tk.Canvas(self.window, width=700, height=700)
        self.active = tk.Button(self.window, text="Animation", command=None)

        # Paramètres de la simulation
        self.points = []
        self.standard_contact = strd_contact  # Conditions nécessaires pour décrire un contact
        self.point_data = point_data  # Informations relatives à un point (son diamètre, sa couleur...)
        self.attractor_point = None

    def generate_color(self):
        """
        Génère aléatoirement une couleur parmi le rouge le vert et le orange.
        :return: une couleur (de type string)
        """
        colors = self.point_data["colors"]
        return random.choice(colors)

    def generate_coord(self):
        """
        Rtourne une coordonnée aléatoire pour un point de la fenêtre (contraintes en fonctions des dimensions
        de la fenêtre)
        :return: tuple sous la forme (x, y)
        """
        diameter = self.point_data["diameter"]  # Récupération du diamètre d'un point
        x = int(random.uniform(diameter, self.width - diameter))
        y = int(random.uniform(diameter, self.height - diameter))
        return x, y

    def create_attractor_point(self):
        """
        Positionne sur la fenêtre le point attracteur, ie le point qui génère des phénomènes de foule.
        Exemple : un concert, une école, etc...
        :return: None
        """
        (x0, y0) = self.generate_coord()
        attractor_point = Point(x0, y0, 10, "black", self.canvas)
        attractor_point.draw()

    def put_points(self, n):
        """
        Positionne sur la fenêtre n points de coordonnées générées aléatoirement.
        :param n:
        :return: None
        """
        point = None
        diameter = self.point_data["diameter"]
        for i in range(n):
            (x, y) = self.generate_coord()
            point = Point(x, y, diameter, self.generate_color(), self.canvas)
            self.points.append(point)
            point.draw()

    def display(self):
        self.canvas.pack()
        self.window.mainloop()
