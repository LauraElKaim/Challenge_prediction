import pandas as pd

def date_formated(self):
    df = pd.to_datetime(self['Date'] + ' ' + self['Heure / Time'], format = '%d/%m/%Y %H:%M:%S')
    self['Date'] = df
    del self['Heure / Time']
    return self