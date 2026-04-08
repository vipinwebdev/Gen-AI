import pandas as pd

# data = pd.read_csv("../../Global-YouTube-Statistics.csv", encoding='latin1', low_memory=False)
# data = pd.read_csv("../../Global-YouTube-Statistics.csv", encoding='latin1', low_memory=False).squeeze("columns")
data = pd.read_csv("../../Global-YouTube-Statistics_Two_column.csv", encoding='latin1', low_memory=False, index_col='Youtuber')
print(data)
print(type(data))

print("Head: ",data.head())
print("Tail: ",data.tail())
print("Shape: ",data.shape)
print("Values: ",data.values)
print("Dimensions: ",data.ndim)