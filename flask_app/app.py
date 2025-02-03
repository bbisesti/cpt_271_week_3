from flask import Flask, request, jsonify

app = Flask(__name__)

# In-memory storage for students
students = [
    {
        'id': 1,
        'first_name': 'John',
        'last_name': 'Doe'
    },
    {
        'id': 2,
        'first_name': 'Jane',
        'last_name': 'Doe'
    },
    {
        'id': 3,
        'first_name': 'Alice',
        'last_name': 'Smith'
    }
]

@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    if data['username'] == 'admin' and data['password'] == 'admin':
        return jsonify({'message': 'Login successful'}), 200
    return jsonify({'message': 'Invalid credentials'}), 401

@app.route('/profile', methods=['GET'])
def get_profile():
    return jsonify({'username': 'admin','password':'admin', 'email': 'admin@mainecc.edu'}), 200

@app.route('/students', methods=['GET'])
def get_students():
    return jsonify(students), 200

@app.route('/students', methods=['POST'])
def add_student():
    data = request.get_json()
    student_id = len(students) -1
    students[student_id] = {
        'id': student_id,
        'first_name': data['first_name'],
        'last_name': data['last_name']
    }
    return jsonify(students[student_id]), 201

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
