import tkinter as gui

window_python = gui.Tk()
#Überschrifft für Fenster
window_python.title("Projektverwaltung")

#Bezeichnung für das Eingabefeld
label_projekt_name = gui.Label(window_python, text="Projekt Name: ")
label_projekt_name.grid(row=0,column=0,padx=10,pady=30, sticky="e")

#Eingabefeld
projekt_name = gui.Entry(window_python)
projekt_name_wert = gui.StringVar()
projekt_name = gui.Entry(window_python, textvariable= projekt_name_wert)
projekt_name.grid(row=0,column=1,padx=10,pady=10,sticky="e")

#buttons um zu Speichern und Suchen Projekten
button_suchen = gui.Button(window_python, text="Suchen")
button_suchen.grid(row=1, column=3,pady=3,sticky="ew")

button_save = gui.Button(window_python,text="Speichern")
button_save.grid(row=2,column=3,pady=3,sticky="ew")

#Buttons um zu Hilfe und Abbrechen
button_cancel = gui.Button(window_python, text="Abbrechen")
button_cancel.grid(row=3, column=3,pady=3,sticky="ew")

button_help = gui.Button(window_python, text="Hilfe")
button_help.grid(row=4, column=3,pady=3,sticky="ew")

#Navigation Bar
navigation_frame = gui.Frame(window_python, padx=10,pady=10)
navigation_frame.grid(row=5, column=0, columnspan=2, sticky="w")

button_jump_first = gui.Button(navigation_frame, text="|<")
button_jump_first.grid(row=0, column=0, padx=5, pady=5)

button_one_before = gui.Button(navigation_frame, text="<<")
button_one_before.grid(row=0, column=1, padx=5, pady=5)

button_one_after = gui.Button(navigation_frame, text=">")
button_one_after.grid(row=0, column=2, padx=5, pady=5)

button_skip_5 = gui.Button(navigation_frame, text=">>")
button_skip_5.grid(row=0, column=3, padx=5, pady=5)

button_jump_last = gui.Button(navigation_frame, text=">|")
button_jump_last.grid(row=0, column=4, padx=5, pady=5)

window_python.mainloop()