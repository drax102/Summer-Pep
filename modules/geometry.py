import math

def area_square(s):
    return s * s

def area_rectangle(l, b):
    # Fixed: Returns l * b instead of the perimeter formula
    return l * b

def area_circle(r):
    # Fixed: Uses math.pi instead of a hardcoded number
    return math.pi * r * r