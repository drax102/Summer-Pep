# invoice.py

from datetime import datetime


def print_invoice(customer, items, subtotal, tax, total):
    print("\n")
    print("=" * 50)
    print("            BILLING SYSTEM")
    print("=" * 50)

    print("Customer :", customer)
    print("Date     :", datetime.now().strftime("%d-%m-%Y %H:%M:%S"))

    print("-" * 50)
    print("{:<20}{:<10}{:<10}{:<10}".format(
        "Item", "Price", "Qty", "Total"))
    print("-" * 50)

    for name, price, qty in items:
        print("{:<20}{:<10}{:<10}{:<10}".format(
            name,
            price,
            qty,
            price * qty
        ))

    print("-" * 50)
    print(f"Subtotal : ₹{subtotal:.2f}")
    print(f"GST (18%): ₹{tax:.2f}")
    print(f"Grand Total : ₹{total:.2f}")
    print("=" * 50)
    print("Thank You! Visit Again.")
    print("=" * 50)