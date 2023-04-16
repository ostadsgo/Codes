import tkinter as tk


root = tk.Tk()
root.title("Draw Shapes")
canvas = tk.Canvas(root, width=500, height=400)
canvas.create_line(0, 0, 100, 200, fill="red")
canvas.create_rectangle(10, 10, 50, 50, fill="green")
canvas.create_polygon(400, 10, 300, 300, 500, 300, fill="blue")
canvas.pack()


root.mainloop()
