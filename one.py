 # Restaurant Order Management System

# Step 1: Create the menu
menu = {
    "Burger": 100,
    "Pizza": 200,
    "Coffee": 50
}

# Step 2: Display the menu
print("===== RESTAURANT MENU =====")

for item, price in menu.items():
    print(f"{item}: Rs.{price}")

# Step 3: Select table number
while True:
    try:
        table = int(input("\nEnter table number (1-20): "))

        if 1 <= table <= 20:
            break
        else:
            print("Invalid table! Choose between 1 and 20.")

    except ValueError:
        print("Please enter a valid number.")

# Step 4: Create an empty order list
order = []

# Step 5: Take customer orders
while True:

    item = input(
        "\nEnter item name (or 'done' to finish): "
    ).strip().title()

    # Stop ordering
    if item == "Done":
        break

    # Validate menu item
    if item not in menu:
        print("Invalid item! Available: Burger, Pizza, Coffee")
        continue

    # Take quantity
    try:
        quantity = int(input("Enter quantity: "))

        if quantity <= 0:
            print("Quantity must be greater than zero.")
            continue

    except ValueError:
        print("Invalid quantity! Enter a whole number.")
        continue

    # Calculate item amount
    price = menu[item]
    amount = price * quantity

    # Add item to order list
    order.append({
        "item": item,
        "quantity": quantity,
        "price": price,
        "amount": amount
    })

    print(f"{item} x {quantity} added to Table {table}")
    print(f"Amount: Rs.{amount}")

    # Show running order
    print("\n===== RUNNING ORDER =====")

    for food in order:
        print(
            f"{food['item']} x {food['quantity']} "
            f"= Rs.{food['amount']}"
        )

# Step 6: Generate final bill

subtotal = sum(food["amount"] for food in order)

service_charge = subtotal * 0.10
gst = subtotal * 0.05
total = subtotal + service_charge + gst

# Step 7: Print final bill

print("\n========== FINAL BILL ==========")
print(f"Table Number: {table}")

print("--------------------------------")
print("Item       Qty     Price    Amount")
print("--------------------------------")

for food in order:
    print(
        f"{food['item']:<10}"
        f"{food['quantity']:<8}"
        f"{food['price']:<9}"
        f"{food['amount']}"
    )

print("--------------------------------")
print(f"Subtotal:         Rs.{subtotal:.2f}")
print(f"Service Charge:   Rs.{service_charge:.2f}")
print(f"GST (5%):         Rs.{gst:.2f}")
print("--------------------------------")
print(f"Total Bill:       Rs.{total:.2f}")
print("================================")
print("Thank you for visiting!")