import pandas as pd

from dataset import dislikes, channel_name

series = pd.Series(data=dislikes.values, index=channel_name)
print(series)
print(f"Get by key: {series['Mazhavil Manorama']}")
print(f"Dislikes: {dislikes}")
index = int(input("Enter a number: "))
print(f"Indexing -> Item at {index}: {dislikes.iloc[index]}")