# ============================================
# PIZZA ORDER SYSTEM — Complete Program
# ============================================

# ----- Menu Data -----
sizes = ["Personal (8\")", "Medium (12\")", "Large (16\")", "Party (20\")"]
size_prices = [6.99, 9.99, 12.99, 16.99]

topping_names = ["Pepperoni", "Mushrooms", "Green Peppers", "Onions",
                 "Sausage", "Bacon", "Extra Cheese", "Pineapple"]
topping_price = 1.50

# ----- Order Storage -----
order_descriptions = []
order_prices = []

print("Welcome to the CS 1300 Pizza Shop!\n")

# ===== ORDERING LOOP =====
while True:

    # ----- EX 1: Display Menu -----
    print("==============================")
    print("       PIZZA SIZES")
    print("==============================")
    for i in range(len(sizes)):
        print(f"{i+1}. {sizes[i]:<18} ${size_prices[i]:>5.2f}")
    print("==============================")

    # ----- EX 2: Choose Size -----
    while True:
        choice = input("Pick a size (1-4): ")
        try:
            choice = int(choice)
            if 1 <= choice <= 4:
                size_choice = choice - 1
                base_price = size_prices[size_choice]
                break
            else:
                print("  Choose 1-4.")
        except ValueError:
            print("  Please enter a number!")

    # ----- EX 3: Add Toppings -----
    selected_toppings = []

    print("\nAvailable toppings ($1.50 each):")
    for i in range(len(topping_names)):
        print(f"  {i+1}. {topping_names[i]}")

    while True:
        topping = input("Add topping # (or 'done'): ").lower()

        if topping == "done":
            break

        try:
            topping = int(topping)
            if 1 <= topping <= len(topping_names):
                topping_name = topping_names[topping - 1]

                if topping_name in selected_toppings:
                    print(f"  Already added {topping_name}!")
                    continue

                selected_toppings.append(topping_name)
                print(f"  ✓ Added {topping_name}")
            else:
                print("  Invalid topping number.")
        except ValueError:
            print("  Enter a number or 'done'.")

    # ----- EX 4: Calculate Price -----
    price = base_price + len(selected_toppings) * topping_price

    if selected_toppings:
        toppings_str = ", ".join(selected_toppings)
    else:
        toppings_str = "Cheese"

    description = f"{sizes[size_choice]} {toppings_str}"

    order_descriptions.append(description)
    order_prices.append(price)

    # ----- EX 5: Order Another -----
    while True:
        again = input("\nOrder another pizza? (yes/no): ").lower()
        if again in ["yes", "y"]:
            break
        elif again in ["no", "n"]:
            break
        else:
            print("  Please enter yes or no.")

    if again in ["no", "n"]:
        break

# ===== POST-ORDER =====
if not order_descriptions:
    print("\nNo pizzas ordered. See you next time!")
else:

    # ----- EX 8: Discount Code -----
    discount = 0
    attempts = 0

    while attempts < 3:
        code = input("\nEnter discount code (or 'none'): ").upper()

        if code == "NONE":
            break
        elif code == "STUDENT10":
            discount = 0.10
            print("  10% discount applied!")
            break
        elif code == "HALFOFF":
            discount = 0.50
            print("  50% discount applied!")
            break
        else:
            attempts += 1
            print("  Invalid code.")

    if attempts == 3:
        print("No discount applied.")

    # ----- EX 6: Receipt -----
    print("\n====================================")
    print("         YOUR ORDER RECEIPT")
    print("====================================")

    subtotal = 0

    for i in range(len(order_descriptions)):
        print(f"{i+1}. {order_descriptions[i]}")
        print(f"{'':30} ${order_prices[i]:>6.2f}")
        subtotal += order_prices[i]

    # apply discount
    discount_amount = subtotal * discount
    subtotal_after_discount = subtotal - discount_amount

    tax = subtotal_after_discount * 0.07
    total = subtotal_after_discount + tax

    print("------------------------------------")
    print(f"Subtotal:                  ${subtotal:>6.2f}")
    print(f"Discount:                 -${discount_amount:>6.2f}")
    print(f"Tax (7%):                 ${tax:>6.2f}")
    print(f"Total:                    ${total:>6.2f}")
    print("====================================")

    # ----- EX 7: Most Expensive -----
    max_price = max(order_prices)
    max_index = order_prices.index(max_price)

    print(f"\nMost expensive pizza:")
    print(f"{order_descriptions[max_index]} (${max_price:.2f})")

    # ----- EX 9: Count by Size -----
    counts = [0, 0, 0, 0]

    for desc in order_descriptions:
        for i in range(len(sizes)):
            if sizes[i] in desc:
                counts[i] += 1

    print("\nPizza count by size:")
    for i in range(len(sizes)):
        print(f"{sizes[i]}: {counts[i]}")

    print("\nThank you for your order!")