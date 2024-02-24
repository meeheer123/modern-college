import sqlite3
from flask import Flask, request, jsonify, render_template, session, redirect, url_for
from flask_cors import CORS

app = Flask(__name__)
app.secret_key = '5rps'
# Function to initialize the database
def initialize_database():
    conn = sqlite3.connect('healthcare.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS users
                 (id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT, password TEXT, age INTEGER, 
                 phonenumber TEXT, email TEXT UNIQUE, username TEXT UNIQUE)''')
    c.execute('''CREATE TABLE IF NOT EXISTS doctors
                 (id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT, password TEXT, age INTEGER, 
                 speciality TEXT, phonenumber TEXT, experience TEXT, education TEXT, 
                 username TEXT UNIQUE, email TEXT UNIQUE, address TEXT)''')
    c.execute('''CREATE TABLE IF NOT EXISTS prescriptions
                 (id INTEGER PRIMARY KEY AUTOINCREMENT, user_id INTEGER, medicine TEXT, time TEXT)''')
    conn.commit()
    conn.close()

# Function to handle user signup
    
@app.route('/')
def home():
    return render_template('index.html')

@app.route('/signup/user', methods=['POST'])
def user_signup():
    if request.method == 'POST':
        data = request.get_json()
        name = data.get('name')
        password = data.get('password')
        age = data.get('age')
        phonenumber = data.get('phonenumber')
        email = data.get('email')
        username = data.get('username')
        if not name or not password or not age or not phonenumber or not email or not username:
            return jsonify({'error': 'Missing required fields'}), 400
        conn = sqlite3.connect('healthcare.db')
        c = conn.cursor()
        try:
            c.execute('INSERT INTO users (name, password, age, phonenumber, email, username) VALUES (?, ?, ?, ?, ?, ?)',
                      (name, password, age, phonenumber, email, username))
            conn.commit()
            return jsonify({'message': 'User signed up successfully'}), 201
        except sqlite3.IntegrityError:
            return jsonify({'error': 'Username or email already exists'}), 400
        finally:
            conn.close()
    else:
        return render_template('signup-user.html')

# Function to handle doctor signup
@app.route('/signup/doctor', methods=['POST'])
def doctor_signup():
    if request.method == 'POST':
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
    else:
        return render_template('signup-doctor.html')
    
@app.route('/login/user', methods=['GET', 'POST'])
def user_login():
    if request.method == 'POST':
        data = request.get_json()
        username = data.get('username')
        password = data.get('password')
        conn = sqlite3.connect('healthcare.db')
        c = conn.cursor()
        c.execute("SELECT * FROM users WHERE username=? AND password=?", (username, password))
        user = c.fetchone()
        conn.close()
        if user:
            session['user_id'] = user[0]  # Store user's ID in the session
            return jsonify({'message': 'User logged in successfully'}), 200
        else:
            return jsonify({'error': 'Invalid username or password'}), 401
    else:
        return render_template('login-user.html')

# Function to handle doctor login
@app.route('/login/doctor', methods=['GET', 'POST'])
def doctor_login():
    if request.method == 'POST':
        data = request.get_json()
        username = data.get('username')
        password = data.get('password')
        conn = sqlite3.connect('healthcare.db')
        c = conn.cursor()
        c.execute("SELECT * FROM doctors WHERE username=? AND password=?", (username, password))
        doctor = c.fetchone()
        conn.close()
        if doctor:
            session['doctor_id'] = doctor[0]  # Store doctor's ID in the session
            return jsonify({'message': 'Doctor logged in successfully'}), 200
        else:
            return jsonify({'error': 'Invalid username or password'}), 401
    else:
        return render_template('login-docter.html')

# Logout route
@app.route('/logout')
def logout():
    session.pop('user_id', None)
    session.pop('doctor_id', None)
    return jsonify({'message': 'Logged out successfully'}), 200

# Function to fetch user's prescriptions from the database
def get_user_prescriptions(user_id):
    conn = sqlite3.connect('healthcare.db')
    c = conn.cursor()
    c.execute('SELECT * FROM prescriptions WHERE user_id=?', (user_id,))
    prescriptions = c.fetchall()
    conn.close()
    return prescriptions

# Route to display user's prescriptions
# Route to display user's prescriptions
@app.route('/prescriptions', methods=['GET'])
def prescriptions():
    if 'user_id' not in session:
        return redirect(url_for('user_login'))  # Redirect user to login page if not logged in

    user_id = session['user_id']
    user_prescriptions = get_user_prescriptions(user_id)
    print(user_prescriptions)
    return render_template('prescription.html', user_prescriptions=user_prescriptions)

# Route to submit a new prescription
@app.route('/submit_prescription', methods=['POST', 'GET'])
def submit_prescription():
    if request.method == "POST":
        if 'user_id' not in session:
            return redirect(url_for('user_login'))  # Redirect user to login page if not logged in

        user_id = session['user_id']
        medicines = request.form.getlist('medicine[]')
        times = request.form.getlist('time[]')

        conn = sqlite3.connect('healthcare.db')
        c = conn.cursor()
        for medicine, time in zip(medicines, times):
            c.execute('INSERT INTO prescriptions (user_id, medicine, time) VALUES (?, ?, ?)', (user_id, medicine, time))
        conn.commit()
        conn.close()
        return [medicines, times] #return html here
    else:
        return render_template('prescription.html')

# Route to delete a prescription
@app.route('/prescriptions/<int:prescription_id>', methods=['DELETE'])
def delete_prescription(prescription_id):
    if 'user_id' not in session:
        return redirect(url_for('login'))  # Redirect user to login page if not logged in

    conn = sqlite3.connect('healthcare.db')
    c = conn.cursor()
    c.execute('DELETE FROM prescriptions WHERE id=?', (prescription_id,))
    conn.commit()
    conn.close()

    return redirect(url_for('prescriptions'))
    
if __name__ == '__main__':
    initialize_database()
    app.run(debug=True)
