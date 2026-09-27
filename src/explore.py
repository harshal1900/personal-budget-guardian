import pandas as pd

df = pd.read_csv('data/raw/amex.csv')

print(f"DataFrame shape: {df.shape}")
print(f"DataFrame columns: {df.columns.tolist()}")
print(f"DataFrame head:\n{df.head()}")
print(f"DataFrame tail:\n{df.tail()}")