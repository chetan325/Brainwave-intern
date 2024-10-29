import tkinter as tk
from tkinter import messagebox, simpledialog
import sqlite3
import bcrypt
from datetime import datetime

class InventoryApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Inventory Management System")
        self.geometry("600x400")

        self.login_frame = tk.Frame(self)
        self.inventory_frame = tk.Frame(self)

        self.show_login_screen()

    def show_login_screen(self):
        self.login_frame.pack(fill="both", expand=True)
        tk.Label(self.login_frame, text="Username").grid(row=0, column=0)
        tk.Label(self.login_frame, text="Password").grid(row=1, column=0)

        self.username_entry = tk.Entry(self.login_frame)
        self.password_entry = tk.Entry(self.login_frame, show="*")

        self.username_entry.grid(row=0, column=1)
        self.password_entry.grid(row=1, column=1)

        tk.Button(self.login_frame, text="Login", command=self.login).grid(row=2, column=0, columnspan=2)
        tk.Button(self.login_frame, text="Register", command=self.show_registration_screen).grid(row=3, column=0, columnspan=2)

    def show_registration_screen(self):
        username = simpledialog.askstring("Register", "Enter username:")
        password = simpledialog.askstring("Register", "Enter password:", show="*")
        if username and password:
            register_user(username, password)

    def login(self):
        username = self.username_entry.get()
        password = self.password_entry.get()
        if login_user(username, password):
            self.login_frame.pack_forget()
            self.show_inventory_screen()

    def show_inventory_screen(self):
        self.inventory_frame.pack(fill="both", expand=True)
        tk.Button(self.inventory_frame, text="Add Product", command=self.add_product_screen).pack()
        tk.Button(self.inventory_frame, text="View Low Stock", command=self.check_low_stock).pack()
        tk.Button(self.inventory_frame, text="Record Sale", command=self.record_sale_screen).pack()
        tk.Button(self.inventory_frame, text="Sales Summary", command=self.sales_summary).pack()
        tk.Button(self.inventory_frame, text="Logout", command=self.logout).pack()

    def add_product_screen(self):
        self.product_name = simpledialog.askstring("Add Product", "Enter product name:")
        self.product_category = simpledialog.askstring("Add Product", "Enter product category:")
        self.product_quantity = simpledialog.askinteger("Add Product", "Enter product quantity:")
        self.product_price = simpledialog.askfloat("Add Product", "Enter product price:")
       
        if self.product_name and self.product_category and self.product_quantity is not None and self.product_price is not None:
            add_product(self.product_name, self.product_category, self.product_quantity, self.product_price)
            messagebox.showinfo("Success", "Product added successfully.")
        else:
            messagebox.showwarning("Input Error", "Please provide all product details.")

    def check_low_stock(self):
        low_stock_alert()

    def record_sale_screen(self):
        product_id = simpledialog.askinteger("Record Sale", "Enter product ID:")
        quantity_sold = simpledialog.askinteger("Record Sale", "Enter quantity sold:")
        if product_id is not None and quantity_sold is not None:
            record_sale(product_id, quantity_sold)
            messagebox.showinfo("Success", "Sale recorded successfully.")
        else:
            messagebox.showwarning("Input Error", "Please provide product ID and quantity.")

    def sales_summary(self):
        summary = sales_summary()
        messagebox.showinfo("Sales Summary", summary)

    def logout(self):
        self.inventory_frame.pack_forget()
        self.login_frame.pack(fill="both", expand=True)

# Main app execution
if __name__ == "__main__":
    setup_database()  # Ensure the database is set up
    app = InventoryApp()
    app.mainloop()