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

# plt.savefig("./figures/")




