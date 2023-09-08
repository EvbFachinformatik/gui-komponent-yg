# import tkinter as gui

# import mysql.connector

# # import pymysql

# # Veritabanı bağlantı bilgilerini ayarlayın
# db_config = {
#     "host": "localhost",
#     "port": 3306,
#     "user": "root",
#     "password": "password",
#     "database": "evb_aufgabe_mitarbeiter"
# }

# # Veritabanına bağlanın
# # conn = pymysql.connect(**db_config)

# # Veritabanı işlemlerinizi yapın
# conn = mysql.connector.connect(**db_config)
# cursor = conn.cursor()

# # getTableMitarbeiter = 'select * from mitarbeiter'

# getTableMitarbeiterID ='SELECT MAX(MitarbeiterID) from mitarbeiter';

# cursor.execute(getTableMitarbeiterID)

# records=cursor.fetchall()


# print(records)

# # Bağlantıyı kapatın
# conn.close()


# # Global eine Variable verwenden, um das aktuelle Modalfenster zu verfolgen
# aktuelles_modal  = None

# def suchen():
#     global aktuelles_modal
    
#     # Wenn bereits ein aktives Modal-Fenster existiert, verhindere das Öffnen eines neuen
#     if aktuelles_modal is None or not aktuelles_modal.winfo_exists():
#         aktuelles_modal = gui.Toplevel(window_python)
#         aktuelles_modal.title("Suchen Modal")
        
#         # Inhalt des Modal-Fensters
#         label = gui.Label(aktuelles_modal, text="Inhalt des Modal-Fensters")
#         label.pack(padx=20, pady=20)
        
#         # Schließen-Schaltfläche
#         schließen_button = gui.Button(aktuelles_modal, text="Schließen", command=aktuelles_modal.destroy)
#         schließen_button.pack(pady=10)

# def speichern():
#     return print('Speichern')

# def abbrechen():
#     return print('Abbrechen')

# def hilfe():
#     return print('Hilfe')

# window_python = gui.Tk()
# window_python.geometry("600x600")
# window_python.title("gui-komponent")

# # window_python_width = 600
# # window_python_height = 600
# # screen_width = window_python.winfo_screenwidth()
# # screen_height = window_python.winfo_screenheight()
# # x = (screen_width / 2) - (window_python_width / 2)
# # y = (screen_height / 2) - (window_python_height / 2)
# # window_python.geometry(f"{window_python_width}x{window_python_height}+{int(x)}+{int(y)}")



# window_python.configure(bg="#E4F1FF")

# # Eingabe Beschriftung und Eingabefeld
# eingabe_label = gui.Label(window_python, text="Name des Eingabefeldes1:")
# eingabe_label.config(bg="#E4F1FF",font=16)
# eingabe_label.grid(row=1, column=1, padx=10, pady=10, sticky="w")

# eingabe_eingabe = gui.Entry(window_python)
# eingabe_eingabe.config(width=40, bd=2, font=16)
# eingabe_eingabe.grid(row=1, column=1, padx=210, pady=10, sticky="w")

# # Eingabe Beschriftung und Eingabefeld
# eingabe_label = gui.Label(window_python, text="Name des Eingabefeldes2:")
# eingabe_label.config(bg="#E4F1FF",font=16)
# eingabe_label.grid(row=2, column=1, padx=10, pady=10, sticky="w")

# eingabe_eingabe = gui.Entry(window_python)
# eingabe_eingabe.config(width=40, bd=2, font=16)
# eingabe_eingabe.grid(row=2, column=1, padx=210, pady=10, sticky="w")

# # Suchen Button
# suchen_button = gui.Button(window_python, text="Suchen", command=suchen)
# suchen_button.config(width=20, bd=2, bg="#176B87", fg="white", highlightbackground="black", font=16)
# suchen_button.grid(row=3, column=1, columnspan=2, padx=390, pady=10, sticky="w")

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



# # Veritabanı bağlantı bilgilerini ayarlayın
# db_config = {
#     "host": "localhost",
#     "port": 3306,
#     "user": "root",
#     "password": "password",
#     "database": "evb_aufgabe_mitarbeiter"
# }

# # Veritabanına bağlanın
# # conn = pymysql.connect(**db_config)

# # Veritabanı işlemlerinizi yapın
# conn = mysql.connector.connect(**db_config)
# cursor = conn.cursor()

# # getTableMitarbeiter = 'select * from mitarbeiter'

# getTableMitarbeiterID ='SELECT MAX(MitarbeiterID) from mitarbeiter';

# cursor.execute(getTableMitarbeiterID)

# records=cursor.fetchall()


# print(records)

# # Bağlantıyı kapatın
# conn.close()

# window_python.mainloop()
