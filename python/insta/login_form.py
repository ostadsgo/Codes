import tkinter as tk
from tkinter import messagebox as msgbox
from tkinter import ttk


class Validation:
    def check_password(self, username, password):
        if username == "john" and password == "123":
            msgbox.showinfo("Success", "You're logged in successfuly.")
        else:
            msgbox.showerror("No Success", "Inccorect username or password")


class LoginForm(ttk.Frame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        self.master = master
        self.validation = Validation()

        # First row group
        first_group = ttk.Frame(self)
        ttk.Label(first_group, text="Username").grid(row=0, column=0, stick="w")
        username = ttk.Entry(first_group)
        username.grid(row=1, column=0, sticky="we")
        first_group.grid(row=0, column=0, sticky="we")
        first_group.columnconfigure(0, weight=1)

        # Second entry
        second_group = ttk.Frame(self)
        ttk.Label(second_group, text="Password").grid(row=0, column=0, sticky="w")
        password = ttk.Entry(second_group, show="*")
        password.grid(row=1, column=0, sticky="we")
        second_group.grid(row=1, column=0, sticky="we")
        second_group.columnconfigure(0, weight=1)

        # buttons
        buttons_frame = ttk.Frame(self)
        login_button = ttk.Button(buttons_frame, text="Login")
        login_button.grid(row=0, column=0, sticky="we")
        ttk.Button(buttons_frame, text="Cancel", command=self.master.destroy).grid(
            row=1, column=0, sticky="we", pady=5
        )
        buttons_frame.grid(row=2, column=0, sticky="we")
        buttons_frame.columnconfigure(0, weight=1)

        # Global config on all widgets
        for child in self.winfo_children():
            child.grid_configure(padx=5, pady=5)

        self.columnconfigure(0, weight=1)

    def on_login(self):
        pass


class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Login Form")
        self.geometry("200x180")
        # Login form
        login_form = LoginForm(self, padding=(10, 5))
        login_form.grid(row=0, column=0, sticky="wesn")
        self.rowconfigure(0, weight=1)
        self.columnconfigure(0, weight=1)


def main():
    app = App()
    app.mainloop()


if __name__ == "__main__":
    main()
