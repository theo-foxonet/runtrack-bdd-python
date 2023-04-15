import mysql.connector

mydb = mysql.connector.connect(host="localhost", user="root", password="Troll1394@@@@", database="LaPlateforme")
mycursor = mydb.cursor()
mycursor.execute("select * from etudiants")
resultats = mycursor.fetchall()

for resultat in resultats:
  print(resultat)