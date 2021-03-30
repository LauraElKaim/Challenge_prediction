#%%
from bikeprediction import data
from zipfile import ZipFile
import shutil
import pandas as pd

def load_file (self):
        with ZipFile(self, 'r') as zip:
                zip.printdir()
                print('extraction...')
                zip.extractall()
        files = ["MMM_EcoCompt_X2H19070220_Archive2020.json", 
        "MMM_EcoCompt_X2H20042632_Archive2020.json", "MMM_EcoCompt_X2H20042633_Archive2020.json", 
        "MMM_EcoCompt_X2H20042634_Archive2020.json", "MMM_EcoCompt_X2H20042635_Archive2020.json", 
        "MMM_EcoCompt_X2H20063161_Archive2020.json", "MMM_EcoCompt_X2H20063162_Archive2020.json", 
        "MMM_EcoCompt_X2H20063163_Archive2020.json", "MMM_EcoCompt_X2H20063164_Archive2020.json", 
        "MMM_EcoCompt_XTH19101158_Archive2020.json"]
        for file in files:
                shutil.move(file, "bikeprediction/data")

def save_json_df(self):
        df = pd.read_json(self)
        return df