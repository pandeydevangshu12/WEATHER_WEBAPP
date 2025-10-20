# 🌤️ Weather Checker App

A modern, minimal, and responsive **Weather Checker** web app built using **HTML, CSS, and JavaScript**, with a **Flask backend** serving live weather data.

---

## 🚀 Features

- 🌦️ **Real-time Weather Fetching:** Displays temperature, humidity, wind speed, and weather description.  
- 🎨 **Elegant UI:** Glassmorphism-style interface with gradients and smooth animations.  
- 🧠 **Smart Weather Icons:** Automatically adjusts emojis based on weather conditions.  
- ⚡ **Fast & Lightweight:** Pure frontend + backend integration — no external JS frameworks.  
- 🔒 **Accessible:** Keyboard navigation, ARIA roles, and responsive layout.

---

## 🗂️ Project Structure

```

weather-app/
│
├── static/
│   ├── index.html          # Frontend (HTML, CSS, JS)
│
├── app.py                  # Flask backend
├── requirements.txt        # Python dependencies
└── README.md               # Project documentation

```

> 🧩 **Note:**  
> Keep your `index.html` inside the `static/` folder so that Flask can serve it correctly and the frontend can access `/weather` API routes.

---

## ⚙️ How It Works

1. **User Input:**  
   The user enters a city name and clicks **Check** or presses **Enter**.

2. **API Call:**  
   The frontend sends a request to:
```

GET /weather?city={cityName}

````

3. **Backend Processing:**  
The Flask backend fetches live data (e.g., from OpenWeatherMap API) and returns JSON like this:
```json
{
  "city": "Chennai",
  "country": "IN",
  "temp": 31.2,
  "feels_like": 33.5,
  "humidity": 64,
  "wind_speed": 3.2,
  "description": "clear sky"
}
````

4. **Frontend Display:**
   The UI updates dynamically with emojis, temperature, and other details.

---

## 🧰 Installation & Setup

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/<your-username>/weather-checker.git
cd weather-checker
```

### 2️⃣ Set Up the Backend (Flask Example)

Create a file named **`app.py`** in the root directory:

```python
from flask import Flask, jsonify, request, send_from_directory
import requests

app = Flask(__name__)

@app.route('/')
def home():
    return send_from_directory('static', 'index.html')

@app.route('/weather')
def weather():
    city = request.args.get('city')
    if not city:
        return jsonify({"error": "City not provided"}), 400

    # Replace YOUR_API_KEY with your actual OpenWeatherMap API key
    api_key = "YOUR_API_KEY"
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    response = requests.get(url).json()

    if response.get("cod") != 200:
        return jsonify({"error": response.get("message", "Invalid city")})

    data = {
        "city": response["name"],
        "country": response["sys"]["country"],
        "temp": response["main"]["temp"],
        "feels_like": response["main"]["feels_like"],
        "humidity": response["main"]["humidity"],
        "wind_speed": response["wind"]["speed"],
        "description": response["weather"][0]["description"]
    }
    return jsonify(data)

if __name__ == "__main__":
    app.run(debug=True)
```

---

### 3️⃣ Install Dependencies

Create a `requirements.txt` file with the following:

```
flask
requests
```

Then install them:

```bash
pip install -r requirements.txt
```

---

### 4️⃣ Run the Server

```bash
python app.py
```

---

## 🌐 Accessing the Website

Once your backend is running, open this link in your browser:

👉 **[http://127.0.0.1:5000/static/index.html](http://127.0.0.1:5000/static/index.html)**

This will open your **Weather App frontend**, which communicates with the Flask backend to fetch weather data dynamically.

---

## 🧩 Example Usage

**Search:**

> Enter “Delhi” → Click “Check”

**Response:**

```
Delhi, IN
32°C (Feels like 34°C)
clear sky ☀️
💧 60% humidity • 💨 2.1 m/s wind
```

---

## 👨‍💻 Author

**Devangshu Pandey**
💼 Aspiring Full Stack Developer | VIT Chennai
- 🌐 [LinkedIn](https://www.linkedin.com/in/devangshu-pandey-606611372/)
- 📧 [Gmail](mailto:devangshupandey84@gmail.com)

---

### ⭐ If you find this project helpful, don’t forget to **star** the repo!
