# --- IMPORTS & EXPLANATIONS ---

# os: Bridges Python to your operating system (Windows/Mac/Linux).
import os

# json: Translates Python dictionaries to standard JSON text strings (universal web data format).
import json

# csv: The standard format for basic spreadsheets. Lets you read/write CSV files.
import csv

# math: Your scientific calculator (gives you access to constants like pi, exponents, etc.).
import math

# random: Generates unpredictability, letting you pick random items or generate random numbers.
import random

# pathlib: Handles file paths cleanly as objects, avoiding issues between Windows (\) and Mac/Linux (/) slashes.
from pathlib import Path

# datetime: Handles the messy math of dates, times, leap years, and time intervals.
from datetime import datetime, timedelta

# collections: Provides "upgraded" lists and dictionaries for specific, common jobs.
from collections import Counter, defaultdict


# --- 1. FILE & SYSTEM MANAGEMENT ---
print("--- 1. FILE & SYSTEM MANAGEMENT ---")

# os.getcwd() asks the computer, "What exact folder is this script running in right now?"
print(f"Current directory: {os.getcwd()}")

# Path() creates a virtual reference to a file. 
# We can easily write text to it and check if it successfully exists.
my_file = Path("hello.txt")
my_file.write_text("Hello, Python!")

if my_file.exists():
    print("hello.txt was created successfully!")


# --- 2. DATA FORMATS (JSON & CSV) ---
print("\n--- 2. DATA FORMATS (JSON & CSV) ---")

user_data = {'name': 'Alice', 'role': 'Admin'}
# json.dumps() converts the Python dictionary into a JSON string that any language can read.
json_str = json.dumps(user_data) 
print(f"JSON String: {json_str}")

# csv.writer() builds a mini-spreadsheet. We write headers (ID, Name) and then the rows.
with open('users.csv', mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['ID', 'Name'])
    writer.writerow([1, 'Alice'])
    writer.writerow([2, 'Bob'])
print("users.csv was created successfully!")


# --- 3. DATES AND TIMES ---
print("\n--- 3. DATES AND TIMES ---")

# datetime.now() grabs the exact current time.
now = datetime.now()
print(f"Right now: {now.strftime('%Y-%m-%d %H:%M:%S')}")

# timedelta(days=7) safely calculates exactly one week into the future.
next_week = now + timedelta(days=7)
print(f"Next week: {next_week.date()}")


# --- 4. MATH AND PROBABILITY ---
print("\n--- 4. MATH AND PROBABILITY ---")

# math.pi gives the exact constant. math.pow() raises the radius (5) to the power of 2.
area = math.pi * math.pow(5, 2)
print(f"Area of a circle (radius 5): {area:.2f}")

# random.choice() looks at a list and picks one item completely at random.
fruits = ['apple', 'banana', 'cherry']
print(f"Random fruit selection: {random.choice(fruits)}")


# --- 5. ADVANCED DATA STRUCTURES ---
print("\n--- 5. ADVANCED DATA STRUCTURES ---")

words = ['apple', 'banana', 'apple', 'cherry', 'apple']
# Counter automatically tallies up how many times each item appears in a list.
word_counts = Counter(words)
print(f"Apple count from list: {word_counts['apple']}") 

# defaultdict(int) creates a dictionary where new items automatically start with a value of 0.
# This prevents Python from crashing when we try to add 10 points to 'Alice' before she exists.
scores = defaultdict(int)
scores['Alice'] += 10 
print(f"Alice's default dictionary score: {scores['Alice']}")