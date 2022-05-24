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

    def SIR_data(self):
        s = 0
        i = 0
        r = 0
        for point in self.points:
            if point.is_contaminated():
                i = i + 1
            elif point.is_healthy():
                s = s + 1
            else:
                r = r + 1

        return s, i, r

    def generate_color(self):
        """
        Génère aléatoirement une couleur parmi le rouge le vert et le orange.
        :return: une couleur (de type string)
        """
        colors = self.point_data["colors"]
        return random.choice(colors)

    def generate_coord(self):
        """
        Retourne des coordonnées aléatoires pour un point de la fenêtre (contraintes en fonction des dimensions
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
        self.attractor_point = Point(x0, y0, self.point_data["diameter_attractor"], "black", self.canvas)
        self.attractor_point.draw()

    def put_points(self, n):
        """
        Positionne sur la fenêtre n points de coordonnées générées aléatoirement.
        :param n:
        :return: None
        """
        diameter = self.point_data["diameter"]
        self.create_attractor_point()
        for i in range(n):
            # On génère de manière aléatoire des coordonnées
            (x, y) = self.generate_coord()

            # On crée le point pour ensuite le dessiner dans la fenêtre
            point = Point(x, y, diameter, self.generate_color(), self.canvas)
            point.draw()
            # point.draw_vector(point.get_vector(self.attractor_point))

            # On met à jour les listes caractérisant la simulation
            self.points.append(point)
            self.vectors.append(point.get_vector(self.attractor_point))

        print("-----------------  Début de la simulation...  -----------------")

    def define_neighbors(self, point0):
        """
        Met à jour la liste des voisins de point0.
        Un point est considéré comme voisin de point0 s'il est situé à une distance inférieure à la distance de contact
        de point0.
        :param point0:
        :return:
        """
        contact_distance = self.standard_contact["distance"]
        for point in self.points:
            if point.is_in_ball(point0, contact_distance * 20):
                point0.add_neighbor(point)

    def run_animation(self):
        """
        TODO: Terminer l'animation.
        Déplacer tous les points vers le point attracteur tant qu'ils n'y sont pas.
        :return:
        """
        print("***********")
        all_point_on_attractor = True
        n = len(self.points)
        for i in range(n):
            point, vector = self.points[i], self.vectors[i]

            # 1) Si le point d'indice i n'est pas dans la zone du point attracteur, le faire avancer dans sa direction.
            if not point.is_on_point(self.attractor_point):
                point.move(vector)
                all_point_on_attractor = False

            # 2) Si le point d'indice i est rouge, mettre les points voisins en rouge sous certaines conditions...
            if point.is_contaminated():
                self.define_neighbors(point)
                for neighbor in point.neighbors:
                    neighbor.contaminate(self.standard_contact["beta"])

            # 4) Si deux points se touchent

        # Continuer la simulation tant que tous les points ne sont pas vers le point attracteur
        if not all_point_on_attractor:
            self.canvas.after(10, self.run_animation)
        else:
            print("-----------------  Fin de la simulation !  -----------------")

    def display(self):
        self.canvas.pack()
        self.window.mainloop()
