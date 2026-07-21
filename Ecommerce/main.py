import product
import cart
import checkout

p1 = product.create_product("Wireless Headphones", 50.00)
p2 = product.create_product("Phone Case", 15.00)
p3 = product.create_product("USB-C Cable", 10.00)

my_cart = cart.Cart()
my_cart.add_product(p1, quantity=1)
my_cart.add_product(p2, quantity=2)
my_cart.add_product(p3, quantity=3)

checkout.process_checkout(my_cart, discount_percent=10, tax_percent=5)
