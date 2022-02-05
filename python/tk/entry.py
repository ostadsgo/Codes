import tkinter as tk
from tkinter import ttk
from PIL import ImageTk, Image

root = tk.Tk()
root.title("Custom entry")

style = ttk.Style(root)
frame = ttk.Frame(root)
frame.pack()

ttk.Label(frame, text="First Name: ").pack(expand=True, fill="x")

image_file = Image.open("user.png")
image_file = image_file.resize((32, 32))
image = ImageTk.PhotoImage(image_file)
image_label = ttk.Label(frame, image=image)
image_label.image = image
image_label.pack(side=tk.LEFT)


entry = ttk.Entry(frame, width=20)
entry.pack(expand=True, fill=tk.BOTH)


root.mainloop()
