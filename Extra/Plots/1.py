import matplotlib.pyplot as plt
import pandas as pd

# Load data from CSV file
data = pd.read_csv('1.csv')

def plot_data(data):

    # Extract title, X-axis label, Y-axis label, and data points
    title   = data.columns[0]
    x_label = data.columns[1]
    y_label = data.columns[2]
    d_label = data.columns[3]
    op_file = data.columns[4]
    
    # Extract x and y values from the data
    x = data[data.columns[0]].tolist()
    y = data[data.columns[1]].tolist()
    
    # Customize the Plot
    plt.plot(x, y, marker='o', linestyle='-', color='black', label=d_label)
    plt.title(title)
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    plt.legend()
    plt.grid()

    plt.savefig(op_file + '.svg', format='svg')

# Call the function with data and output name
plot_data(data)
