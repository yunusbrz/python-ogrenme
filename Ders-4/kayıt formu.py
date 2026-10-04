import tkinter as tk

Colors = {
    "bg": "#0B1647",
    "fg": "#D3D1D1",
    "buttonhover": "#8B8B8B",
    "text" : "#000000",
    "hl": "#1D36A5"
}
Fonts = {
    "title" : ("Arial", 20, "bold"),
    "normal": ("Arial", 15),
    "button": ("Arial", 14)
}

pencere = tk.Tk()
pencere.title("Ders-4")
pencere.geometry("450x500+30+30")
pencere.resizable(False,False)
pencere.iconbitmap("logo.ico")
pencere.config(bg=Colors["bg"])

def click():
    name = ad.get()
    surname = soyad.get()
    age = yas.get()
    if name and surname and age:
        successfull.pack()
    else:
        print("boş olamaz")
def clear(event):
    event.widget.delete(0, tk.END)




label = tk.Label(
    pencere,
    text="Kayıt Formu",
    font=Fonts["title"],
    bg=Colors["bg"],
    fg=Colors["fg"]
)
successfull = tk.Label(
    pencere,
    text="Hoşgeldiniz!",
    font=Fonts["title"],
    bg=Colors["bg"],
    fg=Colors["fg"]
)
ad = tk.Entry(
    pencere,
    font=Fonts["normal"],
    borderwidth=1,
    highlightthickness=2,
    highlightcolor=Colors["hl"],
    fg="gray"
)
ad.insert(0, "Adınız")

soyad = tk.Entry(
    pencere,
    font=Fonts["normal"],
    borderwidth=1,
    highlightthickness=2,
    highlightcolor=Colors["hl"],
    fg="gray"
)
soyad.insert(0, "Soyadınız")

yas = tk.Entry(
    pencere,
    font=Fonts["normal"],
    borderwidth=1,
    highlightthickness=2,
    highlightcolor=Colors["hl"],
    fg="gray"
)
yas.insert(0, "Yaşınız")

enter = tk.Button(
    pencere,
    text="Giriş",
    width=15,
    bg=Colors["fg"],
    font=Fonts["button"],
    command=click
)
ad.bind("<FocusIn>", clear)
soyad.bind("<FocusIn>", clear)
yas.bind("<FocusIn>", clear)


label.pack(pady=10)
ad.pack(pady=10)
soyad.pack(pady=10)
yas.pack(pady=10)
enter.pack(pady=15)
successfull.pack_forget
pencere.mainloop()