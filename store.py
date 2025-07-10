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
