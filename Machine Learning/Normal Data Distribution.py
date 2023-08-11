import numpy
import matplotlib.pyplot as plt
#normal data distribution 
x = numpy.random.normal(5.0, 1.0, 10000000)

plt.hist(x, 100)
plt.show()