from dotenv import load_dotenv
import tkinter as tk
import requests
import os
import json
from datetime import datetime, timedelta

CACHE_FILE = "rates_cache.json"
CACHE_DURATION = timedelta(hours=1)  # use cache for 1 hour

load_dotenv(".env")
api_key = os.getenv("API_KEY")

def get_conversion_rates():
    if os.path.exists(CACHE_FILE):
        with open(CACHE_FILE, "r") as file:
            cache = json.load(file)
            if datetime.now() - datetime.fromisoformat(cache["timestamp"]) < CACHE_DURATION:
                return cache["conversion_rates"]
    
    # Otherwise, fetch from API
    response = requests.get(f"https://v6.exchangerate-api.com/v6/{api_key}/latest/USD")
    data = response.json()
    rates = data["conversion_rates"]

    # Save to file with timestamp
    with open(CACHE_FILE, "w") as file:
        json.dump({"timestamp": datetime.now().isoformat(), "conversion_rates": rates}, file)

    return rates

conversion_rates = get_conversion_rates() 

def convert_to_usd(amt : float, unit : str): 
    usd_amt = amt / conversion_rates[unit.strip().upper()]
    return round(usd_amt, 3)

def convert_to_other(amt : float, unit: str): 
    other_amt = amt * conversion_rates[unit.strip().upper()]
    return round(other_amt, 3)

def convert():
    result_usd = convert_to_usd(float(amt_entry.get()), entry_1.get())
    result = convert_to_other(result_usd, entry_2.get())
    result_label.config(text=f"Result is {result}")

root = tk.Tk()
my_img = tk.PhotoImage(file='icon.png')
root.geometry("400x400")
root.resizable(False, False)
root.title("Currency Converter")
root.iconphoto(True, my_img)

title_label = tk.Label(root, text="CURRENCY CONVERTER", font=("Arial", 16, "bold"))
title_label.pack(pady=20)

amt_frame = tk.Frame(root)
amt_frame.pack(pady=5)
amt_label = tk.Label(amt_frame, text="Amount 💰", font=("Arial", 12))
amt_label.grid(row=0, column=0, padx=5)
amt_entry = tk.Entry(amt_frame, width=15)
amt_entry.grid(row=0, column=1, padx=5)

frame1 = tk.Frame(root)
frame1.pack(pady=5)
label_1 = tk.Label(frame1, text="Currency is 💵", font=("Arial", 12))
label_1.grid(row=0, column=0, padx=5)
entry_1 = tk.Entry(frame1, width=15)
entry_1.grid(row=0, column=1, padx=5)

frame2 = tk.Frame(root)
frame2.pack(pady=5)
label_2 = tk.Label(frame2, text="Convert to 💶", font=("Arial", 12))
label_2.grid(row=0, column=0, padx=5)
entry_2 = tk.Entry(frame2, width=15)
entry_2.grid(row=0, column=1, padx=5)

calculate_button = tk.Button(root, text="Convert", width=12, height=1, command=convert)
calculate_button.pack(pady=15)

result_label = tk.Label(root, text='', font=("Arial", 12))
result_label.pack(pady=10)

root.mainloop()
