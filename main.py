import store
import products

# setup initial stock of inventory
product_list = [products.Product("MacBook Air M2", price=1450, quantity=100),
                products.Product("Bose QuietComfort Earbuds", price=250, quantity=500),
                products.Product("Google Pixel 7", price=500, quantity=250)
                ]
best_buy = store.Store(product_list)


def show_menu():
    print("""
        Store Menu
        ----------
1. List all products in store
2. Show total amount in store
3. Make an order
4. Quit
        """)


def make_order(store_obj):
    shopping_list = []
    products = store_obj.get_all_products()
    print_products(products)
    print("When you want to finish order, enter empty text.")
    while True:
        item = input("Which product # do you want? ")
        quantity = input("Which amount do you want? ")
        if item == "" and quantity == "":
            if not shopping_list:
                break
            try:
                print("\n********")
                print(f"Order made! Total payment: ${store_obj.order(shopping_list)}")
                break
            except EnvironmentError:
                print("Error while making order! Quantity larger than what exists")
                break
        else:
            if not int(item) or not int(quantity):
                print("\nError adding product!")
                continue
            shopping_list.append((products[int(item) - 1], int(quantity)))
            print("\nProduct added to list!\n")


def print_products(products):
    print("------")
    for i, product in enumerate(products):
        print(f"{i + 1}. {product.show()}")
    print("------")


def start(store_obj: store.Store):
    while True:
        show_menu()
        try:
            user_choice = int(input("Enter your choice (1-4): "))
            if user_choice not in range(1, 5):
                continue
            else:
                if user_choice == 1:
                    print("\nFull products list:")
                    print_products(store_obj.get_all_products())
                elif user_choice == 2:
                    print(f"\nTotal of {store_obj.get_total_quantity()} items in store")
                elif user_choice == 3:
                    make_order(store_obj)
                else:
                    break
                input("\nPress enter to continue...")
        except ValueError:
            print("\nError with your choice! Try again!")


if __name__ == '__main__':
    start(best_buy)
