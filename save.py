import pandas as pd
import datetime
import os

os.makedirs("data", exist_ok=True)

def save_to_csv(news, trends):
    today = datetime.date.today()

    df = pd.DataFrame({
        "date": [today],
        "news": [", ".join(news)],
        "trends": [", ".join(trends)]
    })

    try:
        old = pd.read_csv("data/history.csv")
        df = pd.concat([old, df])
    except:
        pass

    df.to_csv("data/history.csv", index=False)
