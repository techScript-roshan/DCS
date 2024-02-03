import matplotlib.pyplot as plt
import pandas as pd

# Load data from CSV file
data = pd.read_csv('4.csv')

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
    plt.plot(x, y, color='red', alpha=.8, label=d_label, linewidth=1)
    plt.fill_between(x, y, color='red', alpha=.4)
    
    plt.gca().set_aspect('equal', adjustable='box')  # Set aspect ratio to be equal
    plt.gca().spines['top'].set_visible(False)
    plt.gca().spines['right'].set_visible(False)
    plt.gca().spines['bottom'].set_visible(False)
    plt.gca().spines['left'].set_visible(False)



    plt.title(title)
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    #plt.legend()
    plt.grid()

    plt.savefig(op_file + '.svg', format='svg')
    #plt.show()

# Call the function with data and output name
plot_data(data)
