# main.py

# Importing everything through the clean __init__.py setup we made
from calculator import add, divide, power, celsius_to_fahrenheit

print("=== Custom Calculator Package Test ===")

# 1. Testing Arithmetic Operations
try:
    print(f"Addition (10 + 5)       : {add(10, 5)}")
    print(f"Division (20 / 4)       : {divide(20, 4)}")
except ZeroDivisionError as e:
    print(e)

# 2. Testing Advanced Operations
print(f"Power (2 raised to 5)   : {power(2, 5)}")

# 3. Testing Conversion Operations
print(f"Temperature (37°C to F) : {celsius_to_fahrenheit(37)}°F")