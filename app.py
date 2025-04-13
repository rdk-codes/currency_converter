import tkinter as tk
from tkinter import ttk
import requests
from dotenv import load_dotenv
import os
# Load API Key
load_dotenv()
API_KEY = os.getenv("API_KEY")

def get_all_currencies():
    url = f"https://v6.exchangerate-api.com/v6/{API_KEY}/codes"
    try:
        response = requests.get(url)
        data = response.json()
        if data['result'] == 'success':
            return [f"{code} - {name}" for code, name in data['supported_codes']]
    except Exception as e:
        print("Failed to fetch currency list:", e)
    return []

def convert_currency():
    amount = amount_entry.get()
    from_raw = from_combo.get()
    to_raw = to_combo.get()
    
    if not amount or not from_raw or not to_raw:
        result_label.config(text="⚠️ Please fill in all fields.")
        return
    
    try:
        # Handle both full format and code-only input
        if " - " in from_raw:
            from_currency = from_raw.split(" - ")[0]
        else:
            from_currency = from_raw.upper()
            
        if " - " in to_raw:
            to_currency = to_raw.split(" - ")[0]
        else:
            to_currency = to_raw.upper()
        
        url = f"https://v6.exchangerate-api.com/v6/{API_KEY}/pair/{from_currency}/{to_currency}/{amount}"
        
        response = requests.get(url)
        data = response.json()
        if data['result'] == "success":
            result = data['conversion_result']
            result_label.config(text=f"✅ {amount} {from_currency} = {result:.2f} {to_currency}")
        else:
            result_label.config(text=f"❌ Conversion failed. Error: {data.get('error-type', 'Unknown error')}")
    except Exception as e:
        result_label.config(text=f"🚨 Error: {e}")

def filter_combobox(event, combobox, values):
    # Store cursor position
    cursor_pos = combobox.index(tk.INSERT)
    current_text = combobox.get()
    
    # Update the list without interrupting typing
    filtered = [v for v in values if current_text.lower() in v.lower()]
    combobox['values'] = filtered
    
    # Keep the text as is
    combobox.delete(0, tk.END)
    combobox.insert(0, current_text)
    
    # Restore cursor position
    combobox.icursor(cursor_pos)

# UI Setup
root = tk.Tk()
root.title("Currency Converter")
root.geometry("500x500")
root.resizable(False, False)

icon = tk.PhotoImage(file='icon.png')
root.iconphoto(True, icon)

mainframe = ttk.Frame(root, padding=20)
mainframe.pack(fill="both", expand=True)

ttk.Label(mainframe, text="Currency Converter", font=("Helvetica", 20, "bold")).pack(pady=(10, 20))

ttk.Label(mainframe, text="Amount").pack(anchor="w")
amount_entry = ttk.Entry(mainframe, font=("Helvetica", 12))
amount_entry.pack(fill="x", pady=5)

# Currency dropdowns
currencies = sorted(get_all_currencies())

ttk.Label(mainframe, text="From Currency").pack(anchor="w")
from_combo = ttk.Combobox(mainframe, font=("Helvetica", 12))
from_combo['values'] = currencies
from_combo.pack(fill="x", pady=5)
from_combo.bind('<KeyRelease>', lambda e: filter_combobox(e, from_combo, currencies))

ttk.Label(mainframe, text="To Currency").pack(anchor="w")
to_combo = ttk.Combobox(mainframe, font=("Helvetica", 12))
to_combo['values'] = currencies
to_combo.pack(fill="x", pady=5)
to_combo.bind('<KeyRelease>', lambda e: filter_combobox(e, to_combo, currencies))

ttk.Button(mainframe, text="Convert", command=convert_currency).pack(pady=20)

result_label = ttk.Label(mainframe, text="", font=("Helvetica", 14))
result_label.pack(pady=10)

root.mainloop()