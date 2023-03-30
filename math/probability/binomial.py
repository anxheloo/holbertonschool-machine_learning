#!/usr/bin/env python3
""" defines Normal class that represents normal distribution """


class Binomial:
    """class that represents normal distribution"""
    def __init__(self, data=None, n=1 , p=0.5):
        """class constructor""" 
        self.n = int(n)
        self.p = float(p)
        if self.n <= 0:
            raise ValueError("n must be a positvice value")
        if p <= 0 or p >=1:
             raise ValueError("p must be greater than 0 and less than 1")
        if data is not None:
            if type(data) is not list:
                raise TypeError("data must be a list")
            if len(data) < 2:
                raise ValueError("data must contain multiple values")
            mean = float(sum(data) / len(data))
            summation = 0
            for x in data:
                summation += ((x - mean) ** 2)
            variance = (summation / len(data))
            q = variance / mean
            p = (1 - q)
            n = round(mean / p)
            p = float(mean / n)
            self.n = n
            self.p = p
            
    def pmf(self,k):
        """A class Exponential that represents a Exponential distribution"""
        k = int(k)
        if k < 0 or k > self.n:
            return 0
        else:
            return(math.comb(self.n, k) * (self.p ** k) * ((1 - self.p) ** (self.n - k)))
        
    def cdf(self,k):
        k = int(k)
        if k < 0:
            return 0
        cdf = 0
        for i in range(k + 1):
            cdf += self.pmf(i)
        return cdf
