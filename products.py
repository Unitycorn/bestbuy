class Product:
    """Represents a product"""
    def __init__(self, name: str, price: float, quantity: int):
        if name == "" or not isinstance(name, str):
            raise ValueError(f"Inappropriate product name: {name}")
        self.name = name
        if price < 0:
            raise ValueError(f"Inappropriate price value: {price}")
        self.price = price
        if quantity < 0 or not isinstance(quantity, int):
            raise ValueError(f"Inappropriate quantity value: {quantity}")
        self.quantity = quantity
        if self.quantity <= 0:
            self.active = False
        else:
            self.active = True

    def get_quantity(self) -> int:
        """Getter for quantity"""
        return self.quantity

    def set_quantity(self, quantity):
        """Setter for quantity"""
        self.quantity += quantity
        if self.quantity <= 0:
            self.deactivate()

    def is_active(self) -> bool:
        """Check if item is available"""
        return self.active

    def activate(self):
        """Activates an item"""
        self.active = True

    def deactivate(self):
        """Deactivates an item"""
        self.active = False

    def show(self):
        """Return string representation if item is available"""
        if self.active:
            return f"{self.name}, Price: ${self.price}, Quantity: {self.quantity}"
        return None

    def buy(self, quantity) -> float:
        """Decreases quantity and returns the total price"""
        if self.quantity - quantity < 0:
            raise EnvironmentError("Quantity outcome is negative")
        if self.quantity - quantity == 0:
            self.deactivate()
        self.quantity -= quantity
        return float(self.price * quantity)
