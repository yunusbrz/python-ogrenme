import tkinter as tk

Colors = {
    "bg": "#0B1647",
    "fg": "#D3D1D1",
    "buttonhover": "#8B8B8B",
    "text" : "#000000"
}
Fonts = {
    "title" : ("Arial", 20, "bold"),
    "normal": ("Arial", 15),
    "button": ("Arial", 14)
}

pencere = tk.Tk()
pencere.title("Ders-4")
pencere.geometry("400x300+30+30")
pencere.resizable(False,False)
pencere.iconbitmap("logo.ico")
pencere.config(bg=Colors["bg"])

def click():
    age = entry.get()
    if age.isdigit():
        age = int(age)
        if age >= 18:
            fail.pack_forget()
            smallage.pack_forget()
            successfull.pack()
        else:
            fail.pack_forget()
            successfull.pack_forget()
            smallage.pack()
    else:
        successfull.pack_forget()
        smallage.pack_forget()
        fail.pack()




label = tk.Label(
    pencere,
    text="Yaşınız",
    font=Fonts["title"],
    bg=Colors["bg"],
    fg=Colors["fg"]
)
successfull = tk.Label(
    pencere,
    text="Giriş Başarılı",
    font=Fonts["title"],
    bg=Colors["bg"],
    fg="green"
)
fail = tk.Label(
    pencere,
    text="Geçerli Bir Sayı Giriniz",
    font=Fonts["title"],
    bg=Colors["bg"],
    fg="red"
)
smallage = tk.Label(
    pencere,
    text="18 Yaşında veya Büyük Olmalısınız",
    font=Fonts["title"],
    bg=Colors["bg"],
    fg="red"
)
entry = tk.Entry(
    pencere,
    font=Fonts["normal"],
    borderwidth=2,
    highlightthickness=1,
    highlightcolor="#152779"
)
button = tk.Button(
    pencere,
    text="Enter",
    bg=Colors["fg"],
    font=Fonts["button"],
    width=7,
    command=click
)

label.pack(pady=10)
entry.pack(pady=15)
button.pack(pady=10)
successfull.pack_forget()
fail.pack_forget()
smallage.pack_forget()
pencere.mainloop()