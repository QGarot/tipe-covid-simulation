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
        self.button = tk.Button(self.window, text="Lancer l'animation", command=self.run_animation)
        self.button.pack()

        # Paramètres de la simulation
        self.standard_contact = strd_contact  # Conditions nécessaires pour décrire un contact
        self.point_data = point_data  # Informations relatives à un point (son diamètre, sa couleur...)
        self.attractor_point = None
        self.points = []

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
        self.attractor_point = Point(x0, y0, 10, "black", self.canvas)
        self.attractor_point.draw()

    def put_points(self, n):
        """
        Positionne sur la fenêtre n points de coordonnées générées aléatoirement.
        :param n:
        :return: None
        """
        diameter = self.point_data["diameter"]
        self.create_attractor_point()
        for i in range(1, n + 1):
            (x, y) = self.generate_coord()
            point = Point(x, y, diameter, self.generate_color(), self.canvas)
            point.draw()
            self.points.append(point)
            # point.draw_vector(point.get_vector(self.attractor_point))

    def run_animation(self):
        """
        TODO: Terminer l'animation.
        :return:
        """
        print("Test " + str(self.canvas.find_all()))
        #for point in self.points:
        #    point.move_to(self.attractor_point)
        self.points[2].move_to(self.attractor_point)
        self.canvas.after(10, self.run_animation)

    def display(self):
        self.canvas.pack()
        self.window.mainloop()
