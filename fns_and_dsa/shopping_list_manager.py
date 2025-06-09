# creating an empty list for the shopping cart.

shopping_list = []

def add_item():
    item = input("Enter the item to add: ")
    if item:
        shopping_list.append(item)
        print(f"{item} Added to the list")
    else:
        print("Item name cannot be empty.")

def remove_item():
    item = input("Enter the item to remove: ")
    if item in shopping_list:
        shopping_list.remove(item)
        print(f"{item} has been removed from the list.")

def view_list():
    if shopping_list:
        print("Your Shopping List: ")
        for i, item in enumerate(shopping_list,1):
            print(f"{i}. {item}")
    else:
        print("Your shopping list is currently empty.")

def display_menu():
    print("Menu: ")        
    print("1. Add Item ")        
    print("2. Remove Item ")        
    print("3. View Shopping List ")        
    print("4. Exit ")        

while True:
    display_menu()
    choose = input("Choose an option (1 - 4): ")

    if choose == '1':
        add_item()
    elif choose == '2':
        remove_item()
    elif choose == '3':
        view_list()
    elif choose == '4':
        print("Exiting the program. Goodbye!")
        break
    else:
        print("Invalid choice. Please enter a number between 1 and 4.")