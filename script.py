# import kagglehub
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Download latest version
path = "./data/dementia_patients_health_data.csv"
df = pd.read_csv(path)

print(df)

print(df.describe())
print(df.columns)

df.hist()
# df.boxplot()

print(df.isna().sum())
print(len(df))

print(set(df["Prescription"].tolist()),set(df["Chronic_Health_Conditions"].tolist()))
print(df)
df = pd.get_dummies(df, columns=["Prescription", "Chronic_Health_Conditions"])
df = pd.get_dummies(df, drop_first=True)

print(df.dtypes)

df.to_pickle("./data/dementia_one_hot_encoded.pkl")

