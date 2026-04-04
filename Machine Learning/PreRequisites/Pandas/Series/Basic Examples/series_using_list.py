import pandas as pd

# Series from a list
marks = pd.Series([85, 78, 89, 94, 87])
print(f"Series from a simple list:\n{marks}")

# Series with custom index
students = pd.Series([85, 78, 89, 94, 87], index=['A', 'B', 'C', 'D', 'E'])
print(f'\nSeries with custom index:\n{students}')

# Series with data, custom index, and custom name
ratings = pd.Series(data=[4.9, 4.2, 4.6, 4.8, 4.5], index=['A', 'B', 'C', 'D', 'E'], name='Rating')
print(f'\nSeries with custom name:\n{ratings}')

# Series with scaler value
scaler_series = pd.Series(4, index=['A', 'B', 'C', 'D', 'E'])
print(f'\nSeries with custom scaler:\n{scaler_series}')