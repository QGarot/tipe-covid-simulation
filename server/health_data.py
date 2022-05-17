class HealthData:
    def __init__(self):
        """
        Cette classe permet de générer pour tout individu un objet contenant les données de santé essentielles.
        Pour ce travail on se limite à 3 types de données de santé :
        - Le premier correspond aux données de santé à caractère personnel (antécédents médicaux, maladies, traitements,
          handicap, etc...)

        - Le second correspond à des données relatives aux facteurs extrinsèques environnementaux non-personnels de
        santé (qualité de l'environnement évaluée en fonction de celle de l'eau ou de l'air, contexte régional)

        - Le troisième correspond à des données de contextualisation de la santé relative à l'individu (IMC,
        alimentation, consommation d'alcool/tabac, catégorie socioprofessionnelle, l'appartenance à une classe scolaire)
        """

        self.user_id = None

        self.type1 = {
            "medical_background": None,
            "disease": None,
            "treatment": None,
            "handicap": None
        }

        self.type2 = {
            # Les qualités sont évaluées sur une échelle de 0 à 10
            "environmental_quality": None,
        }

        self.type3 = {
            # Body Mass Index = bmi = IMC
            "bmi": None,
            "alcohol": None,
            "tobacco": None,
            "school": None,
            "socio_professional_category": None,
        }

    def generate(self):
        """
        TODO:
        Cette fonction génère des valeurs correspondant au types 1, 2 et 3 de manière aléatoire
        :return:
        """
        pass

    @staticmethod
    def get_db_attributes() -> str:
        """
        Retourne la chaîne de caractère correspondant aux attributs de la table 'utilisateurs_données_de_sante'.

        :return: str
        """
        return "(utilisateur_id, donnee_id, valeur, info_supplementaire)"

    def get_personal_health_data(self):
        return self.type1

    def get_extrinsic_factors(self):
        return self.type2

    def get_contextualization_health_data(self):
        return self.type3

    def insert_db(self, db):
        """
        TODO:
        :param db:
        :return:
        """
        # Insertion des valeurs correspondant au type1
        # Insertion des valeurs correspondant au type2
        # Insertion des valeurs correspondant au type3
        pass

