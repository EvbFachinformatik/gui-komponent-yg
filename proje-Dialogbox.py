import tkinter as tk
from tkinter import simpledialog


root = tk.Tk()
root.title("Dialogbox")


root.geometry("400x200")
root.configure(bg="lightblue")


def suche_durchfuehren():
    
    verwaltungsart = auswahl.get()

   
    if verwaltungsart == "M":
        titel = "Mitarbeiterverwaltung - Mitarbeitername"
        hinweis = "Bitte den gesuchten Mitarbeiternamen eingeben:"
    elif verwaltungsart == "P":
        titel = "Projektverwaltung - Projektname"
        hinweis = "Bitte den gesuchten Projektnamen eingeben:"
    else:
        titel = "Suche - Ungültiger Verwaltungstyp"
        hinweis = "Bitte einen Suchbegriff eingeben:"

    
    suchbegriff = simpledialog.askstring(titel, hinweis, parent=root)

    
    if suchbegriff is not None:
        suchbegriff = suchbegriff.strip()
        if suchbegriff:
            ergebnis_label.config(text=f"Suchergebnis: {suchbegriff}")
        else:
            ergebnis_label.config(text="Suche abgebrochen oder ungültiger Suchbegriff")
    else:
        ergebnis_label.config(text="Suche abgebrochen")


auswahl = tk.StringVar()
auswahl.set("M")  


auswahl_label = tk.Label(root, text="Wählen Sie die Verwaltung:", bg="lightblue", font=("Helvetica", 12))
auswahl_label.pack()

auswahl_menu = tk.OptionMenu(root, auswahl, "M", "P")
auswahl_menu.config(font=("Helvetica", 12), width=12, height=1)
auswahl_menu.pack()

rahmen_buttons = tk.Frame(root, bg="lightblue")  
rahmen_buttons.pack()

suchen_button = tk.Button(rahmen_buttons, text="Suchen", command=suche_durchfuehren, font=("Helvetica", 12), width=12, height=1)
suchen_button.pack(side=tk.LEFT, padx=5)

abbrechen_button = tk.Button(rahmen_buttons, text="Abbrechen", command=root.destroy, font=("Helvetica", 12), width=12, height=1)
abbrechen_button.pack(side=tk.RIGHT, padx=5)

ergebnis_label = tk.Label(root, text="", font=("Helvetica", 12))
ergebnis_label.pack()


root.mainloop()

