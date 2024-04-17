import requests
from flask import Flask, jsonify
import sqlite3

app = Flask(__name__)
DATABASE = 'data.db'

@app.route('/update_postcodes', methods=['POST'])
def update_postcodes():
    try:
        with sqlite3.connect(DATABASE) as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT id, latitude, longitude FROM Coordinates WHERE postcode IS NULL")
            coordinates = cursor.fetchall()
        
        for coord in coordinates:
            response = requests.get(f"https://api.postcodes.io/postcodes?lon={coord[2]}&lat={coord[1]}")
            data = response.json()
            if data['status'] == 200 and data['result']:
                postcode = data['result'][0]['postcode']
                with sqlite3.connect(DATABASE) as conn:
                    conn.execute("UPDATE Coordinates SET postcode = ? WHERE id = ?", (postcode, coord[0]))
        return jsonify({"message": "Postcodes updated"}), 200
    except Exception as e:
        return str(e), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=6000)

