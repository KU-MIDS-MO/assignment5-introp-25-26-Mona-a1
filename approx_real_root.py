import numpy as np
import matplotlib.pyplot as plt

coeffs = [1, -4, 0, 1]
interval = (0.0, 1.0)


def approx_real_root(coeffs, interval):

    a, b = interval
    c0, c1, c2, c3 = coeffs
    
    fa = ((c3 * a + c2) * a + c1) * a + c0
    fb = ((c3 * b + c2) * b + c1) * b + c0
    
    if fa ==0.0:
        return float(a)
    
    if fb == 0.0:
        return float(b)
    
    while b -a > 1e-9:
        k = 0.5 * (a+b)
        fk = ((c3 * k + c2) * k + c1) * k + c0
        
        if fk == 0.0:
            return k
        
        if fa * fk < 0:
            b, fb = k, fk
            
        else:
            a, fa = k, fk
            
    
    return 0.5 * (a+b)



    pass
    ### Replace with your own code (end)   ###
print(approx_real_root(coeffs, interval))