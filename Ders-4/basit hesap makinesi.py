import tkinter as tk

Colors = {
    "bg": "#0B1647",
    "fg": "#D3D1D1",
    "buttonhover": "#8B8B8B",
    "text" : "#000000"
}
Fonts = {
    "title" : ("Arial", 20, "bold"),
    "normal": ("Arial", 17),
    "button": ("Arial", 14)
}

pencere = tk.Tk()
pencere.title("Ders-4")
pencere.geometry("500x400+30+30")
pencere.resizable(False,False)
pencere.iconbitmap("logo.ico")
pencere.config(bg=Colors["bg"])

def clear(event):
    number1.delete(0, tk.END)
def clear2(event):
    number2.delete(0, tk.END)

def click():
    sayı1 =number1.get()
    sayı2 =number2.get()
    if sayı1.isdigit() and sayı2.isdigit():
        sayı1 = int(sayı1)
        sayı2 = int(sayı2)
        sonuc = sayı1 + sayı2
        msg.set(f"Sonuç: {sonuc}")
        answer.pack()
        number1.delete(0, tk.END)
        number2.delete(0, tk.END)
    else:
        msg.set("Lütfen Geçerli Sayı Giriniz")
        answer.pack()


msg = tk.StringVar()
label = tk.Label(
    pencere,
    text="Basit Hesap Makinesi",
    font=Fonts["title"],
    bg=Colors["bg"],
    fg=Colors["fg"]
)
answer = tk.Label(
    pencere,
    textvariable=msg,
    font=Fonts["title"],
    bg=Colors["bg"],
    fg=Colors["fg"]
)
number1 = tk.Entry(
    pencere,
    font=Fonts["normal"],
    borderwidth=2,
    highlightthickness=2,
    highlightcolor="#1F39AF" ,
    fg="gray" 
)
number1.insert(0, "Sayı 1")
number2 = tk.Entry(
    pencere,
    font=Fonts["normal"],
    borderwidth=2,
    highlightthickness=2,
    highlightcolor="#1F39AF" ,
    fg="gray" 
)
number2.insert(0, "Sayı 2")

button = tk.Button(
    pencere,
    font=Fonts["button"],
    text="Topla",
    bg=Colors["fg"],
    width=15,
    command=click
)

number1.bind("<FocusIn>", clear)
number2.bind("<FocusIn>", clear2)
label.pack(pady=20)
number1.pack(pady=10)
number2.pack(pady=10)
button.pack(pady=8)
answer.pack_forget()
pencere.mainloop()