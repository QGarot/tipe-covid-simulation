from server.database import Database
from random import uniform


class HealthData:
    def __init__(self, user_id, db):
        """
        Cette classe permet de générer pour tout individu un objet contenant les données de santé essentielles.
        Pour ce travail on se limite à 3 types de données de santé, enregistrés dans une bdd :
        - Le premier correspond aux données de santé à caractère personnel (antécédents médicaux, maladies, traitements,
          handicap, etc...)

        - Le second correspond à des données relatives aux facteurs extrinsèques environnementaux non-personnels de
        santé (qualité de l'environnement évaluée en fonction de celle de l'eau ou de l'air, contexte régional)

        - Le troisième correspond à des données de contextualisation de la santé relative à l'individu (IMC,
        alimentation, consommation d'alcool/tabac, catégorie socioprofessionnelle, l'appartenance à une classe scolaire)

        # Les objets issus de cette classe sont construits à partir de la structure de la BDD #
        """

        self.user_id = user_id
        self.nb_types = len(db.select("id", "donnee_de_sante_categories"))
        self.data_health_types = [{} for _ in range(self.nb_types)]

        for i in range(self.nb_types):
            category_id = i + 1
            health_data = db.select("id", "données_de_sante", "categorie = " + str(category_id))
            for n_tuple in health_data:
                id = n_tuple[0]
                self.data_health_types[i][id] = None

    def generate(self):
        """
        TODO:
        Cette fonction génère des valeurs correspondant au types 1, 2 et 3 de manière aléatoire
        :return:
        """
        for data_health_type in self.data_health_types:
            for id in data_health_type.keys():
                data_health_type[id] = round(uniform(0, 1))

    def set_health_data(self, health_data_id, new_value):
        """
        Permet d'assigner une nouvelle valeur correspondant à la donnée de santé dont l'id est renseigné en paramètre.
        :param health_data_id:
        :param new_value:
        :return:
        """
        for health_data_type in self.data_health_types:
            if health_data_id in health_data_type.keys():
                health_data_type[health_data_id] = new_value

    def set_extra_data(self, db, health_data_id, info):
        """
        Permet d'ajouter des informations supplémentaires à un utilisateur selon une certaine donnée de santé.
        :param db:
        :param health_data_id:
        :param info:
        :return:
        """
        table_name = "utilisateurs_données_de_sante"
        attribute = "info_supplementaire"
        new_value = info
        condition = "donnee_id = " + str(health_data_id) + " AND utilisateur_id = " + str(self.user_id)
        db.update(table_name, attribute, new_value, condition)

    @staticmethod
    def get_db_attributes():
        """
        Retourne la chaîne de caractère correspondant aux attributs de la table 'utilisateurs_données_de_sante'.

        :return: str
        """
        return "(utilisateur_id, donnee_id, valeur, info_supplementaire)"

    def insert_in_db(self, db):
        """
        Cette méthode permet d'ajouter les données de santé enregistrées dans cet objet dans la table
        utilisateurs_données_de_sante.
        :param db:
        :return:
        """
        table_name = "utilisateurs_données_de_sante"
        structure = self.get_db_attributes()
        for data_health_type in self.data_health_types:
            for health_data_id, health_data_value in data_health_type.items():
                value = (self.user_id, health_data_id, health_data_value, "")
                db.insert(table_name, structure, value)
