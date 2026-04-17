# =======================================================================================================
# Matrix Plot
from streamlit import columns

# Matrix plot shows the relationship between two dimensions in a tabular form,
# using colors to represent the strength or intensity of the data.

# It is similar to Excel sheets, where instead of numbers,
# color intensity is used to understand the values.
# =======================================================================================================



# =======================================================================================================
# Heatmap

# In many machine learning problems (especially classification),
# heatmaps are used to visualize relationships and patterns in data.
# =======================================================================================================
import matplotlib.pyplot as plt
import plotly.express as px
import seaborn as sns
from data_sets import df,sales

tips = sns.load_dataset("tips")
gap = px.data.gapminder()
gap = gap[gap['continent']== 'Asia']
pivot_table = gap.pivot(index="country",columns="year", values="lifeExp")

# =======================================================================================================
### Syntax ---> sns.heatmap()

### |---> data ---> 2D data (matrix, pivot table, or correlation matrix)
### annot ---> displays values inside cells (True/False)
### cmap ---> color map (e.g., 'coolwarm', 'viridis','summer')
### linewidths ---> width of lines between cells
### linecolor ---> color of the lines between cells
### cbar ---> shows color bar (True/False)
### fmt ---> format of annotation (e.g., '.2f', 'd')
### vmin, vmax ---> control range of values for color scaling
# =======================================================================================================
def matrix_1():
    plt.figure(figsize=(15, 10))
    sns.heatmap(pivot_table, annot=True, cmap='summer', linewidths=0.5)
    plt.show()

"""
What is clustermap in Seaborn?

clustermap is an advanced version of a heatmap in Seaborn that not only shows values using colors 
but also groups (clusters) similar rows and columns together.

A clustermap = heatmap + automatic grouping (clustering)

What it does
Reorders rows and columns based on similarity
Groups similar data points together
Shows dendrograms (tree-like structures) on 

sns.clustermap() internally uses SciPy for clustering
pip install scipy
"""
def matrix_2():
    sns.clustermap(pivot_table, cmap='coolwarm', figsize=(12, 8))
    plt.show()

matrix_2()