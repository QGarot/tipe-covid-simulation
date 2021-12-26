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
        self.vectors = []  # Contient les vecteurs déplacement de chaque point de la simulation.
                           # Il sont unitaires, dirigé et orienté vers le point attracteur.

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
            self.vectors.append(point.get_vector(self.attractor_point))
            #point.draw_vector(point.get_vector(self.attractor_point))

    def attractor_point_zone(self):
        x0 = self.attractor_point.get_x() - self.attractor_point.get_diameter()/2
        y0 = self.attractor_point.get_y() - self.attractor_point.get_diameter()/2
        x1 = self.attractor_point.get_x() + self.attractor_point.get_diameter()/2
        y1 = self.attractor_point.get_y() + self.attractor_point.get_diameter()/2

        return x0, y0, x1, y1

    def run_animation(self):
        """
        TODO: Terminer l'animation.
        Déplacer tous les points vers le point attracteur tant qu'ils n'y sont pas.
        :return:
        """
        for i in range(len(self.points)):
            if not self.points[i].on_attractor:
                current_point = self.points[i]
                current_vector = self.vectors[i]
                current_point.move_to(current_vector, self.attractor_point)

        # Si la longueur de la liste des éléments qui touchent le point attracteur est strictement plus petites que le nombre de points, recommencer...
        x0, y0, x1, y1 = self.attractor_point_zone()
        if len(self.canvas.find_overlapping(x0, y0, x1, y1)) < len(self.points):
            self.canvas.after(10, self.run_animation)

    def display(self):
        self.canvas.pack()
        self.window.mainloop()
