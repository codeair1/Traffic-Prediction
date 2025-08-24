import os
import requests
import joblib
import pandas as pd
from datetime import datetime

def download_file_from_google_drive(file_id, destination):
    URL = "https://docs.google.com/uc?export=download"
    session = requests.Session()
    response = session.get(URL, params={'id': file_id}, stream=True)
    token = None

    for key, value in response.cookies.items():
        if key.startswith('download_warning'):
            token = value

    if token:
        params = {'id': file_id, 'confirm': token}
        response = session.get(URL, params=params, stream=True)

    with open(destination, "wb") as f:
        for chunk in response.iter_content(chunk_size=32768):
            if chunk:
                f.write(chunk)

def TrafficPred(lag1, lag2):
    MODEL_PATH = 'traffic_model.pkl'
    FILE_ID = 'your_file_id_here'  # replace with actual file ID from Drive

    if not os.path.exists(MODEL_PATH):
        print("Downloading model from Google Drive...")
        download_file_from_google_drive(FILE_ID, MODEL_PATH)
        print("Download complete.")

    model = joblib.load(MODEL_PATH)

    current_datetime = datetime.now()
    hour = current_datetime.hour + 1

    weekday_map = {
        'Monday': 0,
        'Tuesday': 1,
        'Wednesday': 2,
        'Thursday': 3,
        'Friday': 4,
        'Saturday': 5,
        'Sunday': 6
    }
    day_of_week = weekday_map[current_datetime.strftime("%A")]

    data = pd.DataFrame([{
        'hour': hour,
        'day_of_week': day_of_week,
        'lag1': lag1,
        'lag2': lag2
    }])

    prediction = model.predict(data)
    return prediction[0]
