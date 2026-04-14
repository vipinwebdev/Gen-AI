import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

from line_plot import df, sales, month_order

data = df['Gender'].value_counts()

x = data.index
y = data.values


# plt.figure(figsize=(10,5))
# plt.title('Univariant bar plot')
# plt.bar(x,y)
# plt.show()
# plt.figure(figsize=(10,5))
# plt.bar(x,y)
# plt.show()

# plt1 = plt
#
# filtered = df[df['Dietary Habits'] != 'Others']
#
# filtered.loc[:, 'Dietary Habits'] = filtered['Dietary Habits'].astype('category')
# filtered.loc[:, 'Dietary Habits'] = (filtered['Dietary Habits'].astype('category')).cat.remove_unused_categories()
# data = filtered.groupby('Dietary Habits', observed=True)['Depression'].sum()
# data1 = filtered['Dietary Habits'].value_counts()
# x1= data1.index
# y1= data.values
# plt1.figure(figsize=(10,5))
# plt1.bar(x1,y1)

# sale = sales.groupby('Country',observed=True)['Boxes Shipped'].sum()
# print(sale)
# x2= sale.index
# y2=sale.values
# plt.xlabel('Countries')
# plt.ylabel('Boxes Shipped')
# plt.bar(x2,y2,color='green')
# plt.show()


# =========================================
#   Horizontal Bar Chart
# =========================================

# sale = sales.groupby('Product',observed=True)['Boxes Shipped'].sum()
# x2= sale.index
# y2=sale.values
# plt.figure(figsize=(15,12))
# plt.xlabel('Countries')
# plt.ylabel('Boxes Shipped')
# plt.barh(x2,y2,color='green')
# plt.show()

# =========================================
#   Multiple Bars
# =========================================

def create_vertical_bar_chart():
    m = sales[sales['Product'] == 'Mint Chip Choco'] \
        .groupby('Date', observed=True)['Amount'].sum()

    s = sales[sales['Product'] == 'Spicy Special Slims'] \
        .groupby('Date', observed=True)['Amount'].sum()

    p = sales[sales['Product'] == 'Peanut Butter Cubes'] \
        .groupby('Date', observed=True)['Amount'].sum()
    m.index = pd.Categorical(m.index, categories=month_order, ordered=True)
    s.index = pd.Categorical(s.index, categories=month_order, ordered=True)
    p.index = pd.Categorical(p.index, categories=month_order, ordered=True)

    m = m.sort_index()  #.reset_index(drop=True)
    s = s.sort_index()  #.reset_index(drop=True)
    p = p.sort_index()  #.reset_index(drop=True)
    plt.figure(figsize=(15, 12))
    plt.xlabel('Countries')
    plt.ylabel('Boxes Shipped')
    bar_width = 0.2
    x3 = np.arange(len(m))
    plt.bar(x3 - bar_width, m.values, label='Mint Chip Choco', width=bar_width)
    plt.bar(x3, s.values, label='Spicy Special Slims', width=bar_width)
    plt.bar(x3 + bar_width, p.values, label='Peanut Butter Cubes', width=bar_width)
    plt.xticks(x3, month_order)
    plt.legend()
    plt.show()


# =========================================
#   Multiple Horizontal Bars
# =========================================
def create_horizontal_bar_chart():
    m = sales[sales['Product'] == 'Mint Chip Choco'] \
        .groupby('Date', observed=True)['Amount'].sum()

    s = sales[sales['Product'] == 'Spicy Special Slims'] \
        .groupby('Date', observed=True)['Amount'].sum()

    p = sales[sales['Product'] == 'Peanut Butter Cubes'] \
        .groupby('Date', observed=True)['Amount'].sum()
    m.index = pd.Categorical(m.index, categories=month_order, ordered=True)
    s.index = pd.Categorical(s.index, categories=month_order, ordered=True)
    p.index = pd.Categorical(p.index, categories=month_order, ordered=True)
    m = m.sort_index()  #.reset_index(drop=True)
    s = s.sort_index()  #.reset_index(drop=True)
    p = p.sort_index()  #.reset_index(drop=True)
    #
    plt.figure(figsize=(15, 12))
    plt.xlabel('Countries')
    plt.ylabel('Boxes Shipped')
    bar_height = 0.2
    y3 = np.arange(0, m.shape[0])
    plt.barh(y3 - bar_height, m.values, label='Mint Chip Choco', height=bar_height)
    plt.barh(y3, s.values, label='Spicy Special Slims', height=bar_height)
    plt.barh(y3 + bar_height, p.values, label='Peanut Butter Cubes', height=bar_height)
    plt.yticks(y3, month_order)
    plt.legend()
    plt.show()

# =========================================
#   Stacked Bars
# =========================================

def create_stacked_bar_chart():
    m = sales[sales['Product'] == 'Mint Chip Choco'] \
        .groupby('Date', observed=True)['Amount'].sum()

    s = sales[sales['Product'] == 'Spicy Special Slims'] \
        .groupby('Date', observed=True)['Amount'].sum()

    p = sales[sales['Product'] == 'Peanut Butter Cubes'] \
        .groupby('Date', observed=True)['Amount'].sum()
    m.index = pd.Categorical(m.index, categories=month_order, ordered=True)
    s.index = pd.Categorical(s.index, categories=month_order, ordered=True)
    p.index = pd.Categorical(p.index, categories=month_order, ordered=True)
    m = m.sort_index()  #.reset_index(drop=True)
    s = s.sort_index()  #.reset_index(drop=True)
    p = p.sort_index()  #.reset_index(drop=True)
    #
    plt.figure(figsize=(15, 12))
    plt.xlabel('Countries')
    plt.ylabel('Boxes Shipped')
    bar_height = 0.2
    y3 = np.arange(0, m.shape[0])
    plt.bar(y3, m.values, label='Mint Chip Choco')
    plt.bar(y3, s.values, label='Spicy Special Slims',bottom=m.values)
    plt.bar(y3, p.values, label='Peanut Butter Cubes',bottom=m.values+s.values)
    plt.xticks(y3, month_order,rotation=90)
    plt.legend()
    plt.show()

# create_stacked_bar_chart()
