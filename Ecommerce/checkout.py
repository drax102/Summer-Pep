def process_checkout(cart, discount_percent=0, tax_percent=0):
    subtotal = cart.get_subtotal()
    discount_amount = subtotal * (discount_percent / 100)
    taxable_amount = subtotal - discount_amount
    tax_amount = taxable_amount * (tax_percent / 100)
    grand_total = taxable_amount + tax_amount

    print("=== ORDER SUMMARY ===")
    for item in cart.items:
        prod = item["product"]
        qty = item["quantity"]
        print(f"{prod['name']} x{qty} - ${prod['price'] * qty:.2f}")

    print("-" * 25)
    print(f"Subtotal:     ${subtotal:.2f}")
    print(f"Discount:    -${discount_amount:.2f}")
    print(f"Tax:         +${tax_amount:.2f}")
    print("-" * 25)
    print(f"Total:        ${grand_total:.2f}")
    print("=====================")
