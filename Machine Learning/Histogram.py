'''
use the Python module Matplotlib to draw a histogram.
'''
import numpy
import matplotlib.pyplot as plt
#import speed
#generate random number between 0 and 5
nums = numpy.random.uniform(0.0, 5.0, 250)

plt.hist(nums, 10)
plt.show()