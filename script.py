#%% prediction
import bikeprediction

bike_df = bikeprediction.load_bike().save_as_df()
bike_formated_df = bikeprediction.df_formatting(bike_df)
bike_date_formated_df = bikeprediction.date_formated(bike_formated_df)
bike_df_weekday = bikeprediction.weekday_column(bike_date_formated_df)
bike_weekday = bikeprediction.plot_weekday(bike_df_weekday)

# Linear regression
linear_regression = bikeprediction.linear_regression(bike_weekday)

# Adjusted linear regression
linear_regression_adjusted = bikeprediction.linear_regression_adjustment(bike_weekday)

# Multivaried regression
bike_df_seconds = bikeprediction.nb_seconds(bike_df_weekday)
multivaried_regression = bikeprediction.multivariate_regression(bike_df_seconds)
print("The prediction is",bikeprediction.predict(737882, 9 * 3600))
#%% vis
import bikeprediction
import shutil
import pandas as pd
import folium

bikeprediction.load_file("bikeprediction/data/MMM_EcoCompt_Archives.zip")

df_Celleneuve = pd.read_json("bikeprediction/data/MMM_EcoCompt_X2H20042633_Archive2020.json", lines=True)
df_Laverune = pd.read_json("bikeprediction/data/MMM_EcoCompt_X2H20042632_Archive2020.json", lines=True)
df_Berracasa = pd.read_json("bikeprediction/data/MMM_EcoCompt_X2H19070220_Archive2020.json", lines=True)
df_Lattes1 = pd.read_json("bikeprediction/data/MMM_EcoCompt_X2H20042635_Archive2020.json", lines=True)
df_Lattes2 = pd.read_json("bikeprediction/data/MMM_EcoCompt_X2H20042634_Archive2020.json", lines=True)
df_Vieille_Poste = pd.read_json("bikeprediction/data/MMM_EcoCompt_X2H20063161_Archive2020.json", lines=True)
df_Gerhardt = pd.read_json("bikeprediction/data/MMM_EcoCompt_X2H20063162_Archive2020.json", lines=True)
df_Albert1er = pd.read_json("bikeprediction/data/MMM_EcoCompt_XTH19101158_Archive2020.json", lines=True)
df_Delmas1 = pd.read_json("bikeprediction/data/MMM_EcoCompt_X2H20063163_Archive2020.json", lines=True)
df_Delmas2 = pd.read_json("bikeprediction/data/MMM_EcoCompt_X2H20063164_Archive2020.json", lines=True)

med_Celleneuve = df_Celleneuve['intensity'].median()
med_Laverune = df_Laverune['intensity'].median()
med_Berracasa = df_Berracasa['intensity'].median()
med_Lattes1 = df_Lattes1['intensity'].median()
med_Lattes2 = df_Lattes2['intensity'].median()
med_Vieille_Poste = df_Vieille_Poste['intensity'].median()
med_Gerhardt = df_Gerhardt['intensity'].median()
med_Albert1er = df_Albert1er['intensity'].median()
med_Delmas1 = df_Delmas1['intensity'].median()
med_Delmas2 = df_Delmas2['intensity'].median()

map_mtp = folium.Map(location=[43.6, 3.8833], zoom_start = 11.5)
folium.CircleMarker([43.60969924926758, 3.896939992904663], popup="Berracasa <br> Median=1058", color='tomato', fill_color='tomato', radius=24.2).add_to(map_mtp)
folium.CircleMarker([43.5907, 3.81324], popup="Laverune <br> Median=225", color='tomato', fill_color='tomato', radius=5.1).add_to(map_mtp)
folium.CircleMarker([43.61465, 3.8336], popup="Celleneuve <br> Median=578 ", color='tomato', fill_color='tomato', radius=13.2).add_to(map_mtp)
folium.CircleMarker([43.57926, 3.93327], popup="Lattes 2 <br> Median=97", color='tomato', fill_color='tomato', radius=2.2).add_to(map_mtp)
folium.CircleMarker([43.57883, 3.93324], popup="Lattes 1 <br> Median=505", color='tomato', fill_color='tomato', radius=11.5).add_to(map_mtp)
folium.CircleMarker([43.6157418, 3.9096322], popup="Vieille Poste <br> Median=196 ", color='tomato', fill_color='tomato', radius=4.5).add_to(map_mtp)
folium.CircleMarker([43.6138841, 3.8684671], popup="Gerhardt <br> Median=881", color='tomato', fill_color='tomato', radius=20.1).add_to(map_mtp)
folium.CircleMarker([43.6266977, 3.8956288], popup="Delmas 1 <br> Median=566", color='tomato', fill_color='tomato', radius=13).add_to(map_mtp)
folium.CircleMarker([43.6266977, 3.8956288], popup="Delmas 2 <br> Median=75", color='tomato', fill_color='tomato', radius=1.7).add_to(map_mtp)
folium.CircleMarker([43.61620945549243, 3.874408006668091], popup="Albert 1er <br> Median=1094", color='tomato', fill_color='tomato', radius=25).add_to(map_mtp)
map_mtp