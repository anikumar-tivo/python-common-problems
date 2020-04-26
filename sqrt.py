__doc__ = 'Problem statements:\
    1. I wanted to know how the square root function works in mathematics?\
    2. How to implement sqrt (square root) function in python?\
    3. Python program to compute the square root of a number.\
    4. Print square root value of numbers from 1 to 100'
__author__ = 'Anil Kumar'
__email__ = 'anilkumar.jan28@gmail.com'
__version = '1.0'
__date__ = 'Apr 26, 2020'


def sqrt(number):
    if (number == 1):
        return 1.0

    high = float(number)
    low = 0.0
    div = 2.0
    i = 0
    while i < 1024:
        i += 1
        mid = (low + high) / div
        tmp = (low + mid) * (low + mid)
        if tmp < number:
            low += mid
        elif tmp > number:
            high -= mid
        else:
            return low + mid

    return low
    
    
if __name__ == "__main__":
    # Square root value of number from 1 to 100
    number = 1
    while number <= 100:
        print "sqrt(%d) = %f" %(number, sqrt(number))
        number += 1
