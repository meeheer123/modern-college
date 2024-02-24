import sqlite3
from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

# Function to initialize the database
def initialize_database():
    conn = sqlite3.connect('healthcare.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS users
                 (id INTEGER PRIMARY KEY AUTOINCREMENT, username TEXT UNIQUE, password TEXT, email TEXT)''')
    c.execute('''CREATE TABLE IF NOT EXISTS doctors
                 (id INTEGER PRIMARY KEY AUTOINCREMENT, username TEXT UNIQUE, password TEXT, email TEXT, specialization TEXT)''')
    conn.commit()
    conn.close()

# Function to handle user signup
@app.route('/signup/user', methods=['GET', 'POST'])
def user_signup():
    if request.method == 'POST':
        data = request.get_json()
        username = data.get('username')
        password = data.get('password')
        email = data.get('email')
        if not username or not password or not email:
            return jsonify({'error': 'Missing required fields'}), 400
        conn = sqlite3.connect('healthcare.db')
        c = conn.cursor()
        try:
            c.execute('INSERT INTO users (username, password, email) VALUES (?, ?, ?)', (username, password, email))
            conn.commit()
            return jsonify({'message': 'User signed up successfully'}), 201
        except sqlite3.IntegrityError:
            return jsonify({'error': 'Username already exists'}), 400
        finally:
            conn.close()
    else:
        return "hello world"

# Function to handle doctor signup
@app.route('/signup/doctor', methods=['GET', 'POST'])
def doctor_signup():
    if request.method == 'POST':
        data = request.get_json()
        username = data.get('username')
        password = data.get('password')
        email = data.get('email')
        specialization = data.get('specialization')
        if not username or not password or not email or not specialization:
            return jsonify({'error': 'Missing required fields'}), 400
        conn = sqlite3.connect('healthcare.db')
        c = conn.cursor()
        try:
            c.execute('INSERT INTO doctors (username, password, email, specialization) VALUES (?, ?, ?, ?)',
                      (username, password, email, specialization))
            conn.commit()
            return jsonify({'message': 'Doctor signed up successfully'}), 201
        except sqlite3.IntegrityError:
            return jsonify({'error': 'Username already exists'}), 400
        finally:
            conn.close()
    else:
        return render_template('signup.html')  # You can change this to render a different HTML template for doctor signup

if __name__ == '__main__':
    initialize_database()
    app.run(debug=True)
