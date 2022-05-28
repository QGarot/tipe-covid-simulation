from server.database import Database
from server.contact import Contact

db = Database("127.0.0.1", "root", "", "tipe")
contact = Contact((1, 3), 0)
contact.insert_in_db(db)

