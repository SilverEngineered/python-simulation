import numpy as np


def generate(distn):
    uniform = np.random.uniform()
    if distn is "uniform":
        return uniform
    if distn is "exponential":
        return generate_exponential()


def generate_exponential():
    return np.random.exponential()


def generate_gaussian(median, sdev):
    return np.random.normal(loc=median, scale=sdev)
