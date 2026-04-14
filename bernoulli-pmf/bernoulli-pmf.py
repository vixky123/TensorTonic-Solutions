import numpy as np

def bernoulli_pmf_and_moments(x, p):
    """
    Compute Bernoulli PMF and distribution moments.
    """
    x = np.array(x)
    # iterate in x array
    # define an empty array
    # when x(i) == 0 push 1 - p else push p in empty array
    # define variable mean = p , var = p(1-p)
    # return array , mean , var
    pmf = []
    for i in x:
        if i == 0:
            pmf.append(1-p)
        elif i == 1:
            pmf.append(p)

    pmf = np.array(pmf)
    mean = p
    var = p*(1-p)
    return pmf, mean , var
    
    pass 