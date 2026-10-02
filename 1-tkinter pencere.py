import tkinter as tk


pencere = tk.Tk()
pencere.title("Ders-1")
pencere.geometry("300x200+20+20")
pencere.config(bg="#aeb4ae")
pencere.resizable(False,False)

x = 0
def click():
    global x
    x = x+1
    print(f"clicked the button {x} times")


button = tk.Button(
    pencere,
    text="Click",
    font=("Arial", 15, "bold"),
    bg="white",
    fg="black",
    activebackground="#d4d6d4",
    width=10,
    height=3,
    command=click
)

button.pack()
pencere.mainloop()