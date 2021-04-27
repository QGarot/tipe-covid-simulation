import tkinter as tk
import consts
import time

# Classes représentant un individu

class Person:
    def __init__(self, x, y, status):
        self.x = x
        self.y = y
        # Status : 0 -> Sains / 1 -> Infecté / 2 -> Rétabli
        self.status = status
        self.circle = None
        self.zone_contamination = None

    def move(self):
        """
        Prend comme argument l'objet canvas sur lequel on travaille.
        Cette fonction permet de déplacer de manière aléatoire la personne caractérisée par cet objet.
        """
        dx = 0.001
        dy = 0.001
        self.x = self.x + dx
        self.y = self.y + dy
        canvas.move(self.circle, self.x, self.x)
        canvas.move(self.zone_contamination, self.x, self.x)

        window.after(300, self.move)

    def draw(self, canvas, display_contamination):
        """
        Prend comme argument l'objet canvas sur lequel on travaille et un booleen
        qui permet d'afficher ou non la zone de contamination.
        Cette fonction dessine un cercle coloré pour représenté un individu.
        """
        radius = 10
        x0 = self.x - radius
        y0 = self.y - radius
        x1 = self.x + radius
        y1 = self.y + radius
        self.circle = canvas.create_oval(x0, y0, x1, y1, fill=self.color())

        if display_contamination:
            self.draw_zone_contamination(canvas)

    def draw_zone_contamination(self, canvas):
        x0 = self.x - consts.contamination_radius
        y0 = self.y - consts.contamination_radius
        x1 = self.x + consts.contamination_radius
        y1 = self.y + consts.contamination_radius
        self.zone_contamination = canvas.create_oval(x0, y0, x1, y1, outline="black", width=2)

    def color(self):
        """
        Fonction qui retourne la couleur correspondant à l'état de l'individu.
        Sains => Vert
        Malade => Rouge
        Rétabli => Orange
        """

        if self.status == 0:
            return "#11EE85"
        elif self.status == 1:
            return "#FF2F2F"
        else:
            return "#F3B33A"
    

# Création d'une fenêtre
window = tk.Tk()
window.title("Simulation de la propagation d'un virus")

# Zone de dessin
canvas = tk.Canvas(window, width=1080, height=720)

p = Person(50, 50, 0)
p.draw(canvas, display_contamination=True)

canvas.pack()

# Affichage de la fenêtre
window.mainloop()