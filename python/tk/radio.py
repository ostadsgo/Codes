import tkinter as tk

def show_choice():
    print(f"You selected: {v.get()}")

root = tk.Tk()
v = tk.StringVar(value="Python")  # Default selection

tk.Label(root, text="Choose a programming language:").pack()

# Creating radio buttons
tk.Radiobutton(root, text="Python", variable=v, value="Python", command=show_choice).pack(anchor=tk.W)
tk.Radiobutton(root, text="Perl", variable=v, value="Perl", command=show_choice).pack(anchor=tk.W)
tk.Radiobutton(root, text="Java", variable=v, value="Java", command=show_choice).pack(anchor=tk.W)

root.mainloop()
