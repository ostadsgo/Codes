
import tkinter as tk

root = tk.Tk()
root.title("Centered Text Label Example")
root.geometry("300x400")

label = tk.Label(root, text="Centered Text", anchor="center", justify="center")
label.pack(padx=10, pady=10)

root.mainloop()
