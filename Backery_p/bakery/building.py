

from bakery.items import available_items

class Bakery:
    def __init__(self):
        self.cart = []

    def show_items(self):
        print("\nAvailable Items:")
        for index, item in enumerate(available_items):
            print(f"{index + 1}. {item.name} - ₹{item.price}")

    def add_to_cart(self, choice):
        if 1 <= choice <= len(available_items):
            item = available_items[choice - 1]
            self.cart.append(item)
            print(f"{item.name} added to cart!")
        else:
            print("Invalid choice!")

    def show_cart(self):
        if not self.cart:
            print("\nCart is empty.")
            return

        print("\nItems in Cart:")
        total = 0
        for item in self.cart:
            print(f"{item.name} - ₹{item.price}")
            total += item.price

        print(f"\nTotal Amount: ₹{total}")
