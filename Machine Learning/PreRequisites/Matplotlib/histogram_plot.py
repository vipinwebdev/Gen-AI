import matplotlib.pyplot as plt

from line_plot import df

filtered = df[df['Age'].isin(
    df['Age'].value_counts()[lambda x: x > 5].index
)]
plt.hist(filtered['Age'], bins=10, edgecolor='black')
plt.xlabel('Age')
plt.ylabel('Frequency')
plt.title('Age Distribution')
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.show()
