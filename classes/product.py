class Product:
    def __init__(self, name: str, price: float, quantity: int) -> None:
        # Check valid inputs
        if not isinstance(name, str):
            raise TypeError(f"name must be string, got {type(name).__name__}.")
        if not name.strip():
            raise ValueError(f"Doesn't accept empty string.")
        if not isinstance(price, (float, int)):
            raise TypeError(f"price must be either float or integer, got {type(price).__name__}.")
        if price < 0:
            raise ValueError(f"Only positive numbers are accepted for price.")
        if not isinstance(quantity, int):
            raise TypeError(f"quantity must be integer, got {type(quantity).__name__}.")
        if quantity < 0:
            raise ValueError(f"Only positive numbers are accepted for quantity")

        # initialize instance variables
        self.name = name
        self.price = price
        self.quantity = quantity
        self.active = True

    def get_quantity(self) -> float:
        """
        Returns the current available quantity
        """
        return self.quantity

    def set_quantity(self, quantity: int) -> None:
        """
        sets instance variable self.quantity equal to quantity
        """
        if not isinstance(quantity, int):
            raise TypeError(f"quantity must be integer, got {type(quantity).__name__}.")
        if quantity < 0:
            raise ValueError(f"Only positive numbers are accepted for quantity")

        self.quantity = quantity
        if quantity == 0:
            self.deactivate()


    def is_active(self) -> bool:
        """
        returns True if product is active or False if product is not.
        """
        return self.active

    def activate(self) -> None:
        """
        Activates the product
        """
        self.active = True

    def deactivate(self) -> None:
        """
        deactivates the Product
        """
        self.active = False

    def show(self) -> str:
        """
        Returns a string, which describes the product.
        :return: f-string which holds product information
        """
        return f"{self.name}, Price: {self.price}, Stock: {self.quantity}"

    def buy(self, quantity: int) -> float:
        """
        Buys a given quantity of the product, returns the total price and updates the current stock.
        Also raises exceptions if something does not work.
        :param quantity: The amount of products to buy (Integer)
        :return: Total price (self.price * quantity) as float
        """
        if not isinstance(quantity, int):
            raise TypeError(f"quantity must be integer, got {type(quantity).__name__}.")
        if quantity < 0:
            raise ValueError(f"Only positive numbers are accepted for quantity")
        if not self.active:
            raise TypeError(f"Product {self.name} is not currently active.")
        if quantity > self.quantity:
            raise ValueError(f"Can't buy {quantity} items, current stock only holds: {self.quantity} items.")

        total_price = quantity * self.price
        self.set_quantity(self.quantity - quantity)
        return total_price
