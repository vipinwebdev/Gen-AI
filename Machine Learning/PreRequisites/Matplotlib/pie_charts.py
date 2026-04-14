from matplotlib import pyplot as plt

from line_plot import df, sales


def simple_pie_chart():
    data = df['Dietary Habits'].value_counts()
    plt.pie(data.values, labels=data.index)
    plt.show()


def create_pie_chart():
    data = df['Dietary Habits'].value_counts()
    plt.pie(data.values, labels=data.index, autopct='%1.1f%%',
            shadow=True, startangle=90,colors=['red','green','blue','yellow'],
            explode=(0.05,0.05,0.05,0.05))
    plt.legend()
    plt.show()

def pie_chart_of_sales():
    data = sales.groupby('Country',observed=True)['Amount'].value_counts().head(5)
    plt.pie(data.values, labels=data.index, autopct='%1.1f%%',
            shadow=True, startangle=90)
    plt.legend()
    plt.show()
# simple_pie_chart()
# create_pie_chart()
pie_chart_of_sales()