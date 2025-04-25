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
- [Contributing](#contributing)
- [License](#license)

---


## Features

- **Real-Time Data**: Fetches current weather data (temperature, wind speed, precipitation) for selected New York State cities via the OpenWeatherMap API.  
- **Risk Prediction**: Uses a logistic regression model to classify disaster risk levels into Low, Medium, or High.  
- **Interactive Dashboard**: Built with Streamlit — users can select a city, view live weather stats, risk predictions, and a map view of the location.  
- **Alerts**: Simulates free email or SMS alerts when risk levels reach High.  
- **Free Hosting**: Deployable on Streamlit Cloud at no cost.  

---

## Demo

A live version is available at: [https://your-app-name.streamlit.app](https://nydisasterdashboard-bwzwrfd3dhfutlzg8xxmt6.streamlit.app/)

---

## Tech Stack

- **Frontend / UI**: Streamlit  
- **Backend / API**: Python, requests  
- **Machine Learning**: scikit-learn (Logistic Regression)  
- **Data Source**: OpenWeatherMap API  
- **Hosting**: Streamlit Cloud  
- **Alerts (Optional)**: SendGrid, Mailgun, or SMS via Twilio  

---

## Prerequisites

- Python 3.7 or above  
- An OpenWeatherMap API Key (free tier)  
- (Optional) SendGrid or Mailgun API Key for email alerts  

---

## Installation

1. **Clone the repository**

   ```bash
   git clone https://github.com/YOUR_USERNAME/NYDisasterDashboard.git
   cd NYDisasterDashboard
