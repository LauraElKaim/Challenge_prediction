import pandas as pd
import datetime as datetime

def nb_seconds(self):
    df = self
    df[["h","m","s"]] = df["Hour"].astype(str).str.split(":", expand=True).astype(int)
    df['Number seconds'] = df['h'] * 3600 + df['m'] * 60 + df['s']
    return df