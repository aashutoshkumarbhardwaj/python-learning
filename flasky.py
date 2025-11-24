from flask import Flask, jsonify, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return "Welcome to the Flask App!"

@app.route('/index')
def index():
    data = {
        "message": "This is the index route",
        "status": "success"
    }
    return jsonify(data)

@app.route('/about')
def about():
    return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True)