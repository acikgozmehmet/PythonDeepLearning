'''2. Implement Naïve Bayes method using scikit-learn library
Use dataset available in https://umkc.box.com/s/ea6wn1cidukan67t02j60nmp1ljln3kd
Use train_test_split to create training and testing part
Evaluate the model on testing part using score and
classification_report(y_true, y_pred)
'''

import os
import pandas as pd
from sklearn.naive_bayes import GaussianNB
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report, confusion_matrix

# load the file
filename = os.getcwd() + "\\data\\glass.csv"
df = pd.read_csv(filename)

# to see the fields
# print(df.info())

# RI,Na,Mg,Al,Si,K,Ca,Ba,Fe,Type
# select the feature column
X = df.drop("Type",axis=1)

# select the target column
y = df["Type"]

print(f"Class labels: {y.unique()}\n")
print(f"Dimension of all data : {df.shape}")
print(f"Dimension of features : {X.shape}")
print(f"Dimension of Target : {y.shape}")

# split the dataset as 70% for training and 30% for testing
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=0)

# print the train and test shape
print(f"\nFeatures used in training: {X_train.shape[0]}\nFeatures used as Target in Training: {y_train.shape[0]}\n")
print(f"Features used in Test: {X_test.shape[0]}\nFeatures used as Target in Test: {y_test.shape[0]}\n")

# create a naive bayes model using GaussianNB()
nb = GaussianNB()

# train the model using fit() method
nb.fit(X_train, y_train)

# print the model accuracy
print(f"Accuracy of Naive Bayes on training set {round(nb.score(X_train, y_train),2)}")
print(f"Accuracy of Naive Bayes on test set {round(nb.score(X_test, y_test),2)}")

y_pred = nb.predict(X_test)
print(classification_report(y_test, y_pred))
