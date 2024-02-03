import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# Generate data for Stress = 10fck*ep - 25fck*ep^2
x_values = np.arange(0, 3.6, .1) # (0 to 3.5)/1000 
y_values = np.where((x_values <= 0.002 * 1000), 1*(10 * x_values / 10 - 25 * (x_values / 10)**2), 1.0)

# Create a DataFrame from the generated data
data = pd.DataFrame({'X': x_values, 'Y': y_values})

def plot_data(data):
    # Extract x and y values from the data
    x = np.array(data['X'])
    y = np.array(data['Y'])
       
    # Customize the Plot
    plt.plot(x, y, marker='', linestyle='-', color='black', label='$f_{ck}$')
    plt.plot(x, y * .67, marker='', linestyle='-', color='blue', label='$0.67f_{ck}$')
    plt.plot(x, y * .67 / 1.5 , marker='', linestyle='-', color='red', label='$0.67f_{ck}/\gamma_m$')
    plt.fill_between(x, y, where=(x_values <= 0.002 * 1000), color='yellow', alpha=0.3)
    plt.fill_between(x, y, where=(x_values >= 0.002 * 1000), color='green', alpha=0.3)

    plt.title('$\sigma - \epsilon$')
    plt.ylabel('$\sigma / f_{ck}$')
    plt.xlabel('$\epsilon x 10^3$')
    plt.legend()
    plt.grid()

    plt.savefig('5.svg', format='svg')
    #plt.show()

# Call the function with data and output name
plot_data(data)
