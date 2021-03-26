#%%
import bikeprediction
bike_df = bikeprediction.load_bike().save_as_df()
bike_formated_df = bikeprediction.df_formatting(bike_df)
bike_date_formated_df = bikeprediction.date_formated(bike_formated_df)
bike_df_weekday = bikeprediction.weekday_column(bike_date_formated_df)
bike_df_weekday