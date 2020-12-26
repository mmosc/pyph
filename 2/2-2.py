"""kleine Einmaleins. """

import numpy as np

# Define the array a of shape (9,1)
a = np.arange(1,10).reshape(9,1)


# Define the array b of shape (1,9)
b = np.arange(1, 10).reshape(1,9)


produkt = a * b
print(produkt)



