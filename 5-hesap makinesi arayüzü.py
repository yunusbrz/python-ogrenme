import tkinter as tk
#  BU PROGRAM SADECE ARAYÜZDUR HESAP MAKİNESİ DEĞİLDİR ARAYÜZDEKİ YERLEŞİM MANTIĞINI DAHA NET ANLAMAK İÇİN YAPILMIŞTIR



Colors = {
    "bg": "#DADADA",
    "fg": "#C9C8C8",
    "buttonhover": "#8B8B8B",
    "text" : "#000000",
    "hl": "#FFFFFF"
}
Fonts = {
    "answer" : ("Arial", 18, "bold"),
    "normal": ("Arial", 20),
    "button": ("Arial", 14),
    "width" : "6",
    "heigth": "3"
}

pencere = tk.Tk()
pencere.title("Hesap Makinesi")
pencere.geometry("303x425+30+30")
pencere.resizable(False,False)
pencere.iconbitmap("logo.ico")
pencere.config(bg=Colors["bg"])
frame = tk.Frame(pencere)
label = tk.Label(
    pencere,
    text="125+18",
    font=Fonts["answer"],
    fg="black",
    bg=Colors["bg"],
    height=3
)
button1= tk.Button(
    frame,
    text="1",
    font=Fonts["button"],
    width=Fonts["width"],
    height=Fonts["heigth"],
    bg=Colors["fg"]
)
button2 = tk.Button(
    frame,
    text="2",
    font=Fonts["button"],
    width=Fonts["width"],
    height=Fonts["heigth"],
    bg=Colors["fg"]
)
button3 = tk.Button(
    frame,
    text="3",
    font=Fonts["button"],
    width=Fonts["width"],
    height=Fonts["heigth"],
    bg=Colors["fg"]
)
button4 = tk.Button(
    frame,
    text="4",
    font=Fonts["button"],
    width=Fonts["width"],
    height=Fonts["heigth"],
    bg=Colors["fg"]
)
button5 = tk.Button(
    frame,
    text="5",
    font=Fonts["button"],
    width=Fonts["width"],
    height=Fonts["heigth"],
    bg=Colors["fg"]
)
button6 = tk.Button(
    frame,
    text="6",
    font=Fonts["button"],
    width=Fonts["width"],
    height=Fonts["heigth"],
    bg=Colors["fg"]
)
button7 = tk.Button(
    frame,
    text="7",
    font=Fonts["button"],
    width=Fonts["width"],
    height=Fonts["heigth"],
    bg=Colors["fg"]
)
button8 = tk.Button(
    frame,
    text="8",
    font=Fonts["button"],
    width=Fonts["width"],
    height=Fonts["heigth"],
    bg=Colors["fg"]
)
button9 = tk.Button(
    frame,
    text="9",
    font=Fonts["button"],
    width=Fonts["width"],
    height=Fonts["heigth"],
    bg=Colors["fg"]
)
button0 = tk.Button(
    frame,
    text="0",
    font=Fonts["button"],
    width=Fonts["width"],
    height=Fonts["heigth"],
    bg=Colors["fg"]
)
buttonvirgül = tk.Button(
    frame,
    text=",",
    font=Fonts["button"],
    width=Fonts["width"],
    height=Fonts["heigth"],
    bg=Colors["fg"]
)
buttonböl = tk.Button(
    frame,
    text="÷",
    font=Fonts["button"],
    width=Fonts["width"],
    height=Fonts["heigth"],
    bg=Colors["fg"]
)
buttoncarp = tk.Button(
    frame,
    text="X",
    font=Fonts["button"],
    width=Fonts["width"],
    height=Fonts["heigth"],
    bg=Colors["fg"]
)
buttoncikar = tk.Button(
    frame,
    text="-",
    font=Fonts["button"],
    width=Fonts["width"],
    height=Fonts["heigth"],
    bg=Colors["fg"]
)
buttontopla = tk.Button(
    frame,
    text="+",
    font=Fonts["button"],
    width=Fonts["width"],
    height=Fonts["heigth"],
    bg=Colors["fg"]
)
buttonesittir = tk.Button(
    frame,
    text="=",
    font=Fonts["button"],
    width=Fonts["width"],
    height=Fonts["heigth"],
    bg=Colors["fg"]
)

label.pack(side="top", fill="x")
frame.pack(expand=True, fill="both")
button1.grid(row=3, column=1)
button2.grid(row=3, column=2)
button3.grid(row=3, column=3)
buttoncikar.grid(row=3, column=4)
button4.grid(row=2, column=1)
button5.grid(row=2, column=2)
button6.grid(row=2, column=3)
buttoncarp.grid(row=2, column=4)
button7.grid(row=1, column=1)
button8.grid(row=1, column=2)
button9.grid(row=1, column=3)
buttonböl.grid(row=1, column=4)
button0.grid(row=4, column=2)
buttonvirgül.grid(row=4, column=1)
buttonesittir.grid(row=4, column=3)
buttontopla.grid(row=4, column=4)
pencere.mainloop()