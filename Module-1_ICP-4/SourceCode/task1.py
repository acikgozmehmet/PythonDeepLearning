import os
import pandas as pd

# 1. find the correlation between ‘survived’ (target column) and ‘sex’ column for the Titanic use case in class.

# load the file
filename = os.getcwd() + "\\data\\train_preprocessed.csv"
df = pd.read_csv(filename)

# ckeck the data
# print(df.head(3))
print(df.info())

# estimate the correlation
corr_Sex_Survived = df[["Survived", "Sex"]].groupby("Sex", as_index=False).mean().\
                                            sort_values(by="Survived", ascending=True)

print("\nCorrelation:\n", corr_Sex_Survived)
