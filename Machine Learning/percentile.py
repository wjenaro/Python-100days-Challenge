import numpy
import speed
x = numpy.percentile(speed.speed(), 10)

print(f' out of the speeds provided, 10%  have a speed of {x} and below')
'''

Percentiles are used in statistics to give you a number that describes the value that a given percent of the values are lower than.'''