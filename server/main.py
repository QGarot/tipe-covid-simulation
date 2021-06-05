import server.database
import server.user

db = None
try:
    db = server.database.Database("127.0.0.1", "root", "", "tipe")
    print("Connecté à la BDD")
except:
    print("Une erreur est survenue lors de la connexion à la BDD.")


# Quelques tests
if db is not None:
    # Nouvel utilisateur
    user1 = server.user.User("GAROT", "Quentin", 19, "Française")
    user1.insert_db(db)
