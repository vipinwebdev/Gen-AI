# =======================================================================================================
# Bar Plot
# =======================================================================================================#%%
from data_sets import *

def bar_1():
    sns.barplot(x="continent", y="lifeExp", data=gap)
    plt.show()

def bar_2():
    sns.barplot(x="continent", y="gdpPercap", data=gap)
    plt.show()

def bar_3():
    sns.barplot(x="Dietary Habits", y="Depression", data=df,hue='Gender')
    plt.show()

def bar_4():
    sns.barplot(data=tips, x="sex", y="total_bill", hue="smoker")
    plt.show()
    plt.show()

# bar_1()
# bar_2()
# bar_3()
# bar_4()


# =======================================================================================================
# Count Plot
# =======================================================================================================

def count_plot_1():
    sns.countplot(x="continent", data=gap)
    plt.show()

def count_plot_2():
    sns.countplot(x="day", data=tips,hue="sex")
    plt.show()


# count_plot_1()
# count_plot_2()

# =======================================================================================================
# Box Plot
# =======================================================================================================

def box_plot_1():
    sns.boxplot(x="day", y="total_bill", data=tips)
    plt.show()

def box_plot_2():
    sns.boxplot(data=df, x="CGPA",hue="Gender")
    plt.show()

def box_plot_3():
    sns.boxplot(x="continent", y="lifeExp", data=gap)
    plt.show()

# box_plot_1()
# box_plot_2()
# box_plot_3()

# =======================================================================================================
# Violin Plot
# =======================================================================================================
def violin_plot_1():
    sns.violinplot(x="continent", y="lifeExp", data=gap)
    plt.show()

def violin_plot_2():
    sns.violinplot(x="total_bill", data=tips,hue="sex")
    plt.show()

# violin_plot_1()
# violin_plot_2()

# =======================================================================================================
# Swarm Plot
# =======================================================================================================

def swarm_plot_3():
    sns.swarmplot(x="Country",y="Boxes Shipped", data=sales)
    plt.show()

swarm_plot_3()
