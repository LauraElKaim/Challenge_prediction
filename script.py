#%%
import bikeprediction
bike_df = bikeprediction.load_bike().save_as_df()
bike_international_date_df = bikeprediction.date_formated(bike_df)
bike_international_date_df
# %%
