import numpy as np
import matplotlib.pyplot as plt

labels = ['T1', 'T2', 'T3', 'T4']
category_a = [10, 15, 20, 25]
category_b = [20, 25, 30, 20]
category_c = [30, 15, 10, 15]

plt.figure(figsize=(10, 6))
plt.bar(labels, category_a, label='Category A', color='blue')
plt.bar(labels, category_b, bottom=category_a, label='Category B', color='orange')
plt.bar(labels, category_c, bottom=np.array(category_a) + np.array(category_b), label='Category C', color='green')

plt.title('Stacked Bar Chart of Categories Over Time Periods')
plt.xlabel('Time Periods')
plt.ylabel('Values')

plt.legend()

plt.grid(axis='y', alpha=0.75)
plt.show()