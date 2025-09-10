def print_header(text):
    print("--------------------")
    print(text)
    print("--------------------")

def print_menu():
    print("Menu")
    print("1.- View Catalog")
    # more options here
    print("2.- Create Catalog")
    print("3.- Delete Catalog")
    print("Q.-Quit")

def print_catalog():
    for prod in catalog
        print(prod)

### Initialize
print_header("Welcome to Store xy")
print_menu()

option=input("Choose an option: ")
# print("User selected: " + option)

if option == "1":
    print_catalog