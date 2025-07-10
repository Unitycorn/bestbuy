class Product:
    def __init__(self, name: str, price: float, quantity: int):
        if name == "" or not isinstance(name, str):
            raise ValueError(f"Inappropriate product name: {name}")
        else:
            self.name = name
        if price < 0 or not isinstance(price, float):
            raise ValueError(f"Inappropriate price value: {price}")
        else:
            self.price = price
        if quantity < 0 or not isinstance(quantity, int):
            raise ValueError(f"Inappropriate quantity value: {quantity}")
        else:
            self.quantity = quantity
        self.active = True

    def get_quantity(self) -> int:
        return self.quantity

    def set_quantity(self, quantity):
        self.quantity += quantity
        if self.quantity <= 0:
            self.deactivate()

    def is_active(self) -> bool:
        return self.active

    def activate(self):
        self.active = True

    def deactivate(self):
        self.active = False

    def show(self):
        print(f"{self.name}, Price: {self.price}, Quantity: {self.quantity}")

    def buy(self, quantity) -> float:
        if self.quantity - quantity < 0:
            raise ValueError("Quantity outcome is negative")
        else:
            if self.quantity - quantity == 0:
                self.deactivate()
            self.quantity -= quantity
        return float(self.price * quantity)
