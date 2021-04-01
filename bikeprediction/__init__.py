__version__="0.0.1"
from .io.load_bike import load_bike
from .preprocess.df_formatting import df_formatting
from .preprocess.df_formatting import weekday_column
from .preprocess.format_date import date_formated
from .preprocess.nb_seconds import nb_seconds
from .vis.plot_bike_weekday import plot_weekday
from .vis.linear_regression import linear_regression
from .vis.linear_regression_adjustment import linear_regression_adjustment
from .vis.multivariate_regression import multivariate_regression
from .vis.multivariate_regression import predict
from .vis.load_file import load_file