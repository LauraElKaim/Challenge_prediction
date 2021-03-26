import pandas as pd

def date_formated(self):
    df = pd.to_datetime(self['Date'], format = '%d/%m/%Y')
    self['Date'] = df
    return self