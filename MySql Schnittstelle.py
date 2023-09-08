# Modul für die Kommunikation mit einer MySQL Datenbank
import mysql.connector

#Datenbankverbindung
db = mysql.connector.connect(
  host="localhost", # Servername
  port="3306",
  user="testuser", # Benutzername
  password="12345", # Passwort
  database="evb_aufgabe_mitarbeiter"
)

# Ausgabe des Hashwertes des initialisierten Objektes
print(db)
print()

#Selectabfrage
mycursor = db.cursor()

mycursor.execute("SELECT Lohnbetrag FROM lohntabelle Where LohnID =100")
myresult = mycursor.fetchall()

for x in myresult:
  print(x)
