import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv("Datasets/student_depression_dataset.csv")  # Data gathering
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

sales = pd.read_csv("Datasets/Chocolate_Sales.csv")
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

data.index = pd.Categorical(data.index, categories=month_order, ordered=True)

data = data.sort_index()

def plot_charts():
    # =========================================
    #   Simple line
    # =========================================
    # x = df.head(20).index
    # plt.figure(figsize=(10,5))
    # plt.title("Age", color='green')
    # plt.xlabel("Row")
    # plt.ylabel("Age")
    # plt.plot(df['Age'].head(20).sort_values(),df['CGPA'].head(20), color='red', linestyle='dashed', marker='o')
    # plt.show()

    # =========================================
    #   Age vs CGPA
    # =========================================
    # plt.title("Age", color='green')
    # plt.xlabel("Row")
    # plt.ylabel("Age")
    # plt.plot(x, df['Age'].head(20).sort_values().reset_index(drop=True), color='red', linestyle='dashed', marker='o')
    # plt.plot(x, df['CGPA'].head(20).sort_values().reset_index(drop=True), color='green', linestyle='dotted', marker='s')
    # plt.show()
    # print(df['Age'].head(20).sort_values().reset_index(drop=True))
    # print(df['CGPA'].head(20).sort_values().reset_index(drop=True))


    # =========================================
    #   Age wise CGPA
    # =========================================
    # y = df.groupby('Age')['CGPA'].mean()
    # x= y.index
    # plt.figure(figsize=(10,5))
    # plt.title("Age wise CGPA", color='green')
    # plt.xlabel("Age")
    # plt.ylabel("CGPA")
    # plt.grid(True)
    # plt.plot(x, y, color='red', linewidth=2, linestyle='--', marker='o')
    # plt.show()


    # Q: Top 10 Populated City, Provide Mean Financial Stress Value
    # =========================================
    #   Financial Stress Mean of Top 10 Populated Cities
    # =========================================

    # x = df['City'].value_counts().head(10).sort_index()
    # y = df[df['City'].isin(x.index)].groupby('City', observed=True)['Financial Stress'].mean().sort_index()
    #
    # print(x,"\n",y)
    #
    # plt.figure(figsize=(10,5))
    # plt.title('Financial Stress Mean of Top 10 Populated Cities')
    # plt.xlabel('City')
    # plt.ylabel('Financial Stress')
    # plt.grid(True)
    # plt.plot(x.index,y, linestyle='dashed', marker='o', markerfacecolor='blue', markersize=10)
    # plt.show()

    # ======================================================================================================================
    #   Working with another data set
    # ======================================================================================================================

    sales.info()


    x = data.index
    y = data.values

    plt.figure(figsize=(10, 5))
    plt.title('Sales Amount by Month')
    plt.xlabel('Month')
    plt.ylabel('Sales')
    plt.grid()
    plt.plot(x, y, linestyle='dashed', marker='o', markerfacecolor='blue', markersize=10)
    plt.show()
