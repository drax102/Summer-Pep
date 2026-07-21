import calculator
import discount
import tax

def print_invoice(item_price, item_quantity, discount_percent, tax_percent):
    subtotal = calculator.calculate_total(item_price, item_quantity)
    after_discount = discount.get_discounted_price(subtotal, discount_percent)
    tax_amount = tax.get_tax_amount(after_discount, tax_percent)
    grand_total = after_discount + tax_amount

    print("--- INVOICE ---")
    print("Subtotal:", subtotal)
    print("After Discount:", after_discount)
    print("Tax Amount:", tax_amount)
    print("Total Bill:", grand_total)

print_invoice(100, 2, 10, 5)