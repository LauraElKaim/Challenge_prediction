import datetime as dt
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler
import statsmodels.api as sm

def predict(Date, Number_seconds):
    return 1.3260 * Date + 0.0245 * Number_seconds -9.789e+05

def predict_all(self, lst_date, lst_nb_seconds):
    predicted_bikes = []
    for n in self.index:
        predicted_bikes.append(predict(lst_date[n], lst_nb_seconds[n]))
    return predicted_bikes

def multivariate_regression(self): 
    self['Date'] = self['Date'].map(dt.datetime.toordinal)
    Y = self['Number of bikes from 00:01 to the given time']
    X = self[['Date', 'Number seconds']]

    fig = plt.figure()
    ax = fig.add_subplot(1,2,1, projection='3d')
    ax.scatter(self["Date"], self["Number seconds"], self["Number of bikes from 00:01 to the given time"], c='orange', marker='.')
    ax.set_xlabel('Date')
    ax.set_ylabel('Number of seconds')
    ax.set_zlabel('Number of bicycle passages')
    ax.set_title('Number of bicycle passages from 00:01 to the given time \n according to the date and the time')
    plt.show()

    X = sm.add_constant(X) #add an intercept (beta_0) to our model
    scale = StandardScaler()
    X_scaled = scale.fit_transform(X[['Date', 'Number seconds']])
    est = sm.OLS(Y, X).fit()
    print(est.summary())

    fig = plt.figure()
    ax = fig.add_subplot(1, 2, 2, projection='3d')
    ax.plot_trisurf(self["Date"], self["Number seconds"], predict_all(self, self["Date"], self["Number seconds"]))
    ax.set_xlabel('Date')
    ax.set_ylabel('Number of seconds')
    ax.set_zlabel('Number of bicycle passages')
    ax.set_title('Multivariate regression of the number of bicycle \n passages from 00:01 to the given time \n according to the date and the time')
    plt.show()

    return X_scaled