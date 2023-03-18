#!/usr/bin/env python3
"""A class Exponential that represents a Exponential distribution"""


class Exponential:
    """A class Exponential that represents a Exponential distribution"""
    def __init__(self, data=None, lambtha=1.):
        self.lambtha = float(lambtha)
        if self.lambtha <= 0:
            raise ValueError("lambtha must be a positvice value")
        if data is not None:
            if type(data) is not list:
                raise TypeError("data must be a list")
            if len(data) < 2:
                raise ValueError("data must contain multiple values")
            self.lambtha = float(len(data)/sum(data))

    def pdf(self,x):
        """A class Exponential that represents a Exponential distribution"""
        if x < 0:
            return 0
        e = 2.7182818285
        pdf = self.lambtha * (e**(-self.lambtha*x))
        return pdf

    def cdf(self,x):
        """A class Exponential that represents a Exponential distribution"""
        if x < 0:
            return 0
        e = 2.7182818285
        cdf = 1 - (e**(-self.lambtha*x))
        return cdf
