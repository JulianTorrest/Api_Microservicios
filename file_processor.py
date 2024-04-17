
from flask import Flask, request, jsonify
import sqlite3
import pandas as pd

app = Flask(__name__)
DATABASE = 'data.db'

def init_db():
    with sqlite3.connect(DATABASE) as conn:
        conn.execute('CREATE TABLE IF NOT EXISTS Coordinates (id INTEGER PRIMARY KEY AUTOINCREMENT, latitude FLOAT, longitude FLOAT, postcode TEXT)')

@app.route('/upload', methods=['POST'])
def upload_file():
    file = request.files['file']
    if not file:
        return "No file provided", 400

    try:
        df = pd.read_csv(file)
        with sqlite3.connect(DATABASE) as conn:
            df.to_sql('Coordinates', conn, if_exists='append', index=False)
        return "File processed and data stored in database", 200
    except Exception as e:
        return str(e), 500

if __name__ == '__main__':
    init_db()
    app.run(host='0.0.0.0', port=5000)
