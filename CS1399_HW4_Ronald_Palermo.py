# Problem 1: Movie Ticket Pricing
age_input = input("Enter your age: ")

if not age_input.isdigit():
    print("Error: Age must be a non-negative integer.")
else:
    age = int(age_input)

    if age < 0:
        print("Error: Age cannot be negative.")
    else:
        matinee_input = input("Is this a matinee showing? (yes/no): ").strip().lower()

        is_matinee = True if matinee_input == "yes" else False

        if age < 13:
            age_group = "Child"
            if is_matinee:
                price = 6.00
            else:
                price = 8.00

        elif 13 <= age <= 17:
            age_group = "Teen"
            if is_matinee:
                price = 7.00
            else:
                price = 10.00

        elif 18 <= age <= 64:
            age_group = "Adult"
            if is_matinee:
                price = 8.00
            else:
                price = 13.00

        else:  # age 65+
            age_group = "Senior"
            if is_matinee:
                price = 6.00
            else:
                price = 7.00

        print(f"Age group: {age_group}")
        print(f"Ticket price: ${price:.2f}")

#############################################################################

# Problem 2: Input Validator
errors = []

# ---- Collect Inputs ----
student_id = input("Enter student ID: ")
full_name = input("Enter full name: ")
age_input = input("Enter age: ")
major_input = input("Enter major: ")

if len(student_id) != 8:
    errors.append(f"Student ID must be exactly 8 characters (got {len(student_id)})")

if not student_id[:1].isalpha():
    errors.append("Student ID must start with a letter")

if len(student_id) == 8 and not student_id[1:].isdigit():
    errors.append("Student ID must have 7 digits after the first letter")

name_clean = full_name.strip()

if len(name_clean) == 0:
    errors.append("Name cannot be empty")
elif len(name_clean) < 2:
    errors.append("Name must be at least 2 characters long")

try:
    age = int(age_input)
    if age < 16 or age > 99:
        errors.append("Age must be between 16 and 99")
except ValueError:
    errors.append("Age must be a valid integer")

valid_majors = ["CS", "IT", "CE", "DS"]
major = major_input.strip().upper()

if major not in valid_majors:
    errors.append(f"Major must be one of: CS, IT, CE, DS (got {major_input})")

# Output
if not errors:
    print("✓ Profile created successfully!")
    print(f"Student ID: {student_id}")
    print(f"Name: {name_clean}")
    print(f"Age: {age}")
    print(f"Major: {major}")
else:
    print("✗ Profile has errors:")
    for error in errors:
        print(f"- {error}")
        
#######################################################################

# Problem 3: Campus Café Menu
TAX_RATE = 0.07

def get_menu_choice():
    """Display menu and get a valid choice from the user."""
    print("=" * 30)
    print("CAMPUS CAFÉ ORDER SYSTEM")
    print("=" * 30)
    print("1. Coffee - $3.50")
    print("2. Sandwich - $6.00")
    print("3. Salad - $5.50")
    print("4. Combo (Sandwich + Coffee) - $8.00")
    print("5. Exit")
    print("=" * 30)

    choice = input("Enter your choice (1-5): ")
    return choice

def get_quantity():
    """Prompt for quantity and validate positive integer."""
    try:
        qty = int(input("How many? "))
        if qty <= 0:
            print("Quantity must be positive. Defaulting to 1.")
            return 1
        return qty
    except ValueError:
        print("Invalid quantity. Defaulting to 1.")
        return 1

def get_customer_name():
    """Prompt for a non-empty customer name."""
    name = input("Enter your name: ").strip()
    if not name:
        print("Name cannot be empty. Using 'Guest'.")
        return "Guest"
    return name

# ---- Main Program ----
choice = get_menu_choice()

if choice == "5":
    print("Goodbye!")
else:
    item_name = ""
    unit_price = 0.0

    # ---- Coffee ----
    if choice == "1":
        item_name = "Coffee"
        unit_price = 3.50

        size = input("Choose size (Small/Medium/Large): ").strip().lower()

        if size == "medium":
            unit_price += 1.00
            item_name += " (Medium)"
        elif size == "large":
            unit_price += 2.00
            item_name += " (Large)"
        else:
            item_name += " (Small)"

    # ---- Sandwich ----
    elif choice == "2":
        item_name = "Sandwich"
        unit_price = 6.00

        cheese = input("Add cheese? (yes/no): ").strip().lower()
        if cheese == "yes":
            unit_price += 0.75
            item_name += " + Cheese"

    # ---- Salad ----
    elif choice == "3":
        item_name = "Salad"
        unit_price = 5.50

        dressing = input("Choose dressing (ranch/italian/vinaigrette/none): ").strip().lower()
        valid_dressings = ["ranch", "italian", "vinaigrette", "none"]

        if dressing not in valid_dressings:
            print("Invalid dressing. Defaulting to none.")
            dressing = "none"

        if dressing != "none":
            item_name += f" ({dressing.capitalize()})"

    # ---- Combo ----
    elif choice == "4":
        item_name = "Combo"
        unit_price = 8.00

        # Coffee size customization
        size = input("Choose coffee size (Small/Medium/Large): ").strip().lower()
        if size == "medium":
            unit_price += 1.00
            item_name += " + Medium Coffee"
        elif size == "large":
            unit_price += 2.00
            item_name += " + Large Coffee"
        else:
            item_name += " + Small Coffee"

        # Cheese option
        cheese = input("Add cheese to sandwich? (yes/no): ").strip().lower()
        if cheese == "yes":
            unit_price += 0.75
            item_name += " + Cheese"

    else:
        print("Invalid menu choice.")
        exit()

    # ---- Get customer info ----
    name = get_customer_name()
    quantity = get_quantity()

    # ---- Calculate totals ----
    subtotal = unit_price * quantity
    tax = subtotal * TAX_RATE
    total = subtotal + tax

    # ---- Print receipt ----
    print("\n" + "=" * 30)
    print("ORDER RECEIPT")
    print("=" * 30)
    print(f"Customer: {name}")
    print(f"Item: {item_name}")
    print(f"Quantity: {quantity}")
    print(f"Unit Price: ${unit_price:.2f}")
    print(f"Subtotal: ${subtotal:.2f}")
    print(f"Tax (7%): ${tax:.2f}")
    print(f"Total: ${total:.2f}")
    print("=" * 30)
    print("Thank you for your order!")