'''
3. Implement linear SVM method using scikit library
Use the same dataset above
Use train_test_split to create training and testing part
Evaluate the model on testing part using score and
classification_report(y_true, y_pred)
'''

import os
import pandas as pd
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.svm import LinearSVC
from sklearn.metrics import classification_report

# load the file
filename = os.getcwd() + "\\data\\glass.csv"
df = pd.read_csv(filename)

# to see the fields
# print(df.info())

# select the feature column
X = df.drop("Type", axis=1)

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

# lsvm = LinearSVC(random_state=0, tol=1e-5)
lsvm = LinearSVC()

# train the model using fit() method
lsvm.fit(X_train, y_train)

# print the model accuracy
print(f"Accuracy of Linear SVM  on training set {round(lsvm.score(X_train, y_train),2)}")
print(f"Accuracy of Linear SVM  on test set {round(lsvm.score(X_test, y_test),2)}")

y_pred = lsvm.predict(X_test)
print(classification_report(y_test, y_pred))


