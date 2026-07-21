# calculator.py

def calculate_total(items):
    """
    items = [(name, price, quantity), ...]
    """
    subtotal = 0

    for item in items:
        subtotal += item[1] * item[2]

    return subtotal