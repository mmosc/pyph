""" Sieb des Eratosthenes. """

import numpy as np

def sieb(n):
    """ Returns a boolean array such that the element is true if the 
    corresponding integer is a prime number. """
    
    
    # The returned array, initialised to all true.
    markiert = np.ones(n, dtype=bool)
    
    
    # One is not  prime number.
    markiert[0] = False
    markiert[1] = False
    
    
    # The ceiled square root of the upper integer to check.
    rootn = int(np.ceil(np.sqrt(n)))+1
    
    
    for i in range(2, rootn):
        if markiert[i]==True:
            markiert[i**2::i] = False

    return markiert
    
n = 20
indices = sieb(n)


zahlen = np.arange(n)
print(zahlen[indices])


