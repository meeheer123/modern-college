from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
db = SQLAlchemy(app)

class Doctor(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True, nullable=False)
    password = db.Column(db.String(100), nullable=False)
    # Other doctor-related fields...

class Patient(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True, nullable=False)
    password = db.Column(db.String(100), nullable=False)
    # Other patient-related fields...

def create_doctor(username, password):
    new_doctor = Doctor(username=username, password=password)
    db.session.add(new_doctor)
    db.session.commit()
    return new_doctor.id

def create_patient(username, password):
    new_patient = Patient(username=username, password=password)
    db.session.add(new_patient)
    db.session.commit()
    return new_patient.id

@app.route('/signup/doctor', methods=['POST'])
def signup_doctor():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')
    if not username or not password:
        return jsonify({'error': 'Username and password are required'}), 400
    doctor_id = create_doctor(username, password)
    return jsonify({'doctor_id': doctor_id}), 201

@app.route('/signup/patient', methods=['POST'])
def signup_patient():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')
    if not username or not password:
        return jsonify({'error': 'Username and password are required'}), 400
    patient_id = create_patient(username, password)
    return jsonify({'patient_id': patient_id}), 201

if __name__ == '__main__':
    db.create_all()
    app.run(debug=True)
