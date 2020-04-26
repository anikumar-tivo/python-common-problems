__doc__ = 'Problem statement:\
    1. How to print the first N fibonacci numbers?\
    2. Check the given number is a fibonacci number.'
__author__ = 'Anil Kumar'
__email__ = 'anilkumar.jan28@gmail.com'
__version__ = '1.0'
__date__ = 'Apr 26, 2020'


def fibonacci_series(number):
    if (number < 2):
        raise Exception("Input cannot be less than 2.")
    series = [1, 1]
    i = 2
    while (i < number):
        fib_i = series[i - 2] + series[i-1]
        series.append(fib_i)
        i += 1
    return series


def is_fibonacci(number):
    if (number == 1):
        return True
    penultimate = 1
    antepenultimate = 1
    while True:
        fibonacci = penultimate + antepenultimate
        if(number == fibonacci):
            return True
        if (fibonacci > number):
            return False
        penultimate = antepenultimate
        antepenultimate = fibonacci
    

if __name__ == "__main__":
    series = fibonacci_series(10)
    for num in series:
        print num,
    print
    print "is_fibonacci(series[-1])?", is_fibonacci(series[-1])
    print "is_fibonacci(100)?", is_fibonacci(100)
    print
