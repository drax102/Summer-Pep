import calculator
import geometry
import math
import random
import statistics
from datetime import datetime, date
import os
import sys
import keyword

print("\n--- CALCULATOR TESTS ---")
print(calculator.add(10, 4))
print(calculator.subtract(10, 4))
print(calculator.multiply(10, 4))
print(calculator.divide(10, 4))
print(calculator.square(10))

print("\n--- GEOMETRY TESTS ---")
print(geometry.area_square(10))
print(geometry.area_rectangle(10, 5))
print(geometry.area_circle(10))

print("\n--- MATH TESTS ---")
print(math.sqrt(25))
print(math.factorial(5))
print(math.pi)
print(math.pow(5, 6))

print("\n--- RANDOM TESTS ---")
print(random.randint(1, 10))

for i in range(5):
    print(random.randint(1, 10))

print(random.choice(['Python', 'Sql', 'BI']))

print("\n--- DATETIME TESTS ---")
today = datetime.now()
print(today)
print(date.today())
print(today.time())

print("\n--- STATISTICS TESTS ---")
marks = [75, 80, 98, 35, 29]
print(statistics.mean(marks))
print(statistics.median(marks))

print("\n--- SYSTEM & OS TESTS ---")
# print(keyword.kwlist) # Hidden to keep output clean, but it works!
print(f"Is 'for' a keyword? {keyword.iskeyword('for')}")
print(f"Current Directory: {os.getcwd()}")
print(f"Python Version: {sys.version.split()[0]}")
print(f"Platform: {sys.platform}")