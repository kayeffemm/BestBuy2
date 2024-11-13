from classes.product import Product, NonStockedProduct, LimitedProduct


class Store:
    def __init__(self, products: list[Product]) -> None:
        if not isinstance(products, list):
            raise TypeError(f"Expected a list, got {type(products).__name__}.")
        if not all(isinstance(product, Product) for product in products):
            raise TypeError(f"Not every item in list is instance of Product.")

        # initialize products list as instance variable
        self.products = []
        for product in products:
            self.products.append(product)

    def add_product(self, product: Product) -> None:
        """
        Adds a product to our Store
        """
        if not isinstance(product, Product):
            raise TypeError(f"Expected a product to be instance of Product, got {type(product).__name__}.")

        self.products.append(product)

    def remove_product(self, product: Product) -> None:
        """
        Removes a product from our Store
        """
        if not isinstance(product, Product):
            raise TypeError(f"Expected a product to be instance of Product, got {type(product).__name__}.")
        if product not in self.products:
            raise ValueError(f"{product.name} is not in the store.")

        self.products.remove(product)

    def get_total_quantity(self) -> int:
        """
        Returns how many individual items the store currently has in stock.
        """
        return sum(product.quantity for product in self.products)

    def get_all_products(self) -> list[Product]:
        """
        Returns a list with all currently active products.
        """
        return [product for product in self.products if product.is_active()]

    def order(self, shopping_list: list[tuple[Product, int]]) -> float:
        """
        Gets a list of tuples, where each tuple has 2 items:
        Product (Product class) and quantity (int).
        Buys the products and returns the total price of the order.
        """
        if not isinstance(shopping_list, list):
            raise TypeError(f"Expected a list, got {type(shopping_list).__name__}.")
        for product, quantity in shopping_list:
            if not isinstance(product, Product):
                raise TypeError(f"Expected instance of Product class, got {type(product).__name__}.")
            if not product.is_active():
                raise ValueError(f"{product.name} is currently inactive.")
            if type(product) == Product and quantity > product.quantity:
                raise ValueError(f"Order quantity exceed store stock for product: {product.name}.")

        total_price = 0
        for product, quantity in shopping_list:
            total_price += product.buy(quantity)
        return total_price

