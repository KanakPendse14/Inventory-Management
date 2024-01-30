import tkinter as tk
from tkinter import ttk, messagebox
import sqlite3
import os
import openpyxl

def submit_form():
    product_name = entry_product_name.get()
    description = entry_description.get("1.0", tk.END)
    stock_value = entry_stock_value.get()
    sales_month = entry_sales_month.get()
    sales_year = entry_sales_year.get()
    selected_year = year_var.get()
    selected_supplier = supplier_var.get()
    
    # Process the form data as needed
    print("Product Name:", product_name)
    print("Description:", description)
    print("Stock Value:", stock_value)
    print("Sales per Month:", sales_month)
    print("Sales per Year:", sales_year)
    print("Selected Year:", selected_year)
    print("Selected Supplier:", selected_supplier)

    conn = sqlite3.connect('data.db')
    table_create_query = '''CREATE TABLE IF NOT EXISTS Product_data(product_name TEXT, description TEXT, stock_value INT, sales_month INT, sales_year INT, selected_year INT, selected_supplier TEXT)'''
    conn.execute(table_create_query)
    data_insert = '''INSERT INTO Product_data(product_name,description,stock_value,sales_month,sales_year,selected_year,selected_supplier) VALUES(?,?,?,?,?,?,?)'''
    data_tuple = (product_name, description, stock_value, sales_month, sales_year, selected_year, selected_supplier)
    cursor = conn.cursor()
    cursor.execute(data_insert, data_tuple)
    conn.commit()
    conn.close()

    # Display a message box after successful insertion
    messagebox.showinfo("Success", "Product details have been inserted.")

    # Clear the form fields
    entry_product_name.delete(0, tk.END)
    entry_description.delete("1.0", tk.END)
    entry_stock_value.delete(0, tk.END)
    entry_sales_month.delete(0, tk.END)
    entry_sales_year.delete(0, tk.END)
    year_combobox.current(0)
    supplier_combobox.current(0)


    filepath = "C:\\Users\\ACER\\IdeaProjects\\InventoryManagement\\exceldata.xlsx"

    if not os.path.exists(filepath):
        workbook = openpyxl.Workbook()
        sheet = workbook.active
        heading = ["Product Name","Description","Stock Value","Sales per Month","Sales per Year","Year","Supplier"]
        sheet.append(heading)
        workbook.save(filepath)
    workbook = openpyxl.load_workbook(filepath)
    sheet = workbook.active
    sheet.append([product_name, description, stock_value, sales_month, sales_year, selected_year, selected_supplier])
    workbook.save(filepath)
# GUI
root = tk.Tk()
root.title("Product Information Form")
root.geometry("800x700")

# Styling
root.configure(bg="#f3e5f5")  # Lightest purple background color

main_frame = ttk.Frame(root, padding=(20, 20, 20, 20), style="Main.TFrame", borderwidth=2, relief="solid")
main_frame.pack(expand=True, fill=tk.BOTH, padx=20, pady=20)

# Product Name
label_product_name = ttk.Label(main_frame, text="Product Name:")
label_product_name.pack(anchor="w", pady=5)
entry_product_name = ttk.Entry(main_frame, width=60)
entry_product_name.pack(anchor="w", pady=5)

# Description
label_description = ttk.Label(main_frame, text="Description:")
label_description.pack(anchor="w", pady=5)
entry_description = tk.Text(main_frame, width=60, height=6)
entry_description.pack(anchor="w", pady=5)

# Stock Value
label_stock_value = ttk.Label(main_frame, text="Stock Value:")
label_stock_value.pack(anchor="w", pady=5)
entry_stock_value = ttk.Entry(main_frame, width=60)
entry_stock_value.pack(anchor="w", pady=5)

# Sales per Month
label_sales_month = ttk.Label(main_frame, text="Sales per Month:")
label_sales_month.pack(anchor="w", pady=5)
entry_sales_month = ttk.Entry(main_frame, width=60)
entry_sales_month.pack(anchor="w", pady=5)

# Sales per Year
label_sales_year = ttk.Label(main_frame, text="Sales per Year:")
label_sales_year.pack(anchor="w", pady=5)
entry_sales_year = ttk.Entry(main_frame, width=60)
entry_sales_year.pack(anchor="w", pady=5)

# Year (Dropdown)
label_year = ttk.Label(main_frame, text="Year:")
label_year.pack(anchor="w", pady=5)
year_var = tk.StringVar()
year_combobox = ttk.Combobox(main_frame, textvariable=year_var, values=[2021, 2022, 2023, 2024], state="readonly", width=57)
year_combobox.pack(anchor="w", pady=5)
year_combobox.current(0)

# Supplier (Dropdown)
label_supplier = ttk.Label(main_frame, text="Supplier:")
label_supplier.pack(anchor="w", pady=5)
supplier_var = tk.StringVar()
supplier_combobox = ttk.Combobox(main_frame, textvariable=supplier_var, values=["Supplier A", "Supplier B", "Supplier C"], state="readonly", width=57)
supplier_combobox.pack(anchor="w", pady=5)
supplier_combobox.current(0)

# Submit Button
submit_button = ttk.Button(main_frame, text="Submit", command=submit_form, style="Submit.TButton")
submit_button.pack(anchor="center", pady=20)

# Apply Styling
style = ttk.Style(root)
style.configure("Main.TFrame", background="#f3e5f5")  # Lightest purple background color
style.configure("TLabel", foreground="#311b92")  # Dark purple text color for labels and borders
style.configure("TButton", foreground="#000000")  # Black text color for buttons

# Create a new style for the Submit button with a black background
style.configure("Submit.TButton", background="#000000", foreground="#ffffff")

root.mainloop()
