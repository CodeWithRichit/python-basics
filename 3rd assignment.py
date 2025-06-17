#Task1:Calculate factorial using a function
def factorial(x):
    if x<2:
        return 1
    else:
        return x*factorial(x-1)
Num=int(input("Enter the number: "))
result=factorial(Num)
print("The factorial is: ",result)
#Task2:Using the math module for calculation
import math
a=int(input("Give me a number: "))
from math import sqrt
print("Square root: ",sqrt(a))
from math import log
print("logarithm of the number: ",log(a))
from math import sin
print("Sine of the number: ",sin(a))

