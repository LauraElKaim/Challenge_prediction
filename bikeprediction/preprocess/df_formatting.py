def df_formatting(self):
    df = self.iloc[:,0:4].dropna()
    return df.rename(columns={"Vélos depuis le 1er janvier / Grand total":"Sum of bikes since 01/01", "Vélos ce jour / Today's total":"Number of bikes from 00:01 to the given time"})