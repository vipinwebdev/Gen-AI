import pandas as pd
from dataset import likes

print(f"Sum of likes: {likes.sum()}")
print(f"Minimum likes: {likes.min()}")
print(f"Maximum likes: {likes.max()}")
print(f"Product of likes: {likes.prod()}")
print(f"Average likes: {likes.mean():.2f}")
print(f"Mode of likes: {likes.mode()}")
print(f"Standard deviation of the likes: {likes.std():.2f}")
print(f"Summary of likes:\n{likes.describe()}")
