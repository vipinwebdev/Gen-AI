# =======================================================================================================
# Bivariate Histogram and KDE Plots.

# These plots are used to analyze the relationship between two numerical variables.
# They help in understanding how the data is distributed jointly for both variables.
#
# Bivariate Histogram divides the 2D space into bins and shows the frequency (or density)
# of data points in each bin.
#
# Bivariate KDE Plot shows a smooth density distribution using contour lines,
# representing areas where data points are concentrated.
#
# These plots are useful for identifying patterns, clusters, and correlations between variables.
# =======================================================================================================

### Bivariate Histogram ---> sns.histplot()

### |---> data ---> DataFrame containing the columns
### x ---> first numerical column
### y ---> second numerical column
### bins ---> number of bins in both directions
### cbar ---> shows color bar for density (True/False)
# =======================================================================================================
### Bivariate KDE Plot ---> sns.kdeplot()

### |---> data ---> DataFrame containing the columns
### x ---> first numerical column
### y ---> second numerical column
### fill ---> fills the contour levels (True/False)
### cmap ---> color map for density visualization
# =======================================================================================================

import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px

tips = sns.load_dataset("tips")
gap = px.data.gapminder()

def b_hist_plot_1():
    sns.histplot(tips,x="total_bill",y="tip")
    plt.show()

def b_hist_plot_2():
    sns.histplot(tips,x="total_bill",y="tip", hue='sex')
    plt.show()

# b_hist_plot_1()
# b_hist_plot_2()

def b_kde_plot():
    sns.kdeplot(tips,x="total_bill",y="tip")
    plt.show()

b_kde_plot()