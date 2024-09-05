from tkinter import ttk
import tkinter as tk



class Main:
    def __init__(self):
        self.root = tk.Tk()
        listbox1 = ttk.Listbox(self.root)
        listbox2 =  ttk.Listbox(self.root)
        listbox1.pack()
        listbox2.pack()
        listbox1.insert(0, "One")
        listbox1.insert(1, "Two")
        listbox1.insert(2, "Three")
        self.root.mainloop()


main = Main()
