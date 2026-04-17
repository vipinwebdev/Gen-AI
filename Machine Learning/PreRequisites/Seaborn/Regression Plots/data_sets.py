import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
tips = sns.load_dataset("tips")
gap = px.data.gapminder()
df = pd.read_csv("../Dataset/student_depression_dataset.csv")  # Data gathering
categorical_cols = [
    'City',
    'Profession',
    'Academic Pressure',
    'Sleep Duration',
    'Dietary Habits',
    'Degree',
    'Have you ever had suicidal thoughts ?',
    'Family History of Mental Illness',
    'Gender'
]


df = df[df['Financial Stress'] != '?']

df[categorical_cols] = df[categorical_cols].astype('category')
df['Financial Stress'] = df['Financial Stress'].astype('int64')

sales = pd.read_csv("../Dataset/Chocolate_Sales.csv")
sales['Date'] = pd.to_datetime(sales['Date'], format='%d-%b-%y')
sales['Sales Person'] = sales['Sales Person'].astype('category')
sales['Country'] = sales['Country'].astype('category')
sales['Product'] = sales['Product'].astype('category')
sales['Date'] = sales['Date'].dt.month_name()
sales['Date'] = sales['Date'].astype('category')

sales['Amount'] = sales['Amount'].str.strip("$").str.replace(",", "")
sales['Amount'] = sales['Amount'].astype('int32')
sales['Boxes Shipped'] = sales['Boxes Shipped'].astype('int32')
data = sales.groupby('Date', observed=True)['Amount'].sum()

month_order = [
    'January', 'February', 'March', 'April', 'May', 'June',
    'July', 'August'
]
