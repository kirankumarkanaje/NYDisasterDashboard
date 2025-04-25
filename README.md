# NY State Disaster Risk Forecasting Dashboard

A live, interactive dashboard that predicts and visualizes natural disaster risk levels across New York State counties and major cities using real-time weather data and a simple machine learning model.

---

<img width="1503" alt="UI1" src="https://github.com/user-attachments/assets/67bc99b5-31f0-4069-97c4-7ee3d0b51a43" />

---

<img width="1505" alt="UI2" src="https://github.com/user-attachments/assets/f5daa75b-aab2-4078-8652-90b4f15d009d" />

---

## Table of Contents

- [Features](#features)
- [Demo](#demo)
- [Tech Stack](#tech-stack)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Configuration](#configuration)
- [Running Locally](#running-locally)
- [Deployment](#deployment)
- [Usage](#usage)
- [Alert System](#alert-system)
- [Future Enhancements](#future-enhancements)

---


## Features

- **Real-Time Data**: Fetches current weather data (temperature, wind speed, precipitation) for selected New York State cities via the OpenWeatherMap API.  
- **Risk Prediction**: Uses a logistic regression model to classify disaster risk levels into Low, Medium, or High.  
- **Interactive Dashboard**: Built with Streamlit — users can select a city, view live weather stats, risk predictions, and a map view of the location.  
- **Alerts**: Simulates free email or SMS alerts when risk levels reach High.  
- **Free Hosting**: Deployable on Streamlit Cloud at no cost.  

---

## Demo

A live version is available at: [NY Disaster Prediction Dashboard](https://nydisasterdashboard-bwzwrfd3dhfutlzg8xxmt6.streamlit.app/)

---

## Tech Stack

- **Frontend / UI**: Streamlit  
- **Backend / API**: Python, requests  
- **Machine Learning**: scikit-learn (Logistic Regression)  
- **Data Source**: OpenWeatherMap API  
- **Hosting**: Streamlit Cloud  
- **Alerts (Optional)**: SendGrid

---

## Prerequisites

- Python 3.7 or above  
- An OpenWeatherMap API Key
- SendGrid API Key for email alerts  

---

## Installation

1. **Clone the repository**

   ```bash
   git clone https://github.com/YOUR_USERNAME/NYDisasterDashboard.git
   cd NYDisasterDashboard

2. **Create and activate a virtual environment**

   ```bash
      python3 -m venv venv
      source venv/bin/activate    # On Windows: venv\Scripts\activate
3. **Install dependencies**

   ```bash
      pip install -r requirements.txt

---

## Configuration
**Streamlit Secrets**

1. Create a folder named .streamlit in the project root:

   ```bash
      mkdir -p .streamlit
      Inside .streamlit, create secrets.toml with your API keys:

2. Inside .streamlit, create secrets.toml with your API keys:

   ```toml
      OPENWEATHER_API_KEY = "YOUR_OPENWEATHERMAP_API_KEY"
      # Optional: for email alerts
      SENDGRID_API_KEY     = "YOUR_SENDGRID_API_KEY"
      EMAIL_FROM           = "alerts@yourdomain.com"
      EMAIL_TO             = "recipient@example.com"

3. Add .streamlit/secrets.toml to .gitignore to keep keys private.

---

## Running Locally

   ```bash
         streamlit run app.py
         Then open http://localhost:8501 in your browser.


```
---

## Deployment

1. Push your code to a GitHub repository.
2. Sign in to Streamlit Cloud with GitHub.
3. Create a new app, point to your repo and branch, set app.py as the entry point.
4. Add secrets via the Streamlit Cloud dashboard.
5. Deploy.

---

## Usage
Select a city from the sidebar (Albany, New York, or Buffalo).
View current weather data and the predicted disaster risk level.
(Optional) Click Send Test Alert Email to simulate an alert.
Refresh data at any time using the Refresh Weather Data button.

---

## Alert System
This project supports free alerting via:

1. SendGrid (recommended): up to 100 emails/day on free tier
2. The alert function reads credentials from st.secrets and sends notifications when risk is High.

---

## Future Enhancements

1. Integrate NOAA/NWS alerts for automated triggers.
2. Replace dummy training data with real historical disaster/climate datasets.
3. Add more cities/counties and support custom location input.
4. Enhance map visualizations with GeoJSON layers and choropleth.
5. Implement scheduled background updates via a job scheduler.




