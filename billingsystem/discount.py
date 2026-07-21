import calculator

def get_discounted_price(price, discount_rate):
    discount_amount = calculator.calculate_discount(price, discount_rate)
    return price - discount_amount