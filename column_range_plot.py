import numpy as np
import matplotlib.pyplot as plt


A = np.array([[1., 4., 9.],
              [3., 1., 5.],
              [7., 2., 8.]])


def column_range_plot(A, filename="column_ranges.pdf"):
    

    B = []
    
    for i in range(A.shape[1]):
        x = A[:,i]
        z = x.max() - x.min()
        
        B.append(z)
     
    xAchse = []
    
    for i in range(0, A.shape[1]):
        xAchse.append(i+1)
    
    colors = ['orange','green', 'blue']

    plt.bar(xAchse,B, color = colors, label=f"Column {i}")
    plt.savefig(filename)
    
    bars = plt.bar(xAchse, B, color=colors)
    
    plt.legend(bars, ['Column 1', 'Column 2', 'Column 3'], title="My Legend", loc= "upper right", frameon=False)
    plt.title("Plot with Ranges of Columns in A")
    plt.xlabel('Column')
    plt.ylabel('Range')
    plt.savefig(filename)
    plt.show()

    return np.array(B, dtype = float)

    ### Replace with your own code (end)   ###
print(column_range_plot(A, filename="column_ranges.pdf"))

