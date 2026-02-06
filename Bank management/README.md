## Bank Management System (Python OOP + Web)

This project is a simple **Bank Management System** written in Python using OOP concepts.  
It supports both:

- **Terminal/CLI interface** (original version)
- **Web interface** built with **Streamlit**

All data is stored in a local JSON file (`data.json`).

---

### Features

- **Create Account**
  - Name, age, email, 4‑digit PIN
  - Auto‑generated account number
  - Minimum age: 18
- **Deposit Money**
  - Validates account number and PIN
  - Deposit limit: 1 to 100000 per transaction
- **Withdraw Money**
  - Validates account number and PIN
  - Checks for sufficient balance
- **Show Account Details**
  - View all stored fields (name, age, email, account number, balance, etc.)
- **Update Account Details**
  - Update name, email, or PIN (age, account number, and balance cannot be edited directly)
- **Delete Account**
  - Requires confirmation

---

### Project Structure

- `main.py` – Core `Bank` class and **terminal (CLI) interface**
- `app.py` – **Streamlit web app** interface
- `data.json` – JSON database file for storing accounts
- `requirements.txt` – Python dependencies for the project

---

### Requirements

- **Python 3.10+** (recommended)
- Packages (already listed in `requirements.txt`):
  - `streamlit`
  - `pyyaml`
  - `python-dotenv`
  - `pandas`
  - `openpyxl`
  - `python-magic`

---

### Setup

1. **Open a terminal** and go to the project folder:

```bash
cd "C:\Users\Aditya Wagh\Desktop\Pythonoops\Bank management"
```

2. (Recommended) **Create and activate a virtual environment**:

```bash
python -m venv .venv
.venv\Scripts\activate
```

3. **Install dependencies**:

```bash
pip install -r requirements.txt
```

---

### Run the Web Version (Streamlit)

1. In the project folder, run:

```bash
streamlit run app.py
```

2. Your default browser will open automatically.  
   If not, look in the terminal for a URL like:

```text
http://localhost:8501
```

3. Use the **sidebar** to:
   - Create accounts
   - Deposit / withdraw money
   - Show / update account details
   - Delete accounts

4. To **stop** the app, return to the terminal and press:

```text
Ctrl + C
```

---

### Run the Terminal Version (CLI)

If you prefer the original terminal interface:

1. In the project folder, run:

```bash
python main.py
```

2. You will see a text-based menu:
   - Choose options 1–7 to perform actions.

The CLI and web app **share the same `data.json` file**, so changes made in one interface are visible in the other.

---

### Notes

- Do **not** share or expose `data.json` publicly if it contains real user data.
- This project is for **learning/demo purposes** and is **not** production‑ready banking software.

