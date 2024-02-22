from tkinter import ttk
import tkinter as tk



root = tk.Tk()
root.geometry("300x400")
root.title("Style Test")
style = ttk.Style()
style.configure("e.TEntery", font="iosevka 30")

e = ttk.Entry(root, style="e.TEntery")
e.pack()


root.mainloop()
