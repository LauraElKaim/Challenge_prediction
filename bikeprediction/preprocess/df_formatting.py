def df_formatting(self):
    df = self.iloc[:,0:4].dropna()
    df = df.rename(columns={"Heure / Time":"Hour", "Vélos depuis le 1er janvier / Grand total":"Sum of bikes since 01/01", "Vélos ce jour / Today's total":"Number of bikes from 00:01 to the given time"})
    return df

def weekday_column(self):
    weekday = self['Date'].dt.dayofweek #Monday=0, Sunday=6
    self["Weekday"] = weekday
    df = self.reindex(columns=['Date','Hour','Weekday','Sum of bikes since 01/01','Number of bikes from 00:01 to the given time'])
    return df