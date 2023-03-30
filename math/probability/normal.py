#!/usr/bin/env python3
""" defines Normal class that represents normal distribution """


class Normal:
    """class that represents normal distribution"""
    def __init__(self, data=None, mean = 0. , stddev=1.):
        """class constructor"""
        self.mean = float(mean)
        self.stddev = float(stddev)
        if stddev <= 0:
            raise ValueError("sttdev must be a positive value")
        if data is None:
            self.mean = mean
            self.stddev = stddev
        else:
            if not isinstance(data, list):
                raise TypeError("data must be a list")
            if len(data) < 2:
                raise ValueError("data must contain multiple values")   
            self.mean = sum(data) / len(data)
            self.stddev = (sum([(x - self.mean) ** 2 for x in data]) / len(data)) ** (1/2)

    def z_score(self, x):
        """calculates the z-score of a given x-value"""
        z = (x - self.mean) / self.stddev
        return z

    def x_value(self, z):
        """calculates the x-value of a given z-score"""
        x = (z * self.stddev) + self.mean
        return x

    def pdf(self, x):
        """calculates the value of the PDF for a given x-value"""
        pi = 3.1415926536
        e = 2.7182818285
        pdf = (1 / (self.stddev * math.sqrt(2 * pi))) * e**(-((x-self.mean)**2) / (2*(self.stddev**2)))
        return pdf
        
    def cdf(self, x):
        """calculates the value of the CDF for a given x-value"""
        erfx_value = ((x - self.mean) / (self.stddev * (2**(1/2))))
        cdf = (1/2) * (1 + self.calculate_erf(erfx_value))
        return cdf
         
    def calculate_erf(self,x):
        pi = 3.1415926536
        erfx = (2 / (pi**(1/2))) * (x - ((x**3) / 3) + ((x**5) / 10) - ((x**7) / 42) + ((x**9) / 216))
        return erfx
