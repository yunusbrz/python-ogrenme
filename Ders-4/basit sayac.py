import tkinter as tk

pencere = tk.Tk()
pencere.title("Sayaç")
pencere.geometry("400x300+35+35")
pencere.resizable(False,False)
pencere.config(bg="#D4D4D4")

x = 0
def click():
    global x
    x = x+1
    sayac.set(x)
def reset():
    global x
    sayac.set("0")
    x = 0
def butonhover(event):
    arti.config(bg="#DFDCDC")
def resethover(event):
    resetbuton.config(bg="#DFDCDC")
def buttonleave(event):
    arti.config(bg="white")
    resetbuton.config(bg="white")



sayac = tk.StringVar()
sayac.set("0")
label = tk.Label(
    text="Mini Sayaç",
    font=("Arial", 25, "bold"),
    bg="#D4D4D4",
    fg="Black"
)
sayaclbl = tk.Label(
    textvariable=sayac,
    font=("Arial", 20, "bold"),
    bg="#D4D4D4"
)
arti = tk.Button(
    text="+",
    font=("Arial", 20, "bold"),
    width="8",
    height="1",
    command=click
)
resetbuton = tk.Button(
    text="reset",
    font=("Arial", 20, "bold"),
    width="8",
    command=reset
)

arti.bind("<Enter>", butonhover)
arti.bind("<Leave>", buttonleave)
resetbuton.bind("<Enter>", resethover)
resetbuton.bind("<Leave>", buttonleave)
label.pack(pady=10)
sayaclbl.pack(pady=20)
arti.pack(pady=5)
resetbuton.pack(pady=10)
pencere.mainloop()