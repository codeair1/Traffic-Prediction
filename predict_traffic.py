# %%
import joblib 
import pandas as pd
from datetime import datetime 
import joblib



def TrafficPred(lag1,lag2):

    model = joblib.load('traffic_model.pkl')
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
    day_of_week1 = current_datetime.strftime("%A")
    day_of_week = weekday_map[day_of_week1]

    data = pd.DataFrame([{
            'hour': hour,
            'day_of_week': day_of_week,
            'lag1': lag1,
            'lag2': lag2
        }])


    prediction = model.predict(data)
    return prediction[0]


