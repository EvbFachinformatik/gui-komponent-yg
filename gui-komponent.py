import tkinter as gui

def suchen():
    return print('Hallo Welt')

def speichern():
    return print('Speichern')

def abbrechen():
    return print('Abbrechen')

def hilfe():
    return print('Hilfe')

window_python = gui.Tk()
window_python.geometry("600x600")
window_python.title("gui-komponent")
window_python.configure(bg="#E4F1FF")

# Eingabe Beschriftung und Eingabefeld
eingabe_label = gui.Label(window_python, text="Name des Eingabefeldes1:")
eingabe_label.config(font=16)
eingabe_label.grid(row=1, column=1, padx=10, pady=10, sticky="w")

eingabe_eingabe = gui.Entry(window_python)
eingabe_eingabe.config(width=40, bd=2, font=16)
eingabe_eingabe.grid(row=1, column=1, padx=210, pady=10, sticky="w")

# Eingabe Beschriftung und Eingabefeld
eingabe_label = gui.Label(window_python, text="Name des Eingabefeldes2:")
eingabe_label.config(font=16)
eingabe_label.grid(row=2, column=1, padx=10, pady=10, sticky="w")

eingabe_eingabe = gui.Entry(window_python)
eingabe_eingabe.config(width=40, bd=2, font=16)
eingabe_eingabe.grid(row=2, column=1, padx=210, pady=10, sticky="w")

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

window_python.mainloop()
