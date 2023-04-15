import mysql.connector

mydb = mysql.connector.connect(host="localhost", user="root", password="Troll1394@@@@", database="LaPlateforme")
mycursor = mydb.cursor()
mycursor.execute("select nom, capacite from salles")
resultats = mycursor.fetchall()

l = []
for resultat in resultats:
    l.append(resultat)
print(l)