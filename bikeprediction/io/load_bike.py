import pandas as pd
from download import download
from bikeprediction.io import url_db, path_target

class load_bike:
  def __init__(self, url=url_db, target_name=path_target):
    download(url, target_name, replace=True)
  
  @staticmethod
  def save_as_df():
    df_bikes = pd.read_csv(path_target, na_values="", low_memory=False, converters={'data': str, 'heure': str})
    return df_bikes