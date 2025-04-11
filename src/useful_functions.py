import numpy as np
def solve_quadratic_function(a,b,c):
    delta = b**2 - 4*a*c
    x1 = (-b-np.sqrt(delta))/(2*a)
    x2 = (-b+np.sqrt(delta))/(2*a)
    return x1, x2