import mysql.connector

conn = mysql.connector.connect( host="localhost", user="root", password="Troll1394@@@@", database="laplateforme")

cursor = conn.cursor()

query = "SELECT employes.nom, employes.prenom, service.nom FROM employes JOIN service ON employes.id_service = service.id"
cursor.execute(query)

for (nom, prenom, service) in cursor:
    print(f"{nom} {prenom} travaille dans le service {service}")

cursor.close()
conn.close()
