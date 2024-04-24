import tkinter as tk
from tkinter import messagebox

class BankSystem:
    def __init__(self, root, user, other_user_balance_update):
        # Initialize the BankSystem instance with the given parameters
        self.root = root
        self.root.title(f"Advanced Banking System - {user}")

        # Initialize user balance with a default value of $1000
        self.balance = 1000

        # Create GUI elements for the user interface
        self.label_balance = tk.Label(root, text=f"{user} Balance: ${self.balance}")
        self.label_balance.pack(pady=5)

        self.entry_amount = tk.Entry(root, width=30)
        self.entry_amount.pack(pady=10)

        self.button_deposit = tk.Button(root, text="Deposit", command=self.deposit)
        self.button_deposit.pack(pady=5)

        self.button_withdraw = tk.Button(root, text="Withdraw", command=self.withdraw)
        self.button_withdraw.pack(pady=5)

        self.button_transfer = tk.Button(root, text="Transfer", command=self.transfer)
        self.button_transfer.pack(pady=5)

        # Reference to the balance update function of the other user
        self.other_user_balance_update = other_user_balance_update

    def update_balance_label(self):
        # Update the displayed balance label on the GUI
        self.label_balance.config(text=f"Balance: ${self.balance}")

    def deposit(self):
        try:
            # Attempt to convert the entered amount to a float
            amount = float(self.entry_amount.get())
            if amount > 0:
                # Deposit the amount if it is positive
                self.balance += amount
                self.update_balance_label()
            else:
                # Display a warning for an invalid positive amount
                messagebox.showwarning("Invalid Amount", "Please enter a valid positive amount.")
        except ValueError:
            # Display a warning for an invalid number input
            messagebox.showwarning("Invalid Input", "Please enter a valid number.")

    def withdraw(self):
        try:
            # Attempt to convert the entered amount to a float
            amount = float(self.entry_amount.get())
            if 0 < amount <= self.balance:
                # Withdraw the amount if it is within the balance
                self.balance -= amount
                self.update_balance_label()
            else:
                # Display a warning for an invalid withdrawal amount
                messagebox.showwarning("Invalid Amount", "Please enter a valid amount within your balance.")
        except ValueError:
            # Display a warning for an invalid number input
            messagebox.showwarning("Invalid Input", "Please enter a valid number.")

    def transfer(self):
        try:
            # Attempt to convert the entered amount to a float
            amount = float(self.entry_amount.get())
            if 0 < amount <= self.balance:
                # Transfer the amount to another user and update balances
                self.balance -= amount
                self.update_balance_label()
                # Update the other user's balance
                self.other_user_balance_update(amount)
            else:
                # Display a warning for an invalid transfer amount
                messagebox.showwarning("Invalid Amount", "Please enter a valid amount within your balance.")
        except ValueError:
            # Display a warning for an invalid number input
            messagebox.showwarning("Invalid Input", "Please enter a valid number.")

class BankingApp:
    def __init__(self, root):
        # Initialize the BankingApp instance with the main Tkinter window
        self.root = root
        self.root.title("Banking App")

        # Create GUI elements for user login
        self.label_username = tk.Label(root, text="Enter Username:")
        self.label_username.pack(pady=10)

        self.entry_username = tk.Entry(root, width=30)
        self.entry_username.pack(pady=10)

        self.button_login = tk.Button(root, text="Login", command=self.login)
        self.button_login.pack(pady=5)

        # Dictionary to store instances of BankSystem for each user
        self.users = {}

    def login(self):
        # Get the entered username from the login entry
        username = self.entry_username.get().strip()
        if username:
            if username not in self.users:
                # Create a new window for the user
                user_window = tk.Toplevel(self.root)
                # Create a BankSystem instance for the user
                self.users[username] = BankSystem(user_window, username, self.other_user_balance_update(username))
            else:
                # Display a warning for an already logged-in user
                messagebox.showwarning("User Exists", "User already logged in. Please choose a different username.")
        else:
            # Display a warning for an invalid username input
            messagebox.showwarning("Invalid Input", "Please enter a valid username.")

    def other_user_balance_update(self, username):
        # Define a function to update the balance of the other user
        def update_other_user_balance(amount):
            # Find the username of the other user
            other_username = [user for user in self.users.keys() if user != username][0]
            # Update the other user's balance
            self.users[other_username].balance += amount
            self.users[other_username].update_balance_label()

        return update_other_user_balance

if __name__ == "__main__":
    # Create the main Tkinter window
    root = tk.Tk()
    # Create an instance of the BankingApp
    banking_app = BankingApp(root)
    # Start the Tkinter event loop
    root.mainloop()
