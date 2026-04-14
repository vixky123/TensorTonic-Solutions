import numpy as np
import math

def poisson_pmf_cdf(lam, k):
    """
    Compute Poisson PMF and CDF.
    """
    # Write code here
    pmf = ((lam ** k) * (np.exp(-lam)))/math.factorial(k)
    cdf = 0
    for i in range(k+1):
        cdf += ((lam ** i) * (np.exp(-lam)))/(math.factorial(i))

    return pmf , cdf
    pass