# bakery/items.py

class Item:
    def __init__(self, name, price):
        self.name = name
        self.price = price


# Available bakery items
available_items = [
    Item("Cake", 500),
    Item("Bread", 40),
    Item("Cookies", 150),
    Item("Puffs", 35),
    Item("Donut", 60)
]
