import server.database

db = None
try:
    db = server.database.Database("127.0.0.1", "root", "", "tipe")
    print("Connecté à la BDD")
except:
    print("Une erreur est survenue lors de la connexion à la BDD.")


# Quelques tests
if db is not None:
    # SELECT
    print(db.get_cursor())
    test = db.query("SELECT * FROM contamines")
    print(test)
    print(db.get_cursor())

    # INSERT
    db.insert("INSERT INTO contamines (nom, prenom, age, nationalite) VALUES ('Jean', 'Pascal', 36, 'Française')")
    print(db.get_cursor())
