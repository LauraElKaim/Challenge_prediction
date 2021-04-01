import matplotlib.pyplot as plt
from scipy import stats
import seaborn as sns

def predict(x, slope, intercept):
   return slope * x + intercept

def linear_regression(self):
    import datetime as dt
    self['Date'] = self['Date'].map(dt.datetime.toordinal)
    slope, intercept, r_value, p_value, std_err = stats.linregress(self['Date'], self["Number of bikes from 00:01 to the given time"])
    X = self['Date']
    fitLine = predict(X, slope, intercept)
    plt.figure(figsize=(5000,5000))
    plt.figure()
    plt.xlabel("Date")
    plt.ylabel("Number of bicyle passages")
    plt.title("Linear regression of the number of bicycle passages from midnight \n to between 8:30 and 9:30 according to the date")
    plt.plot(X, fitLine, c='darkred')
    plt.scatter(self['Date'], self['Number of bikes from 00:01 to the given time'], c='orangered')
    plt.grid()
    plt.show()
    prediction = predict(737882, slope, intercept)
    print("The prediction is : ",prediction)
    return r_value, p_value, std_err