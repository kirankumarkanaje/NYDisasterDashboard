import streamlit as st
import pandas as pd
import numpy as np
import requests
from sklearn.linear_model import LogisticRegression
import streamlit as st
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail

# --- Configuration ---
st.set_page_config(page_title="NY Disaster Risk Dashboard", layout="centered")
st.title("NY State Disaster Risk Forecasting Dashboard")

# --- API Key Setup ---
# For free hosting on Streamlit Cloud, place your OpenWeatherMap API key in the secrets.
# In a local development environment, consider storing it in an environment variable.
try:
    api_key = st.secrets["OPENWEATHER_API_KEY"]
except Exception:
    st.error("Please set your OpenWeatherMap API key in Streamlit secrets or as an environment variable 'OPENWEATHER_API_KEY'.")
    st.stop()

# --- Function to Fetch Weather Data ---
def get_weather_data(city):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        # Extract essential information: temperature, wind speed, and precipitation (if available)
        temp = data["main"]["temp"]
        wind = data["wind"]["speed"]
        # Some responses might not include precipitation data
        precip = data.get("rain", {}).get("1h", 0)  
        return {"temperature": temp, "wind_speed": wind, "precipitation": precip}
    else:
        st.error("Error fetching weather data. Please check the city name or API key.")
        return None

# --- Sidebar Inputs ---
city = st.sidebar.selectbox("Choose a New York City", ["Albany", "New York", "Buffalo"])
st.sidebar.markdown("### Simulation Controls")
if st.sidebar.button("Refresh Weather Data"):
    st.experimental_rerun()

# --- Fetch Weather Data ---
weather_data = get_weather_data(city)
if weather_data:
    st.subheader(f"Current Weather in {city}")
    st.write(weather_data)

# --- Dummy Model Training ---
st.subheader("Disaster Risk Prediction")
# Generate dummy training data (features: temperature, wind_speed, precipitation)
np.random.seed(42)
n_samples = 100
X_train = np.random.uniform(low=0, high=30, size=(n_samples, 3))  # [temp, wind, precip]
# Create dummy target: risk level (0: Low, 1: Medium, 2: High)
y_train = np.array([
    0 if (x[0] < 15 and x[1] < 5) else 2 if (x[0] > 25 or x[1] > 10 or x[2] > 5) else 1 for x in X_train
])
model = LogisticRegression(multi_class='multinomial', solver='lbfgs')
model.fit(X_train, y_train)

# --- Prediction ---
if weather_data:
    X_input = np.array([[weather_data["temperature"], weather_data["wind_speed"], weather_data["precipitation"]]])
    risk_pred = model.predict(X_input)[0]
    risk_mapping = {0: "Low", 1: "Medium", 2: "High"}
    st.markdown(f"#### Predicted Disaster Risk: **{risk_mapping[risk_pred]}**")
    
    # Provide visual feedback based on risk level
    if risk_pred == 2:
        st.error("High Risk Alert! Take necessary precautions!")
    elif risk_pred == 1:
        st.warning("Moderate Risk: Stay informed and cautious.")
    else:
        st.success("Low Risk: Conditions are favorable.")

# --- Alert Simulation ---
st.markdown("### Alert System")
st.write("If disaster risk is high, you can simulate sending an alert email.")
if st.button("Send Test Alert Email"):
    def send_email_alert(message):
        print("In Here!")
        sg = SendGridAPIClient(st.secrets["SENDGRID_API_KEY"])
        mail = Mail(
            from_email=st.secrets["EMAIL_FROM"],
            to_emails =st.secrets["EMAIL_TO"],
            subject   ="Disaster Risk Alert!",
            html_content=message
        )
        try:
            response = sg.send(mail)
            if response.status_code in (200, 202):
                st.success("Alert email sent via SendGrid!")
            else:
                st.error(f"SendGrid error: {response.status_code}")
        except Exception as e:
            st.error(f"Failed to send via SendGrid: {e}")

    # In this demo, a test email is sent.
    send_email_alert(f"Test Alert: {city} currently has a {risk_mapping[risk_pred]} disaster risk.")

# --- Display Map (Optional) ---
# A minimal map view using the current city's coordinates can be added.
# For simplicity, we’ll use fixed coordinates for our cities.
city_coords = {
    "Albany": {"lat": 42.6526, "lon": -73.7562},
    "New York": {"lat": 40.7128, "lon": -74.0060},
    "Buffalo": {"lat": 42.8864, "lon": -78.8784},
}
if city in city_coords:
    st.markdown("### Location Map")
    df_map = pd.DataFrame([city_coords[city]])
    st.map(df_map)

    
