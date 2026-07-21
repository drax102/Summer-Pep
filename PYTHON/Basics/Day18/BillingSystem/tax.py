# tax.py

GST_RATE = 0.18


def calculate_tax(amount):
    return amount * GST_RATE


def final_amount(amount):
    tax = calculate_tax(amount)
    return amount + tax