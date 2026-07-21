# advanced.py

def power(base, exponent):
    return base ** exponent

def square_root(number):
    if number < 0:
        raise ValueError("Cannot compute square root of a negative number.")
    return number ** 0.5