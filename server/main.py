import server.database

connection_db = server.database.connection("127.0.0.1", "root", "", "tipe")
print(type(connection_db))
print(connection_db)
