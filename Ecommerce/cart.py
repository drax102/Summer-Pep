class Cart:
    def __init__(self):
        self.items = []

    def add_product(self, product, quantity=1):
        self.items.append({"product": product, "quantity": quantity})

    def get_subtotal(self):
        return sum(item["product"]["price"] * item["quantity"] for item in self.items)
