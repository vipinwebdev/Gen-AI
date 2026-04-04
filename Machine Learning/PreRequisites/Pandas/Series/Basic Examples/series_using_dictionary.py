import pandas as pd

students = {
    'Ajay':75,
    'Bob':80,
    'Carol':86,
    'David':90,
    'Joey':95,
}
dict_series = pd.Series(students,name='Students')
print(f"\nSeries using dictionary:\n{dict_series}")