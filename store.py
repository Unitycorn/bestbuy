import products


class Store:
    def __init__(self, product_list):
        if product_list is None:
            self.product_list = []
        else:
            self.product_list = product_list

    def add_product(self, product):
        self.product_list.append(product)

    def remove_product(self, product):
        self.product_list.remove(product)

    def get_total_quantity(self) -> int:
        total_quantity = 0
        for product in self.product_list:
            total_quantity += product.quantity
        return total_quantity

    def get_all_products(self) -> list[products.Product]:
        return [product for product in self.product_list if product.is_active()]

    def order(self, shopping_list) -> float:
        price = 0
        for product, quantity in shopping_list:
            price += product.buy(quantity)
        return price


"""
product_list = [products.Product("MacBook Air M2", price=1450, quantity=100),
                products.Product("Bose QuietComfort Earbuds", price=250, quantity=500),
                products.Product("Google Pixel 7", price=500, quantity=250),
                ]

best_buy = Store(product_list)
products = best_buy.get_all_products()
print(best_buy.get_total_quantity())
print(best_buy.order([(products[0], 1), (products[1], 2)]))
for product in products:
    product.show()
"""
