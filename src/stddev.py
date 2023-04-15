#!/usr/bin/env python3
import cProfile
import pstats
from ivsmath import division
from ivsmath import power
from ivsmath import radical
import sys

def convert_string():
    global numbers
    data = sys.stdin.read().split()
    numbers = [float(i) for i in data]

def arithmetic_mean():
    global arithmeticmean
    sum = 0
    global count
    count = 0
    for num in numbers:
        sum += num
        count += 1
    if count == 0:
        print("Empty input.")
        sys.exit()
    arithmeticmean = division(count, sum)

def variance():
    global variance
    N = count
    numerator = 0
    for num in numbers:
        numerator += power(2, num) - power(2,arithmeticmean)
    denominator = N - 1
    if denominator == 0:
        print("Enter at least 2 numbers.")
        sys.exit()
    variance = division(denominator, numerator)

def standard_deviation():
    stddv= radical(variance, 2)
    print(stddv)


if __name__ == "__main__":
    convert_string()
    arithmetic_mean()
    variance()
    standard_deviation()


