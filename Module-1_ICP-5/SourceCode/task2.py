# Importing the libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn import linear_model, metrics

# Setting the plotting defaults
plt.style.use(style='ggplot')
plt.rcParams['figure.figsize'] = (20, 12)

# Loading the input file
df = pd.read_csv('./data/winequality-red.csv')
print("The first 4 records of the dataframe\n", df.head(4))

# Info about dataframe
print("\nDataframe info")
print(df.info())

# statistics about data
print("\nStatistics about data")
print(df.describe())

# To check null values
print("\nAvailibility of null values in the data\n")
print(df.isnull().sum())


# Non-Categorical  variables
numeric_features = df.select_dtypes(include=[np.number])
print("\nNon-Categorical Variables")
print(numeric_features)

# Non-Categorical  variables
print("\nNumber of Categorical Variables")
categorical_features = df.select_dtypes(exclude=[np.number])
print(categorical_features.shape[1])

# Correlation
corr = numeric_features.corr()
print("\nCorrelation: \n")
print(corr)

# To sort the correlation between quality with other features
# positive correlation to negative correlation
print("\nCorrelation between quality with other features  from positive to negative\n")
print(corr['quality'].sort_values(ascending = False))

# You need to find the top 3 most correlated features to the target label(quality
# To sort the correlation between quality with other features in absolute values to figure out the most correlated ones
print("\nthe top 3 most correlated features to the target label\n")
print(corr['quality'].abs().sort_values(ascending = False)[1:4])

# Unique values in the target
print("\nTarget value uniqueness\n")
print(df['quality'].unique())

# arrange the data for modelling
X = df.drop(['quality'], axis=1)
y = np.log(df.quality)

# Train-test-split
X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=101, test_size=.30)

# Linear Regression
lm = linear_model.LinearRegression()
model = lm.fit(X_train, y_train)
print("\nModel intercept and coefficients \n")
print("Intercept: ", model.intercept_)
print("Coefficients: ")
cdf = pd.DataFrame(lm.coef_, X_train.columns, columns=['Coeff'])
print(cdf)

# R^2
print("\nR^2 : ", round(model.score(X_test,y_test),4))

#predictions
y_pred = model.predict(X_test)

# Metrics
mae = metrics.mean_absolute_error(y_test,y_pred)
mse = metrics.mean_squared_error(y_test, y_pred)
rmse = np.sqrt(mse)

print("\nMean Absolute Error    : ", round(mae,4))
print("Mean Square Error      : ", round(mse,4))
print("Root Mean Square Error : ", round(rmse,4))

