import numpy as np
from collections import Counter

def mean_median_mode(x):
    """
    Compute mean, median, and mode.
    """
    # Write code here
    x = np.array(x)
    mean = np.sum(x)/np.size(x)
    x = np.sort(x)
    sz = np.size(x)
    if sz%2 == 1:
        median = x[sz // 2]
    else:
        median =((x[sz // 2 -1]) + x[sz // 2])/2

    freq = Counter(x)
    maxi = max(freq.values())

    mode = min(i for i , v in freq.items() if v == maxi)

    return mean , median , mode
    

    
    
    pass