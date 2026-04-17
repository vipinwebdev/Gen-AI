"""
Relational plot is being used to figure out the relationship between two or more numerical variables.
It helps us out to figure out that on bringing the changes in one numerical column,
how it affects the other numerical column.
"""

import matplotlib.pyplot as plt
import plotly.express as px
import seaborn as sns

from data_sets import df


def line_plot_1():
    sns.lineplot(data=df, x='Age', y='CGPA')
    plt.show()


def line_plot_2():
    sns.lineplot(data=df, x='Age', y='Financial Stress')
    plt.show()


def line_plot_3():
    sns.lineplot(data=df, x='Age', y='Financial Stress', hue='Gender')
    plt.show()


tips = sns.load_dataset("tips")


def line_plot_4():
    sns.lineplot(data=tips, x='day', y='total_bill', hue='sex', style='smoker')
    plt.show()


# ======================================================================================================
#   Insights
#   1. People coming for lunch are coming only on Thursday or Friday
#   2. People coming for lunch are smokers as well paying bill on thursday then Non smokers
#   3. Non-smokers are coming for dinner everyday while smokers for dinner are not coming on thursday.
#   4. Non-smokers for dinner are always paying less bill than smoker at dinner
# ======================================================================================================

# line_plot_1()
# line_plot_2()
# line_plot_3()
# line_plot_4()


# =======================================================================================================
# Working with plotly
# => gapminder dataset -> Is the population and life expectancy of people from a fixed year in multiple countries are continents.
# country, continent, year, lifeExp, pop, gdpPercap, iso_alpha, iso_num
# =======================================================================================================

gap = px.data.gapminder()
# sns.lineplot(data=gap, x='year', y='lifeExp', hue='continent')
# plt.show()
grouped = gap.groupby(['year', 'continent'])['lifeExp'].mean().reset_index()


def plotly_chart_1():
    fig = px.line(grouped, x="year", y="lifeExp", color="continent", title="Life Expectancy")
    fig.show()


# plotly_chart_1()

# =======================================================================================================
# Scatter Plot
# =======================================================================================================
def scatter_plot_1():
    sns.scatterplot(data=tips, x="total_bill", y="tip", hue="sex", size="size")
    plt.show()


def scatter_plot_2():
    sns.relplot(data=tips, x="total_bill", y="tip", hue="sex", size="size", kind="scatter")
    plt.show()


def scatter_plot_3():
    sns.scatterplot(data=gap, x="lifeExp", y="pop", hue="continent")
    plt.show()


# scatter_plot_1()
# scatter_plot_2()
# scatter_plot_3()

# =======================================================================================================
# Facet Plot
# It can help us divide the plot as per the multiple categories of a categorical column such as we don't want to use hue,
# and we want to divide the plot or graph as the multiple categories of a categorical column as row wise or column wise.
# =======================================================================================================

def facet_plot_1():
    sns.relplot(data=tips, x="total_bill", y="tip", col="sex", kind="scatter")
    plt.show()


def facet_plot_2():
    sns.relplot(data=tips, x="total_bill", y="tip", row="sex", kind="scatter")
    plt.show()


def facet_plot_3():
    sns.relplot(data=tips, x="total_bill", y="tip", row="smoker", col='sex', kind="scatter")
    plt.show()


def facet_plot_4():
    """
    col_wrap --> Life Expectancy for a country year wise in multiple columns.
    Total Countries --> 12 --> 12 columns
    12 columns -->  1st row --> 3 columns
                    2nd row --> 3 columns
                .... 4th row --> 3 columns
    col_wrap --> 3 --> 3 total columns are going to be their in first row.
    :return:
    """
    sns.relplot(data=gap, x="lifeExp", y="pop", col='year', col_wrap=3, kind="scatter")
    plt.show()

# facet_plot_1()
# facet_plot_2()
# facet_plot_3()
# facet_plot_4()
