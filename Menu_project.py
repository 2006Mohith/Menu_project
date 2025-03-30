def main():
    # Menu items and their prices
    menu_items = ["Burger", "Pizza", "Pasta", "Salad", "Soft Drink", "Ice Cream"]
    menu_prices = [120.0, 200.0, 150.0, 80.0, 50.0, 60.0]

    # Combo deals and their prices
    combo_deals = ["Burger + Soft Drink", "Pizza + Soft Drink", "Pasta + Salad", "Burger + Ice Cream"]
    combo_prices = [150.0, 230.0, 200.0, 160.0]

    print("🍽 Welcome to Our Restaurant! 🍽")
    budget = float(input("Enter your budget: ₹"))

    order = []
    total_cost = 0.0

    while True:
        print("\n✅ Items you can afford now:")
        available_items = []

        # Display affordable menu items
        for i, (item, price) in enumerate(zip(menu_items, menu_prices), start=1):
            if price <= (budget - total_cost):
                available_items.append((i, item, price))
                print(f"{i}. {item} (₹{price:.2f})")

        # Display affordable combo meals
        total_items = len(menu_items)
        for i, (combo, price) in enumerate(zip(combo_deals, combo_prices), start=total_items + 1):
            if price <= (budget - total_cost):
                available_items.append((i, combo, price))
                print(f"{i}. {combo} (₹{price:.2f})")

        if not available_items:  
            # No items available with remaining budget
            print("\n🚫 No items are affordable with your remaining budget.")

            choice = input("Do you want to remove items from your cart? (yes/no): ").strip().lower()
            if choice == "yes":
                total_cost = remove_items(order, menu_items, menu_prices, combo_deals, combo_prices, budget, total_cost)
            else:
                print_bill(order, menu_items, menu_prices, combo_deals, combo_prices)
                return  # Exit and show final bill

        print("\n🛒 Enter the number of the item you want to order (Enter 0 to finish):")
        choice = input().strip()

        if choice == "":
            print(⚠️ Please enter a valid number.")
            continue

        choice = int(choice)

        if choice == 0:
            break

        if choice < 1 or choice > total_items + len(combo_deals):
            print("❌ Invalid choice. Please try again.")
            continue

        # Determine selected item's price
        if choice <= total_items:
            selected_price = menu_prices[choice - 1]
        else:
            selected_price = combo_prices[choice - total_items - 1]

        # Check affordability
        if total_cost + selected_price > budget:
            print("💰 Not enough budget to add this item. Try removing something.")
            total_cost = remove_items(order, menu_items, menu_prices, combo_deals, combo_prices, budget, total_cost)
            continue

        # Add item to order
        order.append(choice)
        total_cost += selected_price
        print(f"✔ Added to your order! Remaining budget: ₹{budget - total_cost:.2f}")

    # Display final order summary
    print_bill(order, menu_items, menu_prices, combo_deals, combo_prices)


def remove_items(order, menu_items, menu_prices, combo_deals, combo_prices, budget, total_cost):
    """ Allows the user to remove multiple items to free up budget. """
    while order:
        print("\n🗑️ Your current order:")
        for idx, o in enumerate(order, start=1):
            if o <= len(menu_items):
                print(f"{idx}. {menu_items[o - 1]} (₹{menu_prices[o - 1]:.2f})")
            else:
                print(f"{idx}. {combo_deals[o - len(menu_items) - 1]} (₹{combo_prices[o - len(menu_items) - 1]:.2f})")

        remove_choices = input("\nEnter item numbers to remove (comma-separated) or 'no' to exit: ").strip()
        if remove_choices.lower() == "no":
            return total_cost  # Exit the removal process

        remove_choices = [int(x) for x in remove_choices.split(",") if x.isdigit()]
        removed_cost = 0.0

        for rc in sorted(remove_choices, reverse=True):
            if 1 <= rc <= len(order):
                removed_item = order.pop(rc - 1)
                if removed_item <= len(menu_items):
                    removed_cost += menu_prices[removed_item - 1]
                else:
                    removed_cost += combo_prices[removed_item - len(menu_items) - 1]

        total_cost -= removed_cost
        print(f"✔ Items removed! Remaining budget: ₹{budget - total_cost:.2f}")

        if total_cost < budget:
            return total_cost  # Return updated total cost

    return total_cost  # Ensure we return the final cost


def print_bill(order, menu_items, menu_prices, combo_deals, combo_prices):
    print("\n" + "=" * 40)
    print("🧾  YOUR FINAL BILL  🧾".center(40))
    print("=" * 40)

    total_cost = 0.0  # Reset total cost to ensure only valid items are counted

    for choice in order:
        if choice <= len(menu_items):
            item_name = menu_items[choice - 1]
            item_price = menu_prices[choice - 1]
        else:
            item_name = combo_deals[choice - len(menu_items) - 1]
            item_price = combo_prices[choice - len(menu_items) - 1]

        total_cost += item_price
        print(f"🍽️ {item_name.ljust(25)} ₹{item_price:.2f}")

    print("-" * 40)
    print(f"💰 TOTAL AMOUNT: ₹{total_cost:.2f}".rjust(40))
    print("=" * 40)
    print("🎉 THANK YOU FOR ORDERING! ENJOY YOUR MEAL! 🍔🍕🥗")
    print("=" * 40)


if __name__ == "__main__":
    main()
