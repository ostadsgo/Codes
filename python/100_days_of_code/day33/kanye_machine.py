import tkinter as tk
from tkinter import ttk

import requests
from PIL import Image, ImageTk


def format_quote(quote: str):
    words = quote.split()
    i = 1
    q = ""
    for word in words:
        if i % 4 == 0:
            q += word + " " + "\n"
        else:
            q += word + " "
        i += 1
    return q


def get_quote():
    url = "https://api.kanye.rest"
    response = requests.get(url)
    quote = ""
    if response.status_code == 200:
        quote = response.json()["quote"]
    else:
        # raise appropriate exception based on response code.
        response.raise_for_status()

    quote = format_quote(quote)
    return quote


class QuoteUi(tk.Frame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        self.master = master

        imgfile = Image.open("./quote_cover.jpg")
        image = ImageTk.PhotoImage(imgfile)
        self.image_label = ttk.Label(
            self.master,
            text=get_quote(),
            image=image,
            compound="center",
            justify="center",
            font=("Helvica", 12),
        )
        self.image_label.image = image
        self.image_label.pack(fill="both", expand=True)

        ttk.Button(self.master, text="New Quote", command=self.new_quote).pack(
            fill="both", expand=True, pady=10, padx=10
        )

    def new_quote(self):
        self.image_label.config(text=get_quote())


class MainFrame(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        quote_ui = QuoteUi(master)
        quote_ui.pack()


class App(tk.Tk):
    def __init__(self):
        super().__init__()
        mainframe = MainFrame(self)
        mainframe.pack()


if __name__ == "__main__":
    app = App()
    app.mainloop()
