import tkinter as gui
import mipro_const as mipro

# Global eine Variable verwenden, um das aktuelle Modalfenster zu verfolgen
aktuelles_modal  = None

def suchen():
     return print('Suchen')
def speichern():
    return print('Speichern')

def abbrechen():
    return print('Abbrechen')

def hilfe():
    return print('Hilfe')

window_python = gui.Tk()
window_python.geometry("600x600")
window_python.title("Projekt Verwaltung")
window_python.configure(bg=mipro.HINTERGRUNDFARBE)

# Eingabe Beschriftung und Eingabefeld
eingabe_label = gui.Label(window_python, text="Projekt Name",bg=mipro.HINTERGRUNDFARBE)
eingabe_label.config(font=16)
eingabe_label.grid(row=1, column=1, padx=10, pady=10, sticky="w")

eingabe_eingabe = gui.Entry(window_python)
eingabe_eingabe.config(width=40, bd=2, font=16)
eingabe_eingabe.grid(row=1, column=1, padx=210, pady=10, sticky="w")

# Suchen Button
suchen_button = gui.Button(window_python, text="Suchen", command=suchen)
suchen_button.config(width=20, bd=2, bg="#176B87", fg="white", highlightbackground="black", font=16)
suchen_button.grid(row=3, column=1, columnspan=2, padx=390, pady=10, sticky="w")

# Speichern Button
speichern_button = gui.Button(window_python, text="Speichern", command=speichern)
speichern_button.config(width=20, bd=2, bg="#176B87", fg="white", highlightbackground="black", font=16)
speichern_button.grid(row=4, column=1, columnspan=2, padx=390, pady=10, sticky="w")

# Abbrechen Button
abbrechen_button = gui.Button(window_python, text="Abbrechen", command=abbrechen)
abbrechen_button.config(width=20, bd=2, bg="#176B87", fg="white", highlightbackground="black", font=16)
abbrechen_button.grid(row=5, column=1, columnspan=2, padx=390, pady=10, sticky="w")

# Hilfe Button
hilfe_button = gui.Button(window_python, text="Hilfe", command=hilfe)
hilfe_button.config(width=20, bd=2, bg="#176B87", fg="white", highlightbackground="black", font=16)
hilfe_button.grid(row=6, column=1, columnspan=2, padx=390, pady=10, sticky="w")

#Navigation Bar
navigation_frame = gui.Frame(window_python, padx=10,pady=10,bg="#E4F1FF")
navigation_frame.grid(row=7, column=0, columnspan=2, sticky="w")

button_jump_first = gui.Button(navigation_frame, text="|<")
button_jump_first.grid(row=0, column=0, padx=5, pady=5)

button_one_before = gui.Button(navigation_frame, text="<")
button_one_before.grid(row=0, column=1, padx=5, pady=5)

button_one_after = gui.Button(navigation_frame, text=">")
button_one_after.grid(row=0, column=2, padx=5, pady=5)

button_jump_last = gui.Button(navigation_frame, text=">|")
button_jump_last.grid(row=0, column=4, padx=5, pady=5)

window_python.mainloop()
