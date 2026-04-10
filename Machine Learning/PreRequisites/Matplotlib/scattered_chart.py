import matplotlib.pyplot as plt
from line_plot import df,sales

x = sales['Boxes Shipped']
y = sales['Amount']

plt.figure(figsize=(10,5))
plt.title('Total Amount as Per Boxes Shipped')
plt.xlabel('Boxes Shipped')
plt.ylabel('Amount')
plt.scatter(x,y)
plt.show()


