from data_sets import *

def regression_plot():
    sns.regplot(x="total_bill", y="tip", data=tips)
    plt.show()

def regression_plot_1():
    sns.regplot(x="lifeExp", y="gdpPercap", data=gap)
    plt.show()

# regression_plot()
# regression_plot_1()

# =======================================================================================================
# Multi Plot
# =======================================================================================================

# 1. Joint Plot
def multi_plot_1():
    sns.jointplot(x="total_bill", y="tip", data=tips)
    plt.show()

def multi_plot_2():
    sns.jointplot(x="total_bill", y="tip", data=tips, kind="reg")
    plt.show()

# multi_plot_1()
# multi_plot_2()

def multi_plot_3():
    sns.pairplot(data= tips, hue="day", kind="reg")
    plt.show()

def multi_plot_4():
    sns.pairplot(data=df, kind="reg")
    plt.show()

# multi_plot_3()
# multi_plot_4()