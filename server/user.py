from server.database import Database
from server.health_data import HealthData


class User:
    def __init__(self, id, state):
        self.id = id
        self.state = state
        self.health_data = None

    @staticmethod
    def get_db_attributes() -> str:
        """
        Retourne la chaîne de caractère correspondant aux attributs de la table 'users'.

        :return: str
        """
        return "(id, etat)"

    def get_health_data(self):
        return self.health_data

    def initialize_health_data(self, db):
        """
        """
        self.health_data = HealthData(self.id, db)
        self.health_data.generate()

    def get_values(self):
        """
        Retourne les valeurs des attributs correspondant à cet objet.

        :return: tuple
        """
        return self.id, self.state

    def insert_in_db(self, db: Database):
        """
        Permet d'insérer les données de cet utilisateur dans la base de données indiquée en paramètre.

        :param db: Base de données
        :return:
        """
        db.insert("utilisateurs", self.get_db_attributes(), self.get_values())
        print("L'utilisateur " + str(self.id) + " a bien été enregistré dans la BDD !")
