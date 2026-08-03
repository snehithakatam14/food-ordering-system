import os

# GLOBAL DATA

OWNER_USERNAME = "admin"
OWNER_PASSWORD = "admin123"

restaurant_list = []
food_list = []
user_list = []
cart_list = []
order_list = []

current_user = None

# UTILITY FUNCTIONS

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def banner(title):
    clear_screen()
    print("=" * 50)
    print(title.center(50))
    print("=" * 50)

def pause():
    input("\nPress Enter to continue...")

def generate_restaurant_id():
    return len(restaurant_list) + 1


def generate_food_id():
    return len(food_list) + 101


def generate_order_id():
    return len(order_list) + 1001


# ==========================================
# USER AUTHENTICATION
# ==========================================

def register_user():

    clear_screen()

    print("========== USER REGISTRATION ==========\n")

    username = input("Enter Username : ")

    # Check duplicate username
    for user in user_list:
        if user["username"] == username:
            print("\nUsername already exists!")
            pause()
            return

    password = input("Enter Password : ")
    phone = input("Enter Phone Number : ")

    user = {
        "username": username,
        "password": password,
        "phone": phone,
        "orders": []
    }

    user_list.append(user)

    print("\nRegistration Successful!")

    pause()


def login_user():

    global current_user

    clear_screen()

    print("========== USER LOGIN ==========\n")

    username = input("Username : ")
    password = input("Password : ")

    for user in user_list:

        if user["username"] == username and user["password"] == password:

            current_user = user

            print("\nLogin Successful!")

            pause()

            return True

    print("\nInvalid Credentials!")

    pause()

    return False


# ==========================================
# OWNER LOGIN
# ==========================================

def owner_login():

    clear_screen()

    print("========== OWNER LOGIN ==========\n")

    username = input("Username : ")
    password = input("Password : ")

    if username == OWNER_USERNAME and password == OWNER_PASSWORD:

        print("\nLogin Successful!")

        pause()

        owner_panel()

    else:

        print("\nInvalid Credentials!")

        pause()


# ==========================================
# OWNER PANEL
# ==========================================

def owner_panel():

    while True:

        clear_screen()

        print("======================================")
        print("         OWNER PANEL")
        print("======================================")

        print("1. Dashboard")
        print("2. Manage Restaurants")
        print("3. Manage Food Items")
        print("4. View Orders")
        print("5. Update Order Status")
        print("6. Manage Users")
        print("7. Reports")
        print("8. Logout")

        choice = input("\nEnter Choice : ")

        if choice == "1":
            dashboard()

        elif choice == "2":
            manage_restaurants()

        elif choice == "3":
            manage_food_items()

        elif choice == "4":
            view_orders()

        elif choice == "5":
            update_order_status()

        elif choice == "6":
            manage_users()

        elif choice == "7":
            reports()

        elif choice == "8":
            break

        else:
            print("\nInvalid Choice")
            pause()


# ==========================================
# USER PANEL
# ==========================================

def user_panel():

    while True:

        clear_screen()

        print("======================================")
        print("          USER PANEL")
        print("======================================")

        print("1. Register")
        print("2. Login")
        print("3. Back")

        choice = input("\nEnter Choice : ")

        if choice == "1":

            register_user()

        elif choice == "2":

            if login_user():
                user_dashboard()

        elif choice == "3":
            break

        else:
            print("\nInvalid Choice")
            pause()


# ==========================================
# USER DASHBOARD
# ==========================================

def user_dashboard():

    while True:

        clear_screen()

        print("======================================")
        print(" Welcome,", current_user["username"])
        print("======================================")

        print("1. Browse Restaurants")
        print("2. View Menu")
        print("3. Search Restaurant")
        print("4. Search Food")
        print("5. Add To Cart")
        print("6. Remove From Cart")
        print("7. View Cart")
        print("8. Place Order")
        print("9. Track Order")
        print("10. Order History")
        print("11. Logout")

        choice = input("\nEnter Choice : ")

        if choice == "1":
            browse_restaurants()

        elif choice == "2":
            view_menu()

        elif choice == "3":
            search_restaurant()

        elif choice == "4":
            search_food()

        elif choice == "5":
            add_to_cart()

        elif choice == "6":
            remove_from_cart()

        elif choice == "7":
            view_cart()

        elif choice == "8":
            place_order()

        elif choice == "9":
            track_order()

        elif choice == "10":
            order_history()

        elif choice == "11":
            break


# ==========================================
# PLACEHOLDER FUNCTIONS
# (Will be implemented in later parts)
# ==========================================

def dashboard():

    clear_screen()

    print("===================================")
    print("           DASHBOARD")
    print("===================================")

    print("Total Restaurants :", len(restaurant_list))

    print("Total Food Items  :", len(food_list))

    print("Total Users       :", len(user_list))

    print("Total Orders      :", len(order_list))

    revenue = 0

    for order in order_list:
        revenue += order["total"]

    print("Total Revenue     : ₹", revenue)

    pause()


def manage_restaurants():

    while True:

        clear_screen()

        print("======================================")
        print("     RESTAURANT MANAGEMENT")
        print("======================================")

        print("1. Add Restaurant")
        print("2. View Restaurants")
        print("3. Update Restaurant")
        print("4. Delete Restaurant")
        print("5. Back")

        choice = input("\nEnter Choice : ")

        if choice == "1":
            add_restaurant()

        elif choice == "2":
            view_restaurants()

        elif choice == "3":
            update_restaurant()

        elif choice == "4":
            delete_restaurant()

        elif choice == "5":
            break

        else:
            print("\nInvalid Choice")
            pause()

def add_restaurant():

    clear_screen()

    print("========== ADD RESTAURANT ==========\n")

    name = input("Restaurant Name : ").strip()

    # Check if restaurant already exists
    for restaurant in restaurant_list:
        if restaurant["name"].lower() == name.lower():
            print("\nRestaurant Already Exists.")
            pause()
            return

    location = input("Location : ").strip()

    rid = generate_restaurant_id()

    restaurant = {
        "id": rid,
        "name": name,
        "location": location
    }

    restaurant_list.append(restaurant)

    print("\nRestaurant Added Successfully.")

    pause()
def view_restaurants():

    clear_screen()

    print("========== RESTAURANTS ==========\n")

    if len(restaurant_list) == 0:
        print("No Restaurants Available.")
        pause()
        return

    for restaurant in restaurant_list:

        print("-------------------------------")
        print("Restaurant ID :", restaurant["id"])
        print("Name          :", restaurant["name"])
        print("Location      :", restaurant["location"])

    pause()

def update_restaurant():

    clear_screen()

    print("========== UPDATE RESTAURANT ==========\n")

    if len(restaurant_list) == 0:
        print("No Restaurants Available.")
        pause()
        return

    rid = int(input("Enter Restaurant ID : "))

    for restaurant in restaurant_list:

        if restaurant["id"] == rid:

            print("\nCurrent Name :", restaurant["name"])
            print("Current Location :", restaurant["location"])

            restaurant["name"] = input("\nNew Name : ")

            restaurant["location"] = input("New Location : ")

            print("\nRestaurant Updated Successfully.")

            pause()

            return

    print("\nRestaurant Not Found.")

    pause()
    
def delete_restaurant():

    clear_screen()

    print("========== DELETE RESTAURANT ==========\n")

    if len(restaurant_list) == 0:
        print("No Restaurants Available.")
        pause()
        return

    print("Available Restaurants\n")

    for restaurant in restaurant_list:
        print(restaurant["id"], "-", restaurant["name"])

    try:
        rid = int(input("\nEnter Restaurant ID : "))
    except ValueError:
        print("Invalid Input.")
        pause()
        return

    for restaurant in restaurant_list:

        if restaurant["id"] == rid:

            restaurant_name = restaurant["name"]

            restaurant_list.remove(restaurant)

            # Delete all food items belonging to this restaurant
            food_list[:] = [
                food for food in food_list
                if food["restaurant_id"] != rid
            ]

            print(f"\nRestaurant '{restaurant_name}' Deleted Successfully.")
            print("Associated Food Items Deleted Successfully.")

            pause()
            return

    print("\nRestaurant Not Found.")
    pause()


def manage_food_items():

    while True:

        clear_screen()

        print("======================================")
        print("        FOOD MANAGEMENT")
        print("======================================")

        print("1. Add Food")
        print("2. View Food Items")
        print("3. Update Food")
        print("4. Delete Food")
        print("5. Back")

        choice = input("\nEnter Choice : ")

        if choice == "1":
            add_food()

        elif choice == "2":
            view_food()

        elif choice == "3":
            update_food()

        elif choice == "4":
            delete_food()

        elif choice == "5":
            break

        else:
            print("\nInvalid Choice")
            pause()

def add_food():

    clear_screen()

    print("========== ADD FOOD ==========\n")

    if len(restaurant_list) == 0:
        print("No Restaurants Available.")
        print("Please add a restaurant first.")
        pause()
        return

    print("Available Restaurants\n")

    for restaurant in restaurant_list:
        print(f'{restaurant["id"]}. {restaurant["name"]}')

    try:
        rid = int(input("\nEnter Restaurant ID : "))
    except ValueError:
        print("Invalid Restaurant ID.")
        pause()
        return

    restaurant_name = None

    for restaurant in restaurant_list:
        if restaurant["id"] == rid:
            restaurant_name = restaurant["name"]
            break

    if restaurant_name is None:
        print("\nRestaurant Not Found.")
        pause()
        return

    food_name = input("\nFood Name : ").strip()

    # Prevent duplicate food in the same restaurant
    for food in food_list:
        if (food["restaurant_id"] == rid and
                food["food_name"].lower() == food_name.lower()):
            print("\nThis food already exists in this restaurant.")
            pause()
            return

    try:
        price = float(input("Price : ₹"))
    except ValueError:
        print("Invalid Price.")
        pause()
        return

    if price <= 0:
        print("Price must be greater than zero.")
        pause()
        return

    category = input("Category (Veg / Non-Veg / Beverage): ").strip()

    fid = generate_food_id()

    food = {
        "id": fid,
        "restaurant_id": rid,
        "restaurant_name": restaurant_name,
        "food_name": food_name,
        "price": price,
        "category": category
    }

    food_list.append(food)

    print("\nFood Added Successfully.")

    pause()

    
def view_food():

    clear_screen()

    print("========== FOOD ITEMS ==========\n")

    if len(food_list) == 0:
        print("No Food Items Available.")
        pause()
        return

    for food in food_list:

        print("-----------------------------------------")
        print("Food ID      :", food["id"])
        print("Restaurant   :", food["restaurant_name"])
        print("Food Name    :", food["food_name"])
        print("Category     :", food["category"])
        print("Price        : ₹", food["price"])

    pause()

def update_food():

    clear_screen()

    print("========== UPDATE FOOD ==========\n")

    if len(food_list) == 0:
        print("No Food Items Available.")
        pause()
        return

    try:
        fid = int(input("Enter Food ID : "))
    except ValueError:
        print("Invalid Input")
        pause()
        return

    for food in food_list:

        if food["id"] == fid:

            print("\nCurrent Name :", food["food_name"])
            print("Current Price :", food["price"])
            print("Current Category :", food["category"])

            food["food_name"] = input("\nNew Food Name : ")

            try:
                food["price"] = float(input("New Price : ₹"))
            except ValueError:
                print("Invalid Price")
                pause()
                return

            food["category"] = input("New Category : ")

            print("\nFood Updated Successfully.")

            pause()

            return

    print("\nFood Not Found.")

    pause()

def delete_food():

    clear_screen()

    print("========== DELETE FOOD ==========\n")

    if len(food_list) == 0:
        print("No Food Items Available.")
        pause()
        return

    try:
        fid = int(input("Enter Food ID : "))
    except ValueError:
        print("Invalid Input")
        pause()
        return

    for food in food_list:

        if food["id"] == fid:

            food_list.remove(food)

            print("\nFood Deleted Successfully.")

            pause()

            return

    print("\nFood Not Found.")

    pause()


def view_orders():

    clear_screen()

    print("========== ALL ORDERS ==========\n")

    if len(order_list) == 0:
        print("No Orders Yet.")
        pause()
        return

    for order in order_list:

        print("--------------------------------------")

        print("Order ID :", order["order_id"])
        print("Customer :", order["username"])
        print("Status   :", order["status"])
        print("Amount   : ₹", order["total"])

        print("\nItems")

        for item in order["items"]:

            print(item["food_name"],
                  "x",
                  item["quantity"])

    pause()

def update_order_status():

    clear_screen()

    print("========== UPDATE ORDER STATUS ==========\n")

    if len(order_list) == 0:
        print("No Orders Available.")
        pause()
        return

    # Display all orders
    for order in order_list:
        print("--------------------------------")
        print("Order ID :", order["order_id"])
        print("Customer :", order["username"])
        print("Current Status :", order["status"])

    try:
        oid = int(input("\nEnter Order ID : "))
    except ValueError:
        print("Invalid Input.")
        pause()
        return

    for order in order_list:

        if order["order_id"] == oid:

            print("\nSelect New Status")
            print("1. Placed")
            print("2. Preparing")
            print("3. Out For Delivery")
            print("4. Delivered")

            choice = input("\nEnter Choice : ")

            if choice == "1":
                new_status = "Placed"

            elif choice == "2":
                new_status = "Preparing"

            elif choice == "3":
                new_status = "Out For Delivery"

            elif choice == "4":
                new_status = "Delivered"

            else:
                print("Invalid Choice.")
                pause()
                return

            # Update status in main order list
            order["status"] = new_status

            # Update status in user's order history
            for user in user_list:

                if user["username"] == order["username"]:

                    for user_order in user["orders"]:

                        if user_order["order_id"] == order["order_id"]:
                            user_order["status"] = new_status
                            break

            print("\nOrder Status Updated Successfully.")

            pause()
            return

    print("\nOrder Not Found.")

    pause()
    
    
def manage_users():

    clear_screen()

    print("============== USERS ==============\n")

    if len(user_list) == 0:

        print("No Users Registered.")

        pause()

        return

    for user in user_list:

        print("-------------------------------")

        print("Username :", user["username"])

        print("Phone    :", user["phone"])

    pause()


def reports():

    clear_screen()

    print("========== REPORTS ==========\n")

    if len(order_list) == 0:
        print("No Orders Available.")
        pause()
        return

    total_orders = len(order_list)
    total_revenue = 0

    food_counter = {}

    for order in order_list:

        total_revenue += order["total"]

        for item in order["items"]:

            name = item["food_name"]

            if name in food_counter:
                food_counter[name] += item["quantity"]
            else:
                food_counter[name] = item["quantity"]

    print("Total Restaurants :", len(restaurant_list))
    print("Total Food Items  :", len(food_list))
    print("Total Users       :", len(user_list))
    print("Total Orders      :", total_orders)
    print("Total Revenue     : ₹", total_revenue)

    print("\nMost Ordered Food")

    most_food = ""
    max_count = 0

    for food in food_counter:

        if food_counter[food] > max_count:

            max_count = food_counter[food]
            most_food = food

    print(most_food, "-", max_count, "Orders")

    pause()


def search_restaurant():

    clear_screen()

    print("========== SEARCH RESTAURANT ==========\n")

    keyword = input("Enter Restaurant Name : ").lower()

    found = False

    for restaurant in restaurant_list:

        if keyword in restaurant["name"].lower():

            found = True

            print("-----------------------------")
            print("ID :", restaurant["id"])
            print("Name :", restaurant["name"])
            print("Location :", restaurant["location"])

    if not found:
        print("\nRestaurant Not Found.")

    pause()

def search_food():

    clear_screen()

    print("========== SEARCH FOOD ==========\n")

    keyword = input("Enter Food Name : ").lower()

    found = False

    for food in food_list:

        if keyword in food["food_name"].lower():

            found = True

            print("-----------------------------")
            print("Restaurant :", food["restaurant_name"])
            print("Food :", food["food_name"])
            print("Price : ₹", food["price"])

    if not found:
        print("\nFood Not Found.")

    pause()
    


def browse_restaurants():

    clear_screen()

    print("========== RESTAURANTS ==========\n")

    if len(restaurant_list) == 0:
        print("No Restaurants Available.")
        pause()
        return

    for restaurant in restaurant_list:

        print("--------------------------------")
        print("Restaurant ID :", restaurant["id"])
        print("Restaurant    :", restaurant["name"])
        print("Location      :", restaurant["location"])

    pause()


def view_menu():

    clear_screen()

    print("========== VIEW MENU ==========\n")

    if len(restaurant_list) == 0:
        print("No Restaurants Available.")
        pause()
        return

    for restaurant in restaurant_list:
        print(restaurant["id"], "-", restaurant["name"])

    try:
        rid = int(input("\nEnter Restaurant ID : "))
    except:
        print("Invalid Input")
        pause()
        return

    found = False

    print("\n========== MENU ==========\n")

    for food in food_list:

        if food["restaurant_id"] == rid:

            found = True

            print("--------------------------------")
            print("Food ID :", food["id"])
            print("Food    :", food["food_name"])
            print("Category:", food["category"])
            print("Price   : ₹", food["price"])

    if found == False:
        print("No Food Items Found.")

    pause()


def add_to_cart():

    clear_screen()

    print("========== ADD TO CART ==========\n")

    if len(food_list) == 0:
        print("No Food Items Available.")
        pause()
        return

    # Display all food items
    for food in food_list:
        print("--------------------------------")
        print(food["id"], "-", food["food_name"], "- ₹", food["price"])

    # Get Food ID
    try:
        fid = int(input("\nEnter Food ID : "))
    except ValueError:
        print("Invalid Input")
        pause()
        return

    # Search for the selected food
    for food in food_list:

        if food["id"] == fid:

            # Get quantity
            try:
                qty = int(input("Quantity : "))
            except ValueError:
                print("Invalid Quantity")
                pause()
                return

            # Check if the item is already in the user's cart
            for item in cart_list:

                if (item["username"] == current_user["username"] and
                        item["food_id"] == fid):

                    item["quantity"] += qty
                    item["subtotal"] = item["quantity"] * item["price"]

                    print("\nQuantity Updated Successfully.")

                    pause()
                    return

            # If item is not in cart, create a new cart entry
            cart_item = {
                "username": current_user["username"],
                "food_id": food["id"],
                "food_name": food["food_name"],
                "restaurant": food["restaurant_name"],
                "price": food["price"],
                "quantity": qty,
                "subtotal": qty * food["price"]
            }

            cart_list.append(cart_item)

            print("\nAdded To Cart Successfully.")

            pause()
            return

    print("\nFood Not Found.")
    pause()

def remove_from_cart():

    clear_screen()

    print("========== REMOVE FROM CART ==========\n")

    user_cart = []

    for item in cart_list:
        if item["username"] == current_user["username"]:
            user_cart.append(item)

    if len(user_cart) == 0:
        print("Cart Empty.")
        pause()
        return

    for item in user_cart:
        print("--------------------------------")
        print(item["food_id"], "-", item["food_name"])

    try:
        fid = int(input("\nEnter Food ID To Remove : "))
    except:
        print("Invalid Input")
        pause()
        return

    for item in cart_list:

        if item["username"] == current_user["username"] and item["food_id"] == fid:

            cart_list.remove(item)

            print("\nItem Removed Successfully.")

            pause()

            return

    print("\nFood Not Found In Cart.")

    pause()


def view_cart():

    clear_screen()

    print("========== YOUR CART ==========\n")

    total = 0

    found = False

    for item in cart_list:

        if item["username"] == current_user["username"]:

            found = True

            print("--------------------------------")
            print("Food :", item["food_name"])
            print("Restaurant :", item["restaurant"])
            print("Price :", item["price"])
            print("Quantity :", item["quantity"])
            print("Subtotal : ₹", item["subtotal"])

            total += item["subtotal"]

    if found == False:
        print("Cart Empty.")
    else:
        print("\n-------------------------------")
        print("Grand Total : ₹", total)

    pause()


def place_order():

    global cart_list

    clear_screen()

    print("========== PLACE ORDER ==========\n")

    user_cart = []
    total = 0

    # Get current user's cart items
    for item in cart_list:
        if item["username"] == current_user["username"]:
            user_cart.append(item)
            total += item["subtotal"]

    if len(user_cart) == 0:
        print("Your Cart is Empty.")
        pause()
        return

    print("YOUR ORDER\n")

    for item in user_cart:
        print("--------------------------------")
        print("Food       :", item["food_name"])
        print("Restaurant :", item["restaurant"])
        print("Price      : ₹", item["price"])
        print("Quantity   :", item["quantity"])
        print("Subtotal   : ₹", item["subtotal"])

    print("\n------------------------------")

    gst = total * 0.05
    delivery = 40
    final_total = total + gst + delivery

    print("Subtotal         : ₹", total)
    print("GST (5%)         : ₹", round(gst, 2))
    print("Delivery Charge  : ₹", delivery)
    print("------------------------------")
    print("Grand Total      : ₹", round(final_total, 2))

    choice = input("\nConfirm Order? (Y/N) : ")

    if choice.lower() != "y":
        print("\nOrder Cancelled.")
        pause()
        return

    order = {
        "order_id": generate_order_id(),
        "username": current_user["username"],
        "items": user_cart.copy(),
        "total": round(final_total, 2),
        "status": "Placed"
    }

    # Save order
    order_list.append(order)

    # Save to user's history
    current_user["orders"].append(order)

    # Remove all items from current user's cart
    cart_list = [
        item for item in cart_list
        if item["username"] != current_user["username"]
    ]

    print("\n=================================")
    print("Order Placed Successfully!")
    print("Order ID :", order["order_id"])
    print("=================================")

    pause()

def track_order():

    clear_screen()

    print("========== TRACK ORDER ==========\n")

    found = False

    for order in order_list:

        if order["username"] == current_user["username"]:

            found = True

            print("-------------------------------------")
            print("Order ID :", order["order_id"])
            print("Status   :", order["status"])
            print("Amount   : ₹", order["total"])
            print("-------------------------------------")

    if not found:
        print("No Orders Found.")

    pause()

    
def order_history():

    clear_screen()

    print("========== ORDER HISTORY ==========\n")

    found = False

    for order in current_user["orders"]:

        found = True

        print("--------------------------------------")
        print("Order ID :", order["order_id"])
        print("Status   :", order["status"])
        print("Total    : ₹", order["total"])

        print("\nItems Ordered")

        for item in order["items"]:

            print(item["food_name"],
                  "x",
                  item["quantity"],
                  "= ₹",
                  item["subtotal"])

    if found == False:
        print("No Order History.")

    pause()


# ==========================================
# MAIN MENU
# ==========================================

def main():

    while True:

        clear_screen()

        banner("FOOD ORDERING MANAGEMENT SYSTEM")
        print("        Welcome to FoodHub\n")

        print("1. Owner Panel")
        print("2. User Panel")
        print("3. Exit")

        choice = input("\nEnter Choice : ")

        if choice == "1":
            owner_login()

        elif choice == "2":
            user_panel()

        elif choice == "3":
            print("\nThank You For Using The System.")
            break

        else:
            print("\nInvalid Choice.")
            pause()


# ==========================================
# PROGRAM STARTS HERE
# ==========================================

main()
