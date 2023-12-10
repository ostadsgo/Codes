from tkinter import ttk
import tkinter as tk



root = tk.Tk()
root.geometry("300x400")
root.title("Style Test")
style = ttk.Style()
style.configure("TEntry", font=("iosevka", 30))
e = ttk.Entry(root)
e.pack()


root.mainloop()
