import speed
'''
Objective:
find STD
'''
'''
Standard deviation is a number that describes how spread out the values are.

A low standard deviation means that most of the numbers are close to the mean (average) value.

A high standard deviation means that the values are spread out over a wider range.
'''
import numpy

mystd=numpy.std(speed.speed())

print(f'std is : {mystd}')

'''
Variance
Variance is another number that indicates how spread out the values are.

In fact, if you take the square root of the variance, you get the standard deviation!

Or the other way around, if you multiply the standard deviation by itself, you get the variance!

To calculate the variance you have to do as follows:
'''

my_variance=numpy.var(speed.speed())
#import math to find sqrt
import math

print(f'Variance is : {round(my_variance, 2)}------we can get std which is sqrt of Var: {math.sqrt(my_variance)}')

'''good work 
NB
Symbols
Standard Deviation is often represented by the symbol Sigma: σ

Variance is often represented by the symbol Sigma Squared: σ2'''

print("good work--- remember---")
p=["Symbols: \n Standard Deviation is often represented by the symbol Sigma: σ \nVariance is often represented by the symbol Sigma Squared: σ2"]
print(p)