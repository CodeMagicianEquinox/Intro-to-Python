from catalog import catalog

cart = []

def print_header(text):
    print("\n\n\n")
    print(text)
    print("--------------------")

def print_menu():
    print("Menu")
    print("1.- View Catalog")
    print("2.- Search")
    print("3.- Cart")
    print("4.- Checkout")
    print("5.- Clear Cart")
    print("Q.- Quit")

def print_catalog():
    print_header("- Our catalog -")
    for prod in catalog:
        print(f"| {prod['id']} | {prod['title'].ljust(15)} | ${prod['price']} |")

    answer = input("Type ID to add, or N to close: ").strip()
    if answer.lower() == "n":
        return
    add_product_to_cart(answer)

def add_product_to_cart(prod_id):
    for prod in catalog:
        if str(prod["id"]) == str(prod_id).strip():
            cart.append(prod)
            print(f'{prod["title"]} added to your cart.')
            return
    print("**Error: invalid option**")

def search_product():
    term = input("Search text: ").strip()
    found = False
    for prod in catalog:
        if term.lower() in prod["title"].lower():
            found = True
            print(f'Found: ID {prod["id"]} | {prod["title"]} | ${prod["price"]}')
            choice = input("Do you want this item in your cart? (y/n): ").strip().lower()
            if choice == "y":
                add_product_to_cart(prod["id"])
    if not found:
        print("** No matches found **")

# sum and print total
def total():
    t = 0.0
    for prod in cart:
        try:
            t += float(prod["price"])
        except (TypeError, ValueError):
            pass
    print(f"Total: ${t:.2f}")
    return t

def view_cart():
    print_header("Your Cart")
    if not cart:
        print("Your cart is empty")
    else:
        for prod in cart:
            print(f"| {prod['id']} | {prod['title'].ljust(15)} | ${prod['price']} |")
        print("--------------------")
        print(f"Items: {len(cart)}")
        total()

def checkout():
    print_header("Checkout")
    if not cart:
        print("Your cart is empty. Add items before checking out.")
        return

    name  = input("Full name: ").strip()
    email = input("Email: ").strip()
    phone = input("Phone: ").strip()

    if "@" not in email or "." not in email:
        print("Note: that email looks unusual.")
    if not any(ch.isdigit() for ch in phone):
        print("Note: that phone number looks unusual.")

    print_header("Order Summary")
    for p in cart:
        print(f"| {p['id']} | {p['title'].ljust(15)} | ${p['price']} |")
    print("--------------------")
    total()

    confirm = input("Place order? (y/n): ").strip().lower()
    if confirm == "y":
        print(f"Thanks, {name}! A confirmation will be sent to {email}.")
        cart.clear()
    else:
        print("Order cancelled.")

def clear_cart():
    cart.clear()
    return "your cart has been cleared"

# -------- Initialize --------
option = ""
while option.lower() != "q":
    print_header("Welcome to Store xy")
    print_menu()
    option = input("Choose an option: ").strip()

    if option == "1":
        print_catalog()
    elif option == "2":
        search_product()
    elif option == "3":
        view_cart()
    elif option == "4":
        checkout()
    elif option == "5":
        print_header("Clear Cart")     # don't wrap in print(...)
        print(clear_cart())            # now runs only when option == "5"
    elif option.lower() == "q":
        print("Goodbye!")
    else:
        print("**Error: invalid option**")
