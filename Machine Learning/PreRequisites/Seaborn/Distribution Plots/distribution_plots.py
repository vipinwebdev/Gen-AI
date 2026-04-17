# =======================================================================================================
# Distribution Plots
#   Provides an idea about the distribution of data in a given column, typically a numerical column.
#   It helps us understand how the values are spread in that column.
#   It is mainly used for univariate analysis, where we analyze a single numerical variable.
#       1. Histogram
#       2. KDE Plot
#       3. Box Plot
# =======================================================================================================
import matplotlib.pyplot as plt
import plotly.express as px
import seaborn as sns

from data_sets import *

# =======================================================================================================
# 1. Hist Plot
#   Hist plot is used to check the distribution of a numerical column.
#   The bins represent equal intervals, and their size determines how the data is grouped.

### Syntax ---> histplot()
### |---> data ---> DataFrame containing the column
### x ---> column_name
### bins ---> number of bins (intervals) in the histogram
### kde ---> overlays a KDE (Kernel Density Estimate) curve
# =======================================================================================================
tips = sns.load_dataset("tips")
gap = px.data.gapminder()


def histplot_1():
    sns.histplot(data=df, x="Age", hue="Gender", palette="muted")
    plt.show()


def histplot_2():
    sns.displot(data=df, x="Age", hue="Gender")
    plt.show()


def histplot_3():
    sns.displot(data=tips, x="tip", hue="sex", kind='hist', bins=50, element="step")
    plt.show()


def histplot_4():
    sns.histplot(data=gap, x="lifeExp", hue="continent", palette="muted", bins=50)
    plt.show()
# histplot_1()
# histplot_2()
# histplot_3()
# histplot_4()


# =======================================================================================================
# KDE Plot (Kernel Density Estimation)
#
# KDE plot is used to visualize the distribution of a numerical variable in a smooth way.
# It represents the probability density of the data instead of showing exact frequencies like a histogram.
# It helps in understanding the shape, spread, and pattern of the data.
#
# It is mainly used for univariate analysis.

# Used to show the distribution of data in a numerical column.
# Instead of using bins like a histogram, it provides a smooth curve.
# This curve represents the probability density function, showing how the data is distributed.
### Syntax ---> sns.kdeplot()

### |---> data ---> DataFrame containing the column
### x ---> column whose distribution we want to visualize
### hue ---> used to separate data by categories (different colors)
### fill ---> fills the area under the curve (True/False) [default = False]
### bw_adjust ---> controls the smoothness of the curve (higher value = smoother curve)
### color ---> sets the color of the curve
# =======================================================================================================
def kdeplot_1():
    sns.kdeplot(data=df, x="Age",hue='Gender', palette="muted",fill=True)
    plt.show()

def kdeplot_2():
    sns.kdeplot(data=tips, x="total_bill", hue='sex', palette="muted", fill=True)
    plt.show()

# kdeplot_1()
# kdeplot_2()

# =======================================================================================================
# Rug Plot

# Rug plot is used to visualize the distribution of data points in a numerical column.
# It displays small vertical lines (ticks) on an axis, where each tick represents a single data point.
# It is often used along with histplot or kdeplot to better understand data distribution.

### Syntax ---> sns.rugplot()

### |---> data ---> DataFrame containing the column
### x ---> column whose distribution we want to visualize
### hue ---> used to separate data by categories (different colors)
### height ---> controls the height of the ticks
### color ---> sets the color of the ticks
# =======================================================================================================
def rugplot_1():
    sns.kdeplot(data=tips, x="total_bill", hue='sex')
    sns.rugplot(data=tips, x="total_bill",hue='sex')
    plt.show()

# rugplot_1()