import numpy as np
from numpy.polynomial import Polynomial as P

'''
Calculate the 'dividierte Differenzen' for the given requirements
degree_needed : required degree of the interpolation
fct : the function used to evaluate the corresponding y_i values throught the given list of x_i
lst_x : the list of x_i values
'''
def newton_interpolation_dd(degree_needed, fct, lst_x):
    #resetting the required degree
    if degree_needed >= len(lst_x):
        degree_needed = len(lst_x)-1
    result = np.zeros(sum(np.arange(degree_needed+2)))
    #need some fine tuning work on this 
    for h in range(degree_needed+1):
        result[h] = fct(lst_x[h])
    index_inner = np.arange(degree_needed+1, 0, -1)
    for i in range(degree_needed):
        offset = sum(index_inner[:i])
        off_set_j = sum(index_inner[:i+1])
        for j in range(index_inner[i]-1):
            result[j+off_set_j] = (result[j+1+offset] - result[j+offset])/(lst_x[j+1+i] - lst_x[j])
    target_index = [sum(index_inner[:i]) for i in range(degree_needed+1)]
    return [round(result[k], 8) for k in target_index]

def newton_interpolation(degree, fct, lst_x):
    dd = np.array(newton_interpolation_dd(degree, fct, lst_x))
    tmp = dd.reshape((1, len(dd)))
    lst_fct = np.append(np.array([1]), np.cumprod([P([-i, 1]) for i in lst_x[:-1]]))       
    return np.sum(dd * lst_fct)

'''
Calculate the tschebyschev-abzisse values as ndarray with the given parameters
n : number of points
a : beginning value
b : ending value
'''
def tscheb(n, a, b):
    return np.array([(b-a)/2*np.cos((2*k +1)/(n+1)*np.pi/2)+(b+a)/2 for k in range(n+1)])
  
'''
Calculate the absolute difference between 2 values in the given parameter
lst : list of numbers
'''
def distance_array(lst):
    return np.array([np.abs(lst[i]-lst[i+1]) for i in range(len(lst)-1)])

'''
Return the max value in the given array
'''
def max_h(lst):
    return np.max(distance_array(lst))

