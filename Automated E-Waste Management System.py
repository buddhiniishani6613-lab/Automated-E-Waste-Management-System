# Automated E-Waste Management System

items = []
MAX_STORAGE = 1000
FEE_PER_KG = 10


def add_item():

    total_storage = sum(item["weight"] for item in items)

    if total_storage >= MAX_STORAGE:
        print("Storage Full! Cannot add items.")
        return

    item_id = input("Enter Item ID: ")
    name = input("Enter Device Name: ")

    category = input(
        "Enter Category (Recyclable/Hazardous/Non-Recyclable): "
    )

    if category not in [
        "Recyclable",
        "Hazardous",
        "Non-Recyclable"
    ]:
        print("Invalid Category")
        return

    try:
        weight = float(input("Enter Weight (kg): "))

        if weight <= 0:
            print("Weight must be positive")
            return

    except ValueError:
        print("Invalid Weight")
        return

    fee = weight * FEE_PER_KG

    if weight > 50:
        discount = fee * 0.05
        fee -= discount
    else:
        discount = 0

    item = {
        "id": item_id,
        "name": name,
        "category": category,
        "weight": weight,
        "fee": fee,
        "status": "Stored"
    }

    items.append(item)

    print("Item Added Successfully")


def view_items():

    if len(items) == 0:
        print("No items available")
        return

    for item in items:
        print(item)


def search_item():

    search = input("Enter Item ID or Name: ")

    found = False

    for item in items:

        if item["id"] == search or item["name"] == search:
            print(item)
            found = True

    if not found:
        print("Item Not Found")


def update_item():

    item_id = input("Enter Item ID to update: ")

    for item in items:

        if item["id"] == item_id:

            new_weight = float(input("Enter New Weight: "))
            item["weight"] = new_weight

            item["fee"] = new_weight * FEE_PER_KG

            print("Item Updated")
            return

    print("Item Not Found")


def delete_item():

    item_id = input("Enter Item ID to delete: ")

    for item in items:

        if item["id"] == item_id:
            items.remove(item)
            print("Item Deleted")
            return

    print("Item Not Found")


def storage_status():

    total_weight = sum(item["weight"] for item in items)

    print(f"Current Storage: {total_weight} kg")

    if total_weight >= 800:
        print("Warning! Storage above 80%")

    if total_weight >= MAX_STORAGE:
        print("Storage Full")


def generate_report():

    total_weight = sum(item["weight"] for item in items)

    total_fee = sum(item["fee"] for item in items)

    print("\n===== REPORT =====")
    print("Total Items:", len(items))
    print("Total Weight:", total_weight)
    print("Total Fees:", total_fee)


while True:

    print("\n===== AEWMS MENU =====")
    print("1. Add Item")
    print("2. View Items")
    print("3. Search Item")
    print("4. Update Item")
    print("5. Delete Item")
    print("6. Storage Status")
    print("7. Generate Report")
    print("8. Exit")

    choice = input("Enter Choice: ")

    if choice == "1":
        add_item()

    elif choice == "2":
        view_items()

    elif choice == "3":
        search_item()

    elif choice == "4":
        update_item()

    elif choice == "5":
        delete_item()

    elif choice == "6":
        storage_status()

    elif choice == "7":
        generate_report()

    elif choice == "8":
        print("Program Closed")
        break

    else:
        print("Invalid Choice")