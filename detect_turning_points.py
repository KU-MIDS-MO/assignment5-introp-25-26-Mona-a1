import numpy as np
import matplotlib.pyplot as plt


signal = np.array([1, 4, 2, 5, 3, 6])

def detect_turning_points(signal, filename="turning_points.pdf"):

    
    b = len(signal)
    direction = 0

    x = []
    y = [range(0, b+1)]
    
    for i in range(1,b):
        if signal[i] > signal[i - 1]:
            curr_direction = 1
            
        elif signal[i] < signal[i - 1]:
            curr_direction = -1
        
        else:
            curr_direction = 0
        
        if curr_direction == 0:
            continue
        
        if direction == 0:
            direction = curr_direction
            
            
        if curr_direction != direction:
            x.append(i-1)
        
        direction = curr_direction

    print(x)




    xy = np.arange(b)
    
    plt.plot(xy, signal, label='Signal', color='green')
    
        
    

    plt.scatter(x,signal[x], s=80, label = 'Turning points')

    plt.xlabel('Position')
    plt.ylabel('Value')
    plt.legend()
    plt.title('Turning points')
    plt.savefig(filename)
    plt.show()
    
    return np.array(x)
    
    pass
    ### Replace with your own code (end)   ###
print(detect_turning_points(signal, filename="turning_points.pdf"))