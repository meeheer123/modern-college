import sqlite3
from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

# Function to initialize the database
def initialize_database():
    conn = sqlite3.connect('healthcare.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS users
                 (id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT, password TEXT, age INTEGER, 
                 phonenumber TEXT, email TEXT UNIQUE)''')
    c.execute('''CREATE TABLE IF NOT EXISTS doctors
                 (id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT, password TEXT, age INTEGER, 
                 speciality TEXT, phonenumber TEXT, experience TEXT, education TEXT, 
                 username TEXT UNIQUE, email TEXT UNIQUE, address TEXT)''')
    conn.commit()
    conn.close()

# Function to handle user signup
@app.route('/signup/user', methods=['POST'])
def user_signup():
    data = request.get_json()
    name = data.get('name')
    password = data.get('password')
    age = data.get('age')
    phonenumber = data.get('phonenumber')
    email = data.get('email')
    if not name or not password or not age or not phonenumber or not email:
        return jsonify({'error': 'Missing required fields'}), 400
    conn = sqlite3.connect('healthcare.db')
    c = conn.cursor()
    try:
        c.execute('INSERT INTO users (name, password, age, phonenumber, email) VALUES (?, ?, ?, ?, ?)',
                  (name, password, age, phonenumber, email))
        conn.commit()
        return jsonify({'message': 'User signed up successfully'}), 201
    except sqlite3.IntegrityError:
        return jsonify({'error': 'Username or email already exists'}), 400
    finally:
        conn.close()

# Function to handle doctor signup
@app.route('/signup/doctor', methods=['POST'])
def doctor_signup():
    data = request.get_json()
    name = data.get('name')
    password = data.get('password')
    age = data.get('age')
    speciality = data.get('speciality')
    phonenumber = data.get('phonenumber')
    experience = data.get('experience')
    education = data.get('education')
    username = data.get('username')
    email = data.get('email')
    address = data.get('address')
    if not name or not password or not age or not speciality or not phonenumber or \
            not experience or not education or not username or not email or not address:
        return jsonify({'error': 'Missing required fields'}), 400
    conn = sqlite3.connect('healthcare.db')
    c = conn.cursor()
    try:
        c.execute('''INSERT INTO doctors (name, password, age, speciality, phonenumber, 
                      experience, education, username, email, address) 
                      VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)''',
                  (name, password, age, speciality, phonenumber, experience, education,
                   username, email, address))
        conn.commit()
        return jsonify({'message': 'Doctor signed up successfully'}), 201
    except sqlite3.IntegrityError:
        return jsonify({'error': 'Username or email already exists'}), 400
    finally:
        conn.close()

if __name__ == '__main__':
    initialize_database()
    app.run(debug=True)
