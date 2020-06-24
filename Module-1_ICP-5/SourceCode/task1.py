# Importing the libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


# Setting the plotting defaults
plt.style.use(style='ggplot')
plt.rcParams['figure.figsize'] = (20, 12)

# Loading the input file by setting the index column to Id
df = pd.read_csv('./data/train.csv', index_col='Id')
print("The first 4 records of the dataframe\n", df.head(4))

# First approach to see if there is any missing value
null_values = df[['GarageArea','SalePrice']].isna().sum()
print("\nTotal number of null values\n", null_values)

# Alternative way
# to check if there us a missing value in the attributes we are interested
print("\nAlternative way to see the Total number of null values")
print(df[['GarageArea','SalePrice']].info())

# to have the statistics about feature and target value
print("\nStatistics about the dataframe")
print(df[['GarageArea','SalePrice']].describe())


# To get the skewness of the feature and target
print("Skewness of the feature and target")
print(df[['GarageArea', 'SalePrice']].skew(axis = 0, skipna = True))

# Histogram

fig = plt.figure(figsize=(10, 6))
df['GarageArea'].plot(kind='hist', bins = 20)
plt.title("GarageArea")
#plt.show()
fig.savefig("hist_GarageSale.png",  dpi=fig.dpi)
print("Histogram of GarageArea is saved")

# Histogram of the SalePrice
plt.clf()
fig = plt.figure(figsize=(10, 6))
df['SalePrice'].plot(kind='hist', bins = 30)
plt.title("SalePrice")
# plt.show()
fig.savefig("hist_SalePice.png",  dpi=fig.dpi)
print("Histogram of SalePrice is saved")

# Scatter plot of GarageArea and SalePrice
plt.clf()
fig = plt.figure(figsize=(20, 12))
# df.plot.scatter(x='GarageArea', y='SalePrice', c='Red')
plt.scatter(df['GarageArea'], df['SalePrice'], alpha=.70, color='r')
plt.title('GarageArea vs SalePrice With Outliers');
# plt.show()
fig.savefig("GarageAreaVsSalePrice_WithOutliers",  dpi=fig.dpi)
print("GarageAreaVsSalePrice_WithOutliers is saved")

# Removing the outliers from the data
mask = (df['GarageArea'] <=1200) & (df['GarageArea'] > 0)
df = df[mask]

# GarageArea vs SalePrice Without Outliers
plt.clf()
fig = plt.figure(figsize=(20, 12))
plt.scatter(df['GarageArea'], df['SalePrice'], alpha=.70, color='r')
# plt.title('GarageArea vs SalePrice With Outliers');
fig.savefig("GarageAreaVsSalePrice_Without_Outliers",  dpi=fig.dpi)
print("GarageAreaVsSalePrice_Without_Outliers is saved")

