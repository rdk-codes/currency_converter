# 💱 Currency Converter

A simple GUI currency converter built with **Tkinter** and the **ExchangeRate API**.

You can input an amount, a source currency, and a target currency — the app will convert between them in real time using live exchange rates.

---

## ✨ Getting Started

### ✅ Prerequisites

- Python 3.x installed
- A free account with [ExchangeRate API](https://www.exchangerate-api.com/)
- An API key from ExchangeRate API

---

## 🔐 Setup API Key

Create a `.env` file in the project directory to store your API key securely.

```bash
# Windows (PowerShell)
New-Item .env

# Unix (Linux/macOS)
touch .env
```

Then open the `.env` file in your text editor:

```bash
code .env  # or use notepad, nano, nvim, etc.
```

And add your API key:

```env
API_KEY=your_exchangerate_api_key
```

---

## 💻 Installation Instructions

<details>
<summary><strong>🪟 Windows</strong></summary>

```pwsh
git clone https://github.com/rdk-codes/currency_converter.git
cd currency_converter
python -m venv venv
.\venv\Scripts\activate.ps1
pip install -r requirements.txt
python app.py
```

</details>

<details>
<summary><strong>🍎 macOS /🐧Linux</strong></summary>

```bash
git clone https://github.com/rdk-codes/currency_converter.git
cd currency_converter
python3 -m venv venv
source venv/bin/activate
pip3 install -r requirements.txt
python3 app.py
```

</details>

---

## 📸 GUI Preview
![alt text](<demo.gif>)
---

## 🧠 Notes

- Make sure your API key is valid and not expired.
- You can update the currency list or base currency in the code as needed.
- If you run into issues, feel free to open an issue on the GitHub repo.

---

## 🛠 Built With

- Python 🐍
- Tkinter
- [ExchangeRate API](https://www.exchangerate-api.com/)

---
