class Contact:
    def __init__(self, users, contamination):
        self.users = users
        self.contamination = contamination

    @staticmethod
    def get_db_attributes() -> str:
        """
        Retourne la chaîne de caractère correspondant aux attributs de la table 'users'.

        :return: str
        """
        return "(utilisateur1_id, utilisateur2_id, contamination)"
        
    def get_values(self):
        return self.get_users()[0], self.get_users()[1], self.contamination

    def get_users(self):
        return self.users
        
    def insert_in_db(self, db):
        db.insert("contact", self.get_db_attributes(), self.get_values())
