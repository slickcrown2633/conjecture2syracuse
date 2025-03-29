import time
import tkinter as tk

fenetre = tk.Tk()
fenetre.title("conjécture de Syracuse")
fenetre.config(bg="grey")
fenetre.geometry("1080x1920")
fenetre.mainloop()
while True:
    try:
        nombre = int(input("Choisis un nombre: "))
        if nombre <= 0:
            print("error")
            break
    except ValueError:
        print("error")
        break
itinerance = 0
print(f"très bien, tu as choisis {nombre}")
while True:
    if nombre % 2 == 0:
        print (f"{nombre} est pair")
        time.sleep(1.5)
        tk.Label = print (f"{nombre} / 2")
        nombre = nombre / 2
        time.sleep(1.5)
    elif nombre % 2 != 0:
        tk.Label = print (f"{nombre} est impair")
        time.sleep(1.5)
        tk.Label = print (f"{nombre} * 3 + 1")
        nombre = nombre * 3 + 1
        time.sleep(1.5)