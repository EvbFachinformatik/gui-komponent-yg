import tkinter as gui

import mysql.connector

# Konfigurieren Sie die Verbindungsdaten zur Datenbank
db_config = {
    "host": "localhost",  # Adresse des Datenbankservers
    "port": 3306,  # Verbindungsport des Datenbankservers
    "user": "root",  # Benutzername für die Datenbank
    "password": "password",  # Passwort für den Datenbankbenutzer
    "database": "evb_aufgabe_mitarbeiter"  # Name der zu verwendenden Datenbank
}

def naechste_freie_id(tabellenname,id_name, schrittweite=10):
    try:
         # Starten Sie die Datenbankoperationen
        conn = mysql.connector.connect(**db_config)
        cursor = conn.cursor()

        cursor.execute(f"SELECT * FROM {tabellenname};")
        table_info = cursor.fetchall()

        print(table_info)

        if not table_info:
            raise ValueError(f"Ungültiger oder nicht vorhandener Tabellenname:: {tabellenname}")

         # Holen Sie sich die höchste ID in der Tabelle
        cursor.execute(f"SELECT MAX({id_name}) FROM {tabellenname}")

        max_id = cursor.fetchone()[0]
        # print(max_id)

        if max_id is None:
            max_id = 0

        # Berechnen und geben Sie die neue ID zurück
        next_id = max_id + schrittweite

        # Speichern Sie Datenbankoperationen und schließen Sie die Verbindung
        conn.commit()
        conn.close()

        return next_id

    except Exception as e:
        print("Error:", str(e))
        return -1

# Global eine Variable verwenden, um das aktuelle Modalfenster zu verfolgen
aktuelles_modal  = None

def suchen():
    global aktuelles_modal
    
    # Wenn bereits ein aktives Modal-Fenster existiert, verhindere das Öffnen eines neuen
    if aktuelles_modal is None or not aktuelles_modal.winfo_exists():
        aktuelles_modal = gui.Toplevel(window_python)
        aktuelles_modal.geometry("400x400")
        aktuelles_modal.title("Verfügbaren ID")

        table_name = eingabe_tablename.get()  # Den zu verarbeitenden Tabellennamen abrufen
        id_name = eingabe_idname.get()  # Den zu verarbeitenden ID-Namen abrufen

        new_id = naechste_freie_id(table_name,id_name)
        if new_id != -1:
            table_namelabel = gui.Label(aktuelles_modal, text=f"TabellenName : {table_name}")
            table_namelabel.pack(padx=20, pady=20)

            new_id_label = gui.Label(aktuelles_modal, text=f"Verfügbaren ID : {new_id}")
            new_id_label.pack(padx=20, pady=10)
        else:
            # Inhalt des Modal-Fensters
            label = gui.Label(aktuelles_modal, text="Tabellennamen oder ID-Namen ungültig oder nicht vorhanden")
            label.pack(padx=20, pady=20)

        # Schließen-Schaltfläche
        schließen_button = gui.Button(aktuelles_modal, text="Schließen", command=aktuelles_modal.destroy)
        schließen_button.pack(pady=10)

def speichern():
    return print('Speichern')

def abbrechen():
    return print('Abbrechen')

def hilfe():
    return print('Hilfe')

window_python = gui.Tk()
window_python.geometry("600x600")
window_python.title("Neuen Verfügbaren ID")

window_python.configure(bg="#E4F1FF")

# Eingabe Beschriftung und Eingabefeld
eingabe_label = gui.Label(window_python, text="Tabelle Name:")
eingabe_label.config(bg="#E4F1FF",font=16)
eingabe_label.grid(row=1, column=1, padx=10, pady=10, sticky="w")

eingabe_tablename = gui.Entry(window_python)
eingabe_tablename.config(width=40, bd=2, font=16)
eingabe_tablename.grid(row=1, column=1, padx=210, pady=10, sticky="w")

# Eingabe Beschriftung und Eingabefeld
eingabe_label = gui.Label(window_python, text="ID Name:")
eingabe_label.config(bg="#E4F1FF",font=16)
eingabe_label.grid(row=2, column=1, padx=10, pady=10, sticky="w")

eingabe_idname = gui.Entry(window_python)
eingabe_idname.config(width=40, bd=2, font=16)
eingabe_idname.grid(row=2, column=1, padx=210, pady=10, sticky="w")

# Suchen Button
suchen_button = gui.Button(window_python, text="Suchen", command=suchen)
suchen_button.config(width=20, bd=2, bg="#176B87", fg="white", highlightbackground="black", font=16)
suchen_button.grid(row=3, column=1, columnspan=2, padx=390, pady=10, sticky="w")

# # Speichern Button
# speichern_button = gui.Button(window_python, text="Speichern", command=speichern)
# speichern_button.config(width=20, bd=2, bg="#176B87", fg="white", highlightbackground="black", font=16)
# speichern_button.grid(row=4, column=1, columnspan=2, padx=390, pady=10, sticky="w")

# # Abbrechen Button
# abbrechen_button = gui.Button(window_python, text="Abbrechen", command=abbrechen)
# abbrechen_button.config(width=20, bd=2, bg="#176B87", fg="white", highlightbackground="black", font=16)
# abbrechen_button.grid(row=5, column=1, columnspan=2, padx=390, pady=10, sticky="w")

# # Hilfe Button
# hilfe_button = gui.Button(window_python, text="Hilfe", command=hilfe)
# hilfe_button.config(width=20, bd=2, bg="#176B87", fg="white", highlightbackground="black", font=16)
# hilfe_button.grid(row=6, column=1, columnspan=2, padx=390, pady=10, sticky="w")

window_python.mainloop()
