from itertools import product

from classes.product import Product
from classes.store import Store

def main():
    """
    Main function which sets up default inventory and calls the start() function with given instance of Store
    """
    # setup initial stock of inventory
    product_list = [Product("MacBook Air M2", price=1450, quantity=100),
                    Product("Bose QuietComfort Earbuds", price=250, quantity=500),
                    Product("Google Pixel 7", price=500, quantity=250)
                    ]
    best_buy = Store(product_list)
    start(best_buy)


def start(store: Store) -> None:
    """
    starts the Interface for User to navigate through our Shop.
    """
    func_dict = {
        "1": {
            "function": list_all_products,
            "description": "List all products in store"
        },
        "2": {
            "function": show_total_amount,
            "description": "Show total amount in store"
        },
        "3": {
            "function": make_order,
            "description": "Make an order"
        },
        "4": {
            "function": exit,
            "description": "Quit"
        }
    }

    store_menu = "\n".join(
        f"{key}. {value['description']}" for key, value in func_dict.items()
    )

    print(f"----- Welcome to the store! -----")
    while True:
        print("\n----- Available options -----")
        print(store_menu)
        user_choice = input(f"Please choose an option (1 - {len(func_dict)}): ")
        if user_choice == "4":
            print("\nThanks for visiting us!")
            func_dict[user_choice]["function"]()
        elif user_choice in func_dict:
            func_dict[user_choice]["function"](store)
        else:
            continue
        input("Press enter to continue")


def list_all_products(store: Store) -> None:
    """
    Prints out all currently available Products.
    """
    products = store.get_all_products()
    print("*" * 10)
    if products:
        for i, product in enumerate(products):
            print(f"{i + 1}. {product.show()}")
    else:
        print("We are out of Stock! :(")
    print("*" * 10)


def show_total_amount(store) -> None:
    """
    Prints out the total amount of items in the store.
    """
    print(f"\nWe currently got {store.get_total_quantity()} items in our store!\n")


def make_order(store) -> None:
    """
    Makes an order and prints information
    """
    products = store.get_all_products()
    shopping_cart = []

    list_all_products(store)
    print("Enter empty text to finish shopping!\n")

    while True:
        index, quantity = ask_for_item_and_quantity(len(products))
        if index is None or quantity is None:
            break
        shopping_cart.append((products[index], quantity))
        print(f"{products[index].name} ({quantity}) successfully added to cart.")

    print_shopping_cart(shopping_cart)
    try:
        price = store.order(shopping_cart)
        print(f"Thanks for your order! Total amount to pay: ${price}")
    except Exception as e:
        print(f"Error, something went wrong! {e}")


def print_shopping_cart(shopping_cart: list[tuple]) -> None:
    """
    Takes a shopping cart list and serializes it to a string and prints it.
    """
    serialized_shopping_cart = "\n".join(
        f"{i + 1}. {product.name}, Price: {product.price}, Quantity: {quantity}"
        for i, (product, quantity) in enumerate(shopping_cart)
    )
    serialized_shopping_cart = serialized_shopping_cart or "Empty"
    print(f"\nYour Cart:\n{serialized_shopping_cart}\n")


def ask_for_item_and_quantity(store_items_amount: int) -> tuple:
    """
    Calls another function to verify user input and returns a index and quantity as a tuple of integers
    """
    while True:
        index = string_to_int("Which product # do you want? ")
        if index is None:
            break
        if 1 <= index <= store_items_amount:
            index -= 1
            break

    if index is None:
        return None, None

    while True:
        quantity = string_to_int("How many do you want to buy? ")
        if quantity is not None and quantity >= 0:
            break
        print("Amount has to be positive or zero")

    return index, quantity


def string_to_int(prompt: str) -> int:
    """
    asks User for a number and tries to convert it to an integer.
    """
    while True:
        user_input = input(prompt)
        if not user_input:
            return None
        try:
            return int(user_input)
        except ValueError:
            print("Please enter a number.")


if __name__ == "__main__":
    main()