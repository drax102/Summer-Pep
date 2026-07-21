# main.py

import calculator
import tax
import invoice


items = []

print("=" * 40)
print("WELCOME TO PYTHON BILLING SYSTEM")
print("=" * 40)

customer = input("Enter Customer Name: ")

while True:

    name = input("\nItem Name : ")

    price = float(input("Price : "))

    quantity = int(input("Quantity : "))

    items.append((name, price, quantity))

    choice = input("\nAdd another item? (y/n): ").lower()

    if choice != 'y':
        break


subtotal = calculator.calculate_total(items)

gst = tax.calculate_tax(subtotal)

grand_total = subtotal + gst

invoice.print_invoice(
    customer,
    items,
    subtotal,
    gst,
    grand_total
)