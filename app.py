from flask import Flask, request, jsonify, render_template
import json
import os

app = Flask(__name__)

# Файл для збереження користувачів
users_file = 'users.json'

# Створення файлу з користувачами, якщо його не існує
if not os.path.exists(users_file):
    with open(users_file, 'w') as f:
        json.dump([], f)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/users', methods=['GET', 'POST'])
def users():
    if request.method == 'POST':
        user = request.get_json()
        with open(users_file, 'r+') as f:
            users_data = json.load(f)
            users_data.append(user)
            f.seek(0)
            json.dump(users_data, f)
        return jsonify(user), 201

    elif request.method == 'GET':
        with open(users_file, 'r') as f:
            users_data = json.load(f)
        return jsonify(users_data)

if __name__ == '__main__':
    app.run(debug=True)
