import numpy as np
import math
#!/usr/bin/env python3
""" defines Normal class that represents normal distribution """

class Normal:
    """class that represents normal distribution"""


    def __init__(self, data=None, mean = 0. , stddev=1.):
        """class constructor"""
        # write your code here
        
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
#             self.stddev = math.sqrt(sum([(x - self.mean) ** 2 for x in data]) / len(data)-1)
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
        
        


np.random.seed(0)
data = np.random.normal(70, 10, 100).tolist()
n1 = Normal(data)
print('Mean:', n1.mean, ', Stddev:', n1.stddev)

n2 = Normal(mean=70, stddev=10)
print('Mean:', n2.mean, ', Stddev:', n2.stddev)


print()

np.random.seed(0)
data = np.random.normal(70, 10, 100).tolist()
n1 = Normal(data)
print('Z(90):', n1.z_score(90))
print('X(2):', n1.x_value(2))

n2 = Normal(mean=70, stddev=10)
print()
print('Z(90):', n2.z_score(90))
print('X(2):', n2.x_value(2))


print()

np.random.seed(0)
data = np.random.normal(70, 10, 100).tolist()
n1 = Normal(data)
print('PSI(90):', n1.pdf(90))

n2 = Normal(mean=70, stddev=10)
print('PSI(90):', n2.pdf(90))

print()
np.random.seed(0)
data = np.random.normal(70, 10, 100).tolist()
n1 = Normal(data)
print('PHI(90):', n1.cdf(90))

n2 = Normal(mean=70, stddev=10)
print('PHI(90):', n2.cdf(90))
