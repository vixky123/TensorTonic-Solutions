import numpy as np
from scipy.special import comb

def binomial_pmf_cdf(n, p, k):
    """
    Compute Binomial PMF and CDF.
    """
    # Write code here
    # for pmf use comb(n, k) *pow(p,k) * pow(1-p , n-k)
    # cdf = 0
    # for i in range(k):
    # cdf += comb(n , i) * pow(p, i) * pow(1-p , n-i)
    if k < 0:
        return 0.0, 0.0
    if k > n:
        return 0.0, 1.0

   
    if p == 0:
        pmf = 1.0 if k == 0 else 0.0
        cdf = 1.0
        return pmf, cdf

   
    if p == 1:
        pmf = 1.0 if k == n else 0.0
        cdf = 0.0 if k < n else 1.0
        return pmf, cdf

    pmf = comb(n, k) * (p ** k) * ((1-p) ** (n-k))
    cdf = 0
    for i in range(k+1):
        cdf += comb(n , i) * (p ** i)*((1-p) ** (n-i))

    return pmf , cdf

    
    pass