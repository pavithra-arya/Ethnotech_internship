# main.py

from bakery.building import Bakery

def main():
    shop = Bakery()

    while True:
        print("\n--- Welcome to Bakery ---")
        print("1. Show Items")
        print("2. Add Item to Cart")
        print("3. Show Cart")
        print("4. Exit")

        choice = int(input("Enter your choice: "))

        if choice == 1:
            shop.show_items()

        elif choice == 2:
            shop.show_items()
            item_choice = int(input("Select item number: "))
            shop.add_to_cart(item_choice)

        elif choice == 3:
            shop.show_cart()

        elif choice == 4:
            print("Thank you for visiting!")
            break

        else:
            print("Invalid choice!")

if __name__ == "__main__":
    main()
