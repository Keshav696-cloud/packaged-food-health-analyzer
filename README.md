# Packaged Food Health Analyzer

A Flask-based web application that analyzes packaged food products using their nutritional values and ingredients.

## Features
- Analyzes sugar, saturated fat, sodium, protein, and calories.
- Checks ingredients against a local reference database.
- Provides a health score based on predefined rules.
- Supports ingredient autocomplete and quick-add.
- Works offline using SQLite.

## Technologies
Python, Flask, SQLite, HTML, CSS, JavaScript, and Excel.

## Installation

1. Clone or download the project.
2. Create and activate a virtual environment:
   ```bash
   python -m venv venv
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Sync the ingredient database:
   ```bash
   python database/sync_excel_to_db.py
   ```
5. Start the application:
   ```bash
   python app.py
   ```
6. Open `http://127.0.0.1:5000/` in your browser.

## Disclaimer
Results are based on predefined rules and are for informational purposes only. They are not a substitute for professional dietary advice.
