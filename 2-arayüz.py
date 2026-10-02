import tkinter as tk
import winsound

Colors = {
    "bg": "#0B1647",
    "fg": "#D3D1D1",
    "button": "#",
    "text" : "#FFFFFF"
}
Fonts = {
    "title" : ("Arial", 25, "bold"),
    "normal": ("Arial", 15),
    "button": ("Arial", 14)
}
pencere = tk.Tk()
pencere.title("Ders-2")
pencere.geometry("400x300+30+30")
pencere.resizable(False,False)
pencere.config(bg=Colors["bg"])
pencere.iconbitmap("logo.ico")

def clear(event):
        userentry.delete(0, tk.END)
def clear2(event):
        passentry.delete(0, tk.END)
def click():
        username = userentry.get()
        password = passentry.get()
        userentry.delete(0, tk.END)
        passentry.delete(0, tk.END)        
        successfull.pack()
        print(f"Username: {username}\nPassword: {password}")
        winsound.MessageBeep()
        

loginlabel = tk.Label(
    pencere,
    text="Login",
    font=(Fonts["title"]),
    bg=Colors["bg"],
    fg=Colors["fg"]
)
successfull = tk.Label(
    pencere,
    text="Login Successfull",
    font=(Fonts["title"]),
    bg=Colors["bg"],
    fg=Colors["fg"]
)
userentry = tk.Entry(
    pencere,
    font=(Fonts["normal"]),
    borderwidth=1,
    highlightthickness=2,
    highlightcolor="#12257C",
    bg=Colors["fg"],
    fg="gray"
)
userentry.insert(0, "Username")

passentry = tk.Entry(
    pencere,
    font=(Fonts["normal"]),
    borderwidth=1,
    highlightthickness=2,
    highlightcolor="#12257C",
    bg=Colors["fg"],  
    fg="gray"
)
passentry.insert(0, "Password")

button = tk.Button(
    pencere,
    text="Enter",
    font=Fonts["button"],
    width=12,
    height=1,
    bg=Colors["fg"],
    command=click
)
userentry.bind("<FocusIn>", clear)
passentry.bind("<FocusIn>", clear2)



loginlabel.pack(pady=10)
userentry.pack(pady=6)
passentry.pack(pady=6)
button.pack(pady=10)
pencere.mainloop()