import tkinter as tk
from tkinter import ttk
import requests

# Django server URL
SERVER_URL = 'http://127.0.0.1:8000/inventory/'

def send_data_to_server(item, quantity):
    data = {
        'item': item,
        'quantity': quantity
    }
    try:
        response = requests.post(SERVER_URL, data=data)
        if response.status_code == 201:
            print("Data sent successfully!")
        else:
            print("Failed to send data. Server returned status code:", response.status_code)
    except requests.exceptions.RequestException as e:
        print("An error occurred while sending data:", str(e))

def submit_data():
    item = item_var.get()
    quantity = quantity_entry.get()
    send_data_to_server(item, quantity)

def load_stocks():
    try:
        response = requests.get(SERVER_URL)
        if response.status_code == 200:
            stocks = response.json()
            update_table(stocks)
        else:
            print("Failed to load stocks. Server returned status code:", response.status_code)
    except requests.exceptions.RequestException as e:
        print("An error occurred while loading stocks:", str(e))

def update_table(stocks):
    table.delete(*table.get_children())
    for stock in stocks:
        item = stock['item']
        quantity = stock['quantity']
        table.insert('', 'end', values=(item, quantity))

# Create the Tkinter window
window = tk.Tk()
window.title("Inventory Management")

# Set window size and background color
window.geometry("500x200")
window.configure(bg="#F0F0F0")

# Create a frame for the content
content_frame = tk.Frame(window, bg="#FFFFFF")
content_frame.pack_configure(expand=1, padx=10, pady=10)

# Create a Notebook widget
notebook = ttk.Notebook(content_frame)
notebook.pack(fill='both', expand=True)

# Create the first tab
tab1 = ttk.Frame(notebook)
notebook.add(tab1, text='Tab 1')

# Create labels and entry fields for item and quantity in the first tab
item_label = tk.Label(tab1, text="Item:", bg="#FFFFFF", font=("Arial", 12))
item_label.grid(row=0, column=0, padx=10, pady=5, sticky="w")

item_var = tk.StringVar()
item_combobox = ttk.Combobox(tab1, textvariable=item_var, values=["TOMATO", "POTATO", "CHILLY", "GINGER", "BEANS", "CARROT", "ONION"],
                             font=("Arial", 12))
item_combobox.grid(row=0, column=1, padx=10, pady=5)

quantity_label = tk.Label(tab1, text="Quantity:", bg="#FFFFFF", font=("Arial", 12))
quantity_label.grid(row=1, column=0, padx=10, pady=5, sticky="w")
quantity_entry = tk.Entry(tab1, font=("Arial", 12))
quantity_entry.grid(row=1, column=1, padx=10, pady=5)

submit_button = tk.Button(tab1, text="Submit", command=submit_data, font=("Arial", 12), bg="#ADD8E6",
                          activebackground="#ADD000")
submit_button.grid(row=2, column=1, padx=10, pady=10)

# Create the second tab
tab2 = ttk.Frame(notebook)
notebook.add(tab2, text='Tab 2')

# Create a table to display stocks in the second tab
table_frame = ttk.Frame(tab2)
table_frame.pack(padx=10, pady=10)

table = ttk.Treeview(table_frame, columns=('item', 'quantity'), show='headings')
table.pack(side='left', fill='y')

table.heading('item', text='Item')
table.heading('quantity', text='Quantity')

scrollbar = ttk.Scrollbar(table_frame, orient="vertical", command=table.yview)
scrollbar.pack(side='right', fill='y')

table.configure(yscrollcommand=scrollbar.set)

# Load stocks when the tab is selected
tab2.bind('<<NotebookTabChanged>>', lambda event: load_stocks())

# Create the third tab
tab3 = ttk.Frame(notebook)
notebook.add(tab3, text='Tab 3')

# Create content for the third tab
# ...

# Start the Tkinter event loop
window.mainloop()
