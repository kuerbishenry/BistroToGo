# Dillon Remuck

# Define the menu with items and their prices
menu = {
    "Burger": 5.99,
    "Pizza": 8.99,
    "Pasta": 6.49,
    "Salad": 4.99,
    "Soda": 1.99
}

# Function to display the menu to the user
def display_menu(menu):
    print("Menu:")
    for item, price in menu.items():
        print(f"{item}: ${price}")

# Function to take the user's order
def take_order(menu):
    order = {}
    while True:
        display_menu(menu)
        item = input("Enter the item you want to order (or 'done' to finish): ").capitalize()
        if item.lower() == 'done':
            break
        elif item in menu:
            quantity = int(input(f"How many {item}s do you want to order? "))
            if item in order:
                order[item] += quantity
            else:
                order[item] = quantity
        else:
            print("Invalid item. Please choose from the menu.")
    return order

# Function to calculate the total cost of the order
def calculate_total(order, menu):
    total_cost = 0
    for item, quantity in order.items():
        total_cost += menu[item] * quantity
    return total_cost

# Main function to take the order and display the total cost
def main():
    print("Welcome to the food ordering system!")
    order = take_order(menu)
    total_cost = calculate_total(order, menu)
    print("\nOrder Summary:")
    for item, quantity in order.items():
        print(f"{item}: {quantity}")
    print(f"Total Cost: ${total_cost:.2f}")

# Run the main function
if __name__ == "__main__":
    main()