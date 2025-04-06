import matplotlib.pyplot as plt

products = ['Product A', 'Product B', 'Product C', 'Product D', 'Product E']
sales = [200, 150, 250, 175, 225]

colors = ['blue', 'orange', 'green', 'red', 'purple']

plt.figure(figsize=(10, 6))
plt.bar(products, sales, color=colors)

plt.title('Sales Data')
plt.xlabel('Products')
plt.ylabel('Sales (Units)')

plt.grid(axis='y', alpha=0.75)
plt.show()