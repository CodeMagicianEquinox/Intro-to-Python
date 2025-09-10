from catalog import catalog

def print_header(text):
    print("--------------------")
    print(text)
    print("--------------------")

def print_menu():
    print("Menu")
    print("1.- View Catalog")
    print("2.- Search")           # <- (1) add the option
    print("Q.- Quit")

def print_catalog():
    print_header("- Our catalog -")
    for prod in catalog:
        print(f"| {prod['id']} | {prod['title'].ljust(15)} | ${prod['price']} |")

    answer = input("Type ID to add, or N to close: ")
    if answer in ("n", "N"):
        return
    else:
        add_product_to_cart(answer)

def add_product_to_cart(prod_id):
    found = False
    for prod in catalog:
        if str(prod["id"]) == prod_id:
            found = True
            print("Found")
    if not found:
        print("**Error: invalid option**")

def search_products():
    # (3) ask for the text to search
    term = input("Search for: ").strip()

    # (4) print the text
    print(f'You typed: "{term}"')

    # Optional: show simple matches by title (case-insensitive)
    matches = [p for p in catalog if term.lower() in p["title"].lower()]
    if matches:
        print_header(f"- Results for: {term} -")
        for prod in matches:
            print(f"| {prod['id']} | {prod['title'].ljust(15)} | ${prod['price']} |")
    else:
        print("No matches.")

# -------- Initialize --------
print_header("Welcome to Store xy")
print_menu()

option = input("Choose an option: ")

if option == "1":
    print_catalog()
elif option == "2":                 # <- (2) handle the search selection
    search_products()
elif option in ("q", "Q"):
    print("Goodbye!")
else:
    print("**Error: invalid option**")
