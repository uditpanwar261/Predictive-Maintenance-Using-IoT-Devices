# ⚙️ Predictive Maintenance using IoT Devices

A **full-stack AI-powered web application** that predicts the **health and potential failure of industrial machines or vehicles** using simulated IoT sensor data (Temperature & Vibration).  
Built with **Python (Flask)**, **Machine Learning**, and a sleek **HTML/CSS/Chart.js** dashboard — this project demonstrates a real-world predictive maintenance workflow.

---

## 🧠 Project Overview

Modern industries rely on **IoT sensors** to monitor equipment in real-time.  
This project simulates such sensors to collect readings (temperature, vibration, pressure, etc.) and uses a trained **Random Forest Classifier** to predict machine health.

### 🎯 Core Objectives:
- Monitor device health in real-time
- Predict potential failures before they occur
- Visualize live data and historical trends
- Provide an interactive web-based dashboard

---

## 🚀 Features

✅ **Machine Learning Backend** — Predicts equipment health using real IoT sensor data  
✅ **Flask REST API** — Connects ML model to frontend seamlessly  
✅ **Interactive Dashboard** — Visualizes predictions and system performance  
✅ **Prediction History** — Stores recent predictions with timestamps  
✅ **User Authentication (Login / Signup)** — Designed for multiple users  
✅ **Clean UI/UX** — Built with gradient-glass design & Chart.js visualizations  
✅ **Deployment Ready** — Configured for Render or Heroku cloud deployment  

---

## 🧩 Tech Stack

| Layer | Technology |
|--------|-------------|
| **Frontend** | HTML, CSS, Chart.js, JavaScript |
| **Backend** | Flask (Python) |
| **Machine Learning** | Scikit-learn, Pandas, Joblib |
| **Database** | SQLite (optional for user auth) |
| **Deployment** | Render / Heroku |
| **Version Control** | Git & GitHub |

---

## 📁 Project Structure

```

predictive-maintenance/
│
├── backend/
│   ├── app.py                  # Flask backend (API + routes)
│   ├── train_model.py          # ML model training script
│   ├── requirements.txt        # Project dependencies
│   ├── Procfile                # For Heroku/Render deployment
│   ├── render.yaml             # Render deployment config
│   ├── .gitignore
│   │
│   ├── model/
│   │   ├── model.pkl           # Trained ML model
│   │   └── features.json       # Feature metadata
│   │
│   ├── static/
│   │   └── style.css           # Frontend styling
│   │
│   ├── templates/
│   │   ├── base.html           # Shared HTML layout
│   │   ├── home.html           # Dashboard page
│   │   ├── predict.html        # Prediction page
│   │   ├── history.html        # History page
│   │   ├── login.html          # User login
│   │   └── signup.html         # User signup
│   │
│   └── data/
│       ├── TS1.txt             # Temperature sensor data
│       ├── TS2.txt
│       ├── TS3.txt
│       ├── TS4.txt
│       ├── VS1.txt             # Vibration data
│       └── CE.txt              # Condition indicator
│
└── README.md

````

---

## ⚙️ Installation & Setup

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/your-username/predictive-maintenance.git
cd predictive-maintenance/backend
````

### 2️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

### 3️⃣ Train the Model

```bash
python train_model.py
```

This generates `model.pkl` and `features.json` inside the `/model` folder.

### 4️⃣ Run the Flask Application

```bash
python app.py
```

Now visit 👉 **[http://127.0.0.1:5000](http://127.0.0.1:5000)** in your browser.

---

## 🧠 How It Works

1. IoT sensor data (temperature, vibration, etc.) is loaded from text files
2. Data is preprocessed and averaged per reading
3. The ML model (Random Forest) predicts whether the device is:

   * 🟢 **Healthy**
   * 🔴 **Failure Likely**
4. Predictions are visualized and stored in the history table

---

## 🖥️ UI Preview

| Dashboard                                                                | Prediction                                                              | History                                                                 |
| ------------------------------------------------------------------------ | ----------------------------------------------------------------------- | ----------------------------------------------------------------------- |
| ![Dashboard](C:\Projects\Predictive Maintainance Using Iot Devices\UI_SS\dashboard.png) | ![Prediction](C:\Projects\Predictive Maintainance Using Iot Devices\UI_SS\predict.png) | ![History](C:\Projects\Predictive Maintainance Using Iot Devices\UI_SS\history.png) |


---

## ☁️ Deployment (Render / Heroku)

### Render (Recommended)

1. Create a [Render](https://render.com) account
2. Connect your GitHub repository
3. Configure:

   * **Build Command:** `pip install -r requirements.txt`
   * **Start Command:** `gunicorn app:app`
4. Deploy and get your live URL 🌍

---

## 🧩 Future Enhancements

* Integrate **live IoT sensors or MQTT stream**
* Add **automated email alerts** for failures
* Include **role-based dashboard (Admin/Engineer)**
* Add **data visualization analytics** for trends
* Store predictions persistently in a cloud DB

---

## 👨‍💻 Author

**Udit Panwar**
📍 *B.Tech, Computer Science (AKTU)*
💡 Passionate about Data Science, AI, and IoT-based Predictive Systems.
🔗 [GitHub](https://github.com/your-username) | [LinkedIn](https://linkedin.com/in/your-link)

---

## 🏁 Conclusion

This project demonstrates how **AI + IoT + Web Technologies** can prevent costly machine downtime through early failure prediction.
It’s a perfect blend of **data science, software engineering, and industrial IoT** — ideal for your **portfolio, internships, or final-year project**.
