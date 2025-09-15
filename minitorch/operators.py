"""Collection of the core mathematical operators used throughout the code base."""

import math

# ## Task 0.1
from typing import Callable, Iterable
# from functools import reduce
# Callable means func, iteratable means data str like list, dict, str etc.

#
# Implementation of a prelude of elementary functions.

# Mathematical functions:
# - mul
# - id
# - add
# - neg
# - lt
# - eq
# - max
# - is_close
# - sigmoid
# - relu
# - log
# - exp
# - log_back
# - inv
# - inv_back
# - relu_back
#
# For sigmoid calculate as:
# $f(x) =  \frac{1.0}{(1.0 + e^{-x})}$ if x >=0 else $\frac{e^x}{(1.0 + e^{x})}$
# For is_close:
# $f(x) = |x - y| < 1e-2$


# TODO: Implem“ent for Task 0.1.
def mul(num_1: float, num_2: float) -> float:
    return num_1 * num_2

def id(num): # type: ignore
    return num

def add(num_1, num_2): # type: ignore
    return num_1+num_2

def neg(num): # type: ignore
    return (-1)*num

def lt(num_1, num_2) -> bool: # type: ignore
    return num_1 < num_2

def eq(num_1, num_2) -> bool: # type: ignore
    return num_1 == num_2

def max(num_1, num_2): # type: ignore
    if num_1 >= num_2:
        return num_1
    else:
        return num_2

def is_close(num_1, num_2) -> bool: # type: ignore
    return abs(num_1-num_2) < 1e-2
        
def sigmoid(x): # type: ignore
    if x >= 0:
        z = math.exp(-x)
        return 1.0 / (1.0 + z)          # 1/(1+e^-x)
    else:
        z = math.exp(x)
        return z / (1.0 + z)            # e^x/(1+e^x)

def relu(x): # type: ignore
    if x >= 0:
        return x
    else:
        return 0

def log(x): # type: ignore
    return math.log(x, math.e)

def exp(x): # type: ignore
    return math.exp(x)

def inv(x): # type: ignore
    if x == 0:
        raise ValueError("Reciprocal of zero is undefined.")
    return 1.0 / x

def log_back(x, upstream): # type: ignore
    if x <= 0:
        raise ValueError("Input must be positive!")
    return upstream / x

def inv_back(x, upstream): # type: ignore
    if x == 0:
        raise ValueError("Reciprocal of zero is undefined.")
    return - upstream / (x*x)

def relu_back(x, upstream): # type: ignore
    return upstream * (x > 0)

# ## Task 0.3

# Small practice library of elementary higher-order functions.

# Implement the following core functions
# - map
# - zipWith
# - reduce
#
# Use these to implement
# - negList : negate a list
# - addLists : add two lists together
# - sum: sum lists
# - prod: take the product of lists


# TODO: Implement for Task 0.3.

def map(fn, input): # type: ignore
    return [fn(x) for x in input]

def zipWith(fn, input_1, input_2): # type: ignore
    return [fn(x, y) for x, y in zip(input_1, input_2)]

def reduce(fn, input, init): # type: ignore
    output = init
    for x in input:
        output = fn(output, x)
    return output
        
        

def negList(input: Iterable) -> Iterable: # type: ignore
    # map is lazy iterator
    return map(neg, input)

def addLists(input_1: Iterable, input_2: Iterable) -> Iterable: # type: ignore
    return zipWith(add, input_1, input_2)

def sum(input_1): # type: ignore
    return reduce(add, input_1, 0)

def prod(input_1): # type: ignore
    return reduce(mul, input_1, 1)