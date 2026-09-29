inventory = {
    "iphone": {"full_name": "iphone_duo", "price": 1999.99, "quantity": 11},
    "cdj": {"full_name": "cdj_3000x", "price": 2999.00, "quantity": 15},
    "usb": {"full_name": "sandisk_usb_2_set", "price": 40.00, "quantity": 12},
    "djm": {"full_name": "djm_900nxs2_mixer", "price": 2850.00, "quantity": 15}
}

def display_full_inventory():
    # Print a header for the inventory report
    print("\n" + "=" * 40)
    print("          Full Inventory")
    print("=" * 40)  

    # If the dictionary is empty, tell the user and exit the function early
    if not inventory:
        print("Nothing in inventory yet.")
        return

    # Running totals — start at 0 before the loop so we can add to them each pass
    item_total_value = 0.00
    inventory_total_value = 0.00

    # Loop through every item in inventory: 'item' = the key (like "cdj"), 'info' = the inner dict of details
    for item, info in inventory.items():
        print(f"\n\033[1;4m{info['full_name']}\033[0m")  # bold + underline the item's full name
        print(f"price: ${info['price']}")
        print(f"quantity: {info['quantity']}")
        item_total_value = info["price"] * info["quantity"]  # price x quantity = value of this one item
        print(f"item total = {item_total_value:.2f}")
        inventory_total_value += item_total_value  # add this item's value onto the running grand total

    print(f"\nTotal Value of Inventory:  {inventory_total_value}")
    print("=" * 40)


display_full_inventory()

# Ask the user to look up an item by name — loop forever until they type a valid key
while True:
    search = input("\nWhich item would you like to look up: ").lower()

    if search in inventory:
        item = inventory.get(search)
        print(f"\nFound:  {item['full_name']}")
        print(f"Price:  {item['price']}")
        print(f"Quantity:  {item['quantity']}")
        break  # valid input found, exit the loop
    else:
        print(f"No item found for {search}. Please try again.")


# Ask which item's quantity to update — same loop-until-valid pattern as above
while True:
    # To allow the user to update the quantity of a product
    print("\n--- Update Item Quantity ---")
    item_for_quantity_update = input("Which item would you like to update the quantity for:  ").lower()

    if item_for_quantity_update in inventory:
        break  # valid item, stop asking
    else:
        print(f"'{item_for_quantity_update}' is not a valid item. Please try again.")


# By this point, item_for_quantity_update is GUARANTEED to be a valid key —
# the while loop above only breaks once that's true. The inner "if" below
# is technically no longer needed for that reason, but keeping it doesn't hurt.
item_detail_dictionary = inventory.get(item_for_quantity_update)

if item_for_quantity_update in inventory:
    print(f"We have {item_detail_dictionary['quantity']} {item_for_quantity_update}'s in stock right now.")
    user_update_int = input(f"\nBy how much would you like to update the {item_for_quantity_update}'s count by "
          "(positive number for number restocked or negative number for products sold):  ")

    try:
        value = int(user_update_int)  # try converting their text input into a real number
        item_detail_dictionary['quantity'] += value  # add (or subtract, if negative) from current quantity
        print(f"{item_for_quantity_update}'s quantity has been updated to {item_detail_dictionary['quantity']}")
    except ValueError:
        print(f"You must input an integer.")  # runs if int() failed — e.g. they typed letters


# Build a set of items that are running low (quantity under 10)
low_stock = set()

for item, details in inventory.items():
    if details["quantity"] < 10:
        low_stock.add(item)

# Only print the warning if the set actually has something in it
if low_stock:
    message = ", ".join(low_stock)
    print(f"\n{message} are low on stock, please restock that/those items!")