import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
#%config InlineBackend.figure_formats = ['svg']

# Load data from CSV file
data = pd.read_csv('data.csv')

# Extract title, X-axis label, Y-axis label, and data points
title   = data.columns[0] if len(data.columns[0]) > 0 else 'Sample Line Plot'
x_label = data.columns[1] if len(data.columns[1]) > 0 else 'Sample X-axis Label'
y_label = data.columns[2] if len(data.columns[2]) > 0 else 'Sample Y-axis Label'
d_label = data.columns[3] if len(data.columns[3]) > 0 else 'Sample line label'

# Extract x and y values from the data
x = data[data.columns[0]].tolist() if len(data.columns) > 0 else []
y = data[data.columns[1]].tolist() if len(data.columns) > 0 else []

# Customize the Plot
plt.plot(x, y, marker='o', linestyle='-', color='blue', label=d_label)
plt.title(title)
plt.xlabel(x_label)
plt.ylabel(y_label)
plt.legend()

# Set aspect ratio to be equal and start axes from the origin
#plt.gca().set_aspect('equal', adjustable='box')
plt.axhline(0, color='red', linewidth=0.8)
plt.axvline(0, color='green', linewidth=0.8)

# Remove ticks and labels from both axes
#plt.xticks([])
#plt.yticks([])

# Remove top and right spines
plt.gca().spines['top'].set_visible(False)
plt.gca().spines['right'].set_visible(False)
#plt.gca().spines['bottom'].set_visible(False)
#plt.gca().spines['left'].set_visible(False)


plt.grid(True)

# Save the figure as an SVG file
plt.savefig('plot.svg', format='svg')

# plt.show()
