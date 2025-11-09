from flask import Flask, render_template, request, jsonify, redirect, session
import joblib, json, os
from datetime import datetime

app = Flask(__name__)
app.secret_key = 'iot_secret_key'

# Load model and features
model = joblib.load('model/model.pkl')
feature_names = json.load(open('model/features.json'))

# In-memory history
prediction_history = []

@app.route('/')
def home():
    if not session.get('user'):
        return redirect('/login')
    return render_template('home.html')

@app.route('/predict')
def predict_page():
    if not session.get('user'):
        return redirect('/login')
    return render_template('predict.html')

@app.route('/history')
def history():
    if not session.get('user'):
        return redirect('/login')
    return render_template('history.html', history=prediction_history)

@app.route('/login', methods=['GET', 'POST'])
def login_page():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        # (Optional) Add authentication logic later
        session['user'] = email
        return redirect('/')
    return render_template('login.html')


@app.route('/signup', methods=['GET', 'POST'])
def signup_page():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        password = request.form['password']
        # (Optional) Save user to DB later
        print(f"New signup: {name}, {email}")
        return redirect('/login')
    return render_template('signup.html')

@app.route('/predict', methods=['POST'])
def predict():
    data = request.json
    try:
        X = [data[f] for f in feature_names]
        pred = model.predict([X])[0]
        result = "Healthy" if pred == 1 else "Failure Likely"
        prediction_history.append({
            "time": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            **data,
            "result": result
        })
        return jsonify({"prediction": result})
    except Exception as e:
        return jsonify({"error": str(e)}), 400

@app.route('/logout')
def logout():
    session.clear()
    return redirect('/login')

if __name__ == '__main__':
    app.run(debug=True)
