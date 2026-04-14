import numpy as np

def sample_var_std(x):
    """
    Compute sample variance and standard deviation.
    """
    x = np.array(x)
    mean = np.sum(x)/np.size(x)
    sum = 0
    for i in range(np.size(x)):
        sum += (x[i] - mean) ** 2
    var = sum/(len(x) - 1)
    std = var ** 0.5
    return  var , std
    pass