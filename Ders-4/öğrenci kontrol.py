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


def clear(event):
    event.widget.delete(0, tk.END)
def click():
    name = ad.get()
    surname = soyad.get()
    no = okulno.get()
    if name and surname and no:
        if name == "Adınız" or surname == "Soyadınız" or no == "Okul Numaranız":
            successfull.pack_forget()
            failure.pack()
        elif not name.replace(" ", "").isalpha() or not surname.replace(" ", "").isalpha() or not no.isdigit():
            successfull.pack_forget()
            failure.pack()
        else:
            failure.pack_forget()
            msg.set(f"Sisteme Hoşgeldin\n{name} {surname}")
            successfull.pack()




label = tk.Label(
    pencere,
    text="Öğrenci Kayıt Formu",
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

okulno = tk.Entry(
    pencere,
    font=Fonts["normal"],
    borderwidth=1,
    highlightthickness=2,
    highlightcolor=Colors["hl"],
    fg="gray"
)
okulno.insert(0, "Okul Numaranız")

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
okulno.bind("<FocusIn>", clear)
msg = tk.StringVar()


successfull = tk.Label(
    pencere,
    textvariable=msg,
    font=Fonts["title"],
    bg=Colors["bg"],
    fg="green"
)
failure = tk.Label(
    pencere,
    text="Lütfen Bilgileri\nTam ve Doğru Giriniz",
    font=Fonts["title"],
    bg=Colors["bg"],
    fg="red"
)


label.pack(pady=10)
ad.pack(pady=10)
soyad.pack(pady=10)
okulno.pack(pady=10)
enter.pack(pady=15)
successfull.pack_forget()
failure.pack_forget()
pencere.mainloop()