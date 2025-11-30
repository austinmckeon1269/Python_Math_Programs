# -----------------------------------------------------------
# ItemToPurchase Class
# -----------------------------------------------------------

class ItemToPurchase:
    def __init__(self, item_name="none", item_description="none",
                 item_price=0.0, item_quantity=0):
        self.item_name = item_name
        self.item_description = item_description
        self.item_price = item_price
        self.item_quantity = item_quantity

    def print_item_cost(self):
        total = self.item_price * self.item_quantity
        print(f"{self.item_name} {self.item_quantity} @ ${self.item_price} = ${total}")

    def print_item_description(self):
        print(f"{self.item_name}: {self.item_description}")


# -----------------------------------------------------------
# ShoppingCart Class
# -----------------------------------------------------------

class ShoppingCart:
    def __init__(self, customer_name="none", current_date="January 1, 2020"):
        self.customer_name = customer_name
        self.current_date = current_date
        self.cart_items = []

    def add_item(self, item):
        self.cart_items.append(item)

    def remove_item(self, item_name):
        found = False
        for i, item in enumerate(self.cart_items):
            if item.item_name == item_name:
                found = True
                del self.cart_items[i]
                break
        if not found:
            print("Item not found in cart. Nothing removed.")

    def modify_item(self, item_to_modify):
        found = False
        for item in self.cart_items:
            if item.item_name == item_to_modify.item_name:
                found = True
                if item_to_modify.item_description != "none":
                    item.item_description = item_to_modify.item_description
                if item_to_modify.item_price != 0:
                    item.item_price = item_to_modify.item_price
                if item_to_modify.item_quantity != 0:
                    item.item_quantity = item_to_modify.item_quantity
                break
        if not found:
            print("Item not found in cart. Nothing modified.")

    def get_num_items_in_cart(self):
        total_quantity = 0
        for item in self.cart_items:
            total_quantity += item.item_quantity
        return total_quantity

    def get_cost_of_cart(self):
        total = 0
        for item in self.cart_items:
            total += item.item_price * item.item_quantity
        return total

    def print_total(self):
        print(f"{self.customer_name}'s Shopping Cart - {self.current_date}")
        if len(self.cart_items) == 0:
            print("SHOPPING CART IS EMPTY")
            return

        print(f"Number of Items: {self.get_num_items_in_cart()}")
        for item in self.cart_items:
            item.print_item_cost()

        print(f"Total: ${self.get_cost_of_cart()}")

    def print_descriptions(self):
        print(f"{self.customer_name}'s Shopping Cart - {self.current_date}")
        print("Item Descriptions")
        for item in self.cart_items:
            item.print_item_description()


# -----------------------------------------------------------
# print_menu Function
# -----------------------------------------------------------

def print_menu(cart):
    option = ""

    while option != "q":
        print("\nMENU")
        print("a - Add item to cart")
        print("r - Remove item from cart")
        print("c - Change item quantity")
        print("i - Output items' descriptions")
        print("o - Output shopping cart")
        print("q - Quit")
        option = input("Choose an option:\n").strip().lower()

        if option == "a":
            print("\nADD ITEM TO CART")
            name = input("Enter the item name:\n")
            desc = input("Enter the item description:\n")
            price = float(input("Enter the item price:\n"))
            qty = int(input("Enter the item quantity:\n"))
            new_item = ItemToPurchase(name, desc, price, qty)
            cart.add_item(new_item)

        elif option == "r":
            print("\nREMOVE ITEM FROM CART")
            name = input("Enter name of item to remove:\n")
            cart.remove_item(name)

        elif option == "c":
            print("\nCHANGE ITEM QUANTITY")
            name = input("Enter the item name:\n")
            qty = int(input("Enter the new quantity:\n"))
            modified_item = ItemToPurchase(name, item_quantity=qty)
            cart.modify_item(modified_item)

        elif option == "i":
            print("\nOUTPUT ITEMS' DESCRIPTIONS")
            cart.print_descriptions()

        elif option == "o":
            print("\nOUTPUT SHOPPING CART")
            cart.print_total()

        elif option == "q":
            break

        else:
            print("Invalid option, please try again.")


# -----------------------------------------------------------
# Main Program
# -----------------------------------------------------------

if __name__ == "__main__":
    print("Enter customer's name:")
    customer_name = input()
    print("Enter today's date:")
    current_date = input()

    print(f"\nCustomer name: {customer_name}")
    print(f"Today's date: {current_date}")

    cart = ShoppingCart(customer_name, current_date)
    print_menu(cart)