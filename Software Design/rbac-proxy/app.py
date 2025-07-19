import tkinter as tk
from tkinter import messagebox
from enum import Enum


class Role(Enum):
    ADMIN = "admin"
    USER = "user"
    GUEST = "guest"


class User:
    def __init__(self, username, password, role):
        self.username = username
        self.password = password
        self.role = role

    def check_password(self, password):
        return self.password == password

    def get_username(self):
        return self.username

    def get_role(self):
        return self.role


class AuthenticationSystem:
    def __init__(self):
        self.users = []

    def add_user(self, user):
        self.users.append(user)

    def check_credentials(self, username, password):
        for user in self.users:
            if user.get_username() == username and user.check_password(password):
                return True
        return False

    def get_user_role(self, username):
        for user in self.users:
            if user.get_username() == username:
                return user.get_role()
        return None


class Resource:
    def read(self):
        print("Reading from the resource")

    def write(self):
        print("Writing to the resource")

    def modify(self):
        print("Modifying the resource")


class Proxy:
    def __init__(self, auth_system, username=None, password=None):
        self.resource = Resource()
        self.auth_system = auth_system
        self.username = username
        self.password = password

    def check_credentials(self):
        if self.auth_system.check_credentials(self.username, self.password):
            return True
        else:
            print("Access denied: Invalid credentials")
            return False

    def check_role(self, required_role):
        role = self.auth_system.get_user_role(self.username)
        if role and role == required_role:
            return True
        print(f"Access denied: Insufficient permissions. Required role: {required_role}, User role: {role}")
        return False

    def read(self):
        if self.check_credentials() and self.check_role(Role.USER):
            self.resource.read()

    def write(self):
        if self.check_credentials() and self.check_role(Role.ADMIN):
            self.resource.write()

    def modify(self):
        if self.check_credentials() and self.check_role(Role.ADMIN):
            self.resource.modify()

class Application:
    def __init__(self, auth_system):
        self.auth_system = auth_system
        self.current_user = None

    def login(self, username, password):
        if self.auth_system.check_credentials(username, password):
            for user in self.auth_system.users:
                if user.get_username() == username:
                    self.current_user = user
                    return True
        return False

    def logout(self):
        self.current_user = None

    def is_logged_in(self):
        return self.current_user is not None


# Create Default Users
auth_system = AuthenticationSystem()
auth_system.add_user(User("admin", "adminpass", Role.ADMIN))
auth_system.add_user(User("user", "userpass", Role.USER))
auth_system.add_user(User("guest", "guestpass", Role.GUEST))

app = Application(auth_system)


class LoginWindow:
    def __init__(self, root):
        self.root = root
        self.root.title("Login System")

        self.username_label = tk.Label(root, text="Username")
        self.username_label.pack()
        self.username_entry = tk.Entry(root)
        self.username_entry.pack()

        self.password_label = tk.Label(root, text="Password")
        self.password_label.pack()
        self.password_entry = tk.Entry(root, show="*")
        self.password_entry.pack()

        self.login_button = tk.Button(root, text="Login", command=self.login)
        self.login_button.pack()

        self.logout_button = tk.Button(root, text="Logout", command=self.logout)
        self.logout_button.pack()

        self.read_button = tk.Button(root, text="Read Resource", command=self.read)
        self.read_button.pack()

        self.write_button = tk.Button(root, text="Write Resource", command=self.write)
        self.write_button.pack()

        self.modify_button = tk.Button(root, text="Modify Resource", command=self.modify)
        self.modify_button.pack()

        self.status_label = tk.Label(root, text="")
        self.status_label.pack()

    def login(self):
        username = self.username_entry.get()
        password = self.password_entry.get()
        if app.login(username, password):
            self.status_label.config(text=f"Logged in as {username}")
        else:
            messagebox.showerror("Login failed", "Invalid credentials")

    def logout(self):
        app.logout()
        self.status_label.config(text="Logged out")

    def read(self):
        if app.is_logged_in():
            proxy = Proxy(auth_system, app.current_user.get_username(), app.current_user.password)
            proxy.read()
        else:
            messagebox.showerror("Access Denied", "Please login first")

    def write(self):
        if app.is_logged_in():
            proxy = Proxy(auth_system, app.current_user.get_username(), app.current_user.password)
            proxy.write()
        else:
            messagebox.showerror("Access Denied", "Please login first")

    def modify(self):
        if app.is_logged_in():
            proxy = Proxy(auth_system, app.current_user.get_username(), app.current_user.password)
            proxy.modify()
        else:
            messagebox.showerror("Access Denied", "Please login first")


if __name__ == "__main__":
    root = tk.Tk()
    login_window = LoginWindow(root)
    root.mainloop()
