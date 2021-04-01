from sklearn.model_selection import train_test_split 
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures

def linear_regression_adjustment(self):
    X = self['Date']
    y = self['Number of bikes from 00:01 to the given time']

    X = np.asarray(range(0, len(X)))
    y = np.asarray(y)

    X = X[:, np.newaxis]
    y = y[:, np.newaxis]

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)

    lin_reg = LinearRegression()
    lin_reg.fit(X, y)

    poly_reg = PolynomialFeatures(degree=3)
    X_poly = poly_reg.fit_transform(X)
    pol_reg = LinearRegression()
    pol_reg.fit(X_poly, y)

    print("The prediction is : ", lin_reg.predict([[93]]))
    print("The adjusted R^2 is : ",pol_reg.score(X_poly, y))
    print("The adjusted prediction is : ", pol_reg.predict(poly_reg.fit_transform([[93]])))

    plt.scatter(X, y, color='orangered')
    plt.plot(X, pol_reg.predict(poly_reg.fit_transform(X)), color='blue')
    plt.title('Polynomial regression of the number of bicycle passages from midnight \n to between 8:30 and 9:30 according to the date')
    plt.xlabel('Date')
    plt.ylabel('Number of bicycle passages')
    plt.show()
    
    return X_train, X_test, y_train, y_test