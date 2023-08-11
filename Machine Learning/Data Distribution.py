'''
How Can we Get Big Data Sets?
To create big data sets for testing, we use the Python module NumPy, which comes with a number of methods to create random data sets, of any size.'''


import numpy

x = numpy.random.uniform(0.0, 1.0, 250)
m=numpy.mean(x)

print(x)
print(m)