#%%
import bikeprediction
bike_df = bikeprediction.load_bike().save_as_df()
bike_df_formated = bikeprediction.df_formatting(bike_df)
bike_df_formated
bike_date_formated_df = bikeprediction.date_formated(bike_df_formated)
bike_date_formated_df